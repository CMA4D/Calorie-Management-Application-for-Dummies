from http.server import BaseHTTPRequestHandler, HTTPServer
from hx711 import HX711
import RPi.GPIO as GPIO
import cv2
import os
import time
import signal
import sys
from collections import deque
import pigpio

# 初始化 HX711
hx = HX711(5, 6)
reference_unit = 315  # 校准参数
samples = deque(maxlen=10)  # 存储最近10次读数

# 初始化摄像头
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

# 初始化 SPI 12864 屏幕
pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("pigpio")

# SPI 12864 引脚定义
RS = 17       # RS (数据/指令选择)
E = 18        # E (使能信号)
PSB = 21
VO = 26
DATA_PINS = [22, 23, 24, 25]  # DB4-DB7

# 初始化 GPIO
pi.set_mode(RS, pigpio.OUTPUT)
pi.set_mode(E, pigpio.OUTPUT)
pi.set_mode(PSB, pigpio.OUTPUT)
pi.set_mode(VO, pigpio.OUTPUT)
for pin in DATA_PINS:
    pi.set_mode(pin, pigpio.OUTPUT)
pi.write(PSB, 1)

def send_nibble(data, is_command=True):
    pi.write(RS, 0 if is_command else 1)  # RS=0:命令, RS=1:数据
    for i in range(4):
        pi.write(DATA_PINS[i], (data >> i) & 1)  # 写入高 4 位
    pi.write(E, 1)  # 使能脉冲
    time.sleep(0.001)
    pi.write(E, 0)
    time.sleep(0.001)

def send_byte(data, is_command=True):
    send_nibble(data >> 4, is_command)  # 先发送高 4 位
    send_nibble(data & 0x0F, is_command)  # 再发送低 4 位

def init_lcd():
    time.sleep(0.05)
    send_nibble(0x03)  # 初始化序列
    time.sleep(0.005)
    send_nibble(0x03)
    time.sleep(0.001)
    send_nibble(0x03)
    send_nibble(0x02)  # 切换到 4-bit 模式
    send_byte(0x28)    # 2行显示, 4-bit 数据
    send_byte(0x0C)    # 显示开，无光标
    send_byte(0x01)    # 清屏
    time.sleep(0.002)

def display_string(text, line=0, col=0):
    line_addr = 0x80 + (0x10 * line)  # 行地址偏移
    addr = line_addr + col  # 列偏移
    send_byte(addr, True)  # 设置 DDRAM 地址
    for char in text:
        send_byte(ord(char), False)  # 写入字符数据

# 初始化 HX711
def setup_hx711():
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(reference_unit)
    hx.reset()
    hx.tare()

def read_smoothed_weight():
    """读取单次平滑后的重量数据"""
    samples.clear()  # 清空之前的读数
    valid_samples = []  # 存储有效的读数
    max_attempts = 15  # 最大测量次数
    threshold = 0.2  # 偏差阈值（20%）

    for _ in range(max_attempts):  # 尝试多次读取
        raw = hx.get_weight()
        if 0 <= raw <= 10000:  # 过滤掉负值和超出合理范围的读数（假设最大值为10000）
            valid_samples.append(raw)
        if len(valid_samples) >= 10:  # 如果已收集到足够的有效数据，停止测量
            break
        time.sleep(0.1)  # 增加一点延迟，避免连续读取干扰

    if len(valid_samples) < 5:  # 如果有效数据不足，返回0
        print("未能获取足够的有效重量数据")
        return 0

    # 删除偏差较大的值
    mean = sum(valid_samples) / len(valid_samples)
    filtered_samples = [x for x in valid_samples if abs(x - mean) / mean <= threshold]

    if not filtered_samples:  # 如果过滤后没有数据，返回0
        print("所有数据偏差过大，未能获取有效的重量数据")
        return 0

    # 返回过滤后数据的平均值
    return sum(filtered_samples) / len(filtered_samples)

def capture_image(image_path):
    """拍摄图片并保存到指定路径"""
    for _ in range(5):  # 清空摄像头缓存
        camera.read()

    ret, frame = camera.read()
    if ret:
        cv2.imwrite(image_path, frame)
        print(f"Image saved to {image_path}")
    else:
        print("Failed to capture image from the camera")

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/download":
            # Image path
            image_path = "captured_image.jpg"
            capture_image(image_path)

            # Check if the image exists
            if os.path.exists(image_path):
                self.send_response(200)
                self.send_header('Content-Type', 'application/octet-stream')
                self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(image_path)}"')
                self.end_headers()

                # Read and send the image
                with open(image_path, "rb") as file:
                    self.wfile.write(file.read())
                print("Image sent")
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Image not found")
        elif self.path == "/upload":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')  # 设置编码为 UTF-8
            self.end_headers()
            html_form = """
            <html>
                <body>
                    <h1>上传图片</h1>
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <input type="file" name="file" accept="image/*">
                        <input type="submit" value="上传">
                    </form>
                </body>
            </html>
            """
            self.wfile.write(html_form.encode("utf-8"))  # 将字符串编码为 UTF-8
        elif self.path == "/capture":
            # Handle the capture request
            image_path = "captured_image.jpg"
            capture_image(image_path)

            # Check if the image exists
            if os.path.exists(image_path):
                self.send_response(200)
                self.send_header('Content-Type', 'application/octet-stream')
                self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(image_path)}"')
                self.end_headers()

                # Read and send the image
                with open(image_path, "rb") as file:
                    self.wfile.write(file.read())
                print("Image captured and sent")
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Failed to capture image")
        elif self.path == "/measure":
            # 从机请求测量质量
            current_weight = read_smoothed_weight()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = f'{{"weight": {current_weight:.2f}}}'
            self.wfile.write(response.encode("utf-8"))
        # 主页面显示当前重量和操作链接
        current_weight = read_smoothed_weight()
        display_string(f"Weight: {current_weight:.2f}g", 0, 0)  # 显示到屏幕
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        html = f"""
        <html>
            <head>
                <title>动态刷新质量</title>
                <script>
                    function refreshWeight() {{
                        fetch('/', {{ method: 'POST', body: 'action=refresh' }})
                            .then(response => response.json())
                            .then(data => {{
                                document.getElementById('weight').innerText = data.weight.toFixed(2) + " g";
                            }})
                            .catch(error => console.error('Error:', error));
                    }}
                </script>
            </head>
            <body>
                <h1>当前重量: <span id="weight">{current_weight:.2f} g</span></h1>
                <form onsubmit="event.preventDefault(); setReference();">
                    <label for="reference">校准参数:</label>
                    <input type="number" id="reference" name="reference" step="1" required>
                    <button type="submit">设置校准参数</button>
                </form>
                <button onclick="refreshWeight()">刷新当前质量</button>
                <p><a href="/capture">拍摄图片</a></p>
                <p><a href="/download">下载图片</a></p>
                <p><a href="/upload">上传图片</a></p>
                <script>
                    function setReference() {{
                        const reference = document.getElementById('reference').value;
                        fetch('/', {{
                            method: 'POST',
                            headers: {{ 'Content-Type': 'application/x-www-form-urlencoded' }},
                            body: `action=set_reference&reference=${{reference}}`
                        }})
                        .then(response => response.json())
                        .then(data => {{
                            document.getElementById('weight').innerText = data.weight.toFixed(2) + " g";
                            alert("校准参数已更新为: " + reference);
                        }})
                        .catch(error => console.error('Error:', error));
                    }}
                </script>
            </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        # 处理 POST 请求
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        params = dict(x.split("=") for x in post_data.split("&"))

        if "action" in params:
            if params["action"] == "refresh":
                # 刷新当前质量
                current_weight = read_smoothed_weight()
                display_string(f"Weight: {current_weight:.2f}g", 0, 0)  # 显示到屏幕
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = f'{{"weight": {current_weight:.2f}}}'
                self.wfile.write(response.encode("utf-8"))

            elif params["action"] == "set_reference" and "reference" in params:
                # 设置校准参数
                global reference_unit
                reference_unit = int(params["reference"])
                setup_hx711()  # 重新初始化 HX711
                print(f"校准参数已更新为: {reference_unit}")
                current_weight = read_smoothed_weight()
                display_string(f"Weight: {current_weight:.2f}g", 0, 0)  # 显示到屏幕
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = f'{{"weight": {current_weight:.2f}}}'
                self.wfile.write(response.encode("utf-8"))

def run():
    """启动 HTTP 服务器"""
    setup_hx711()
    init_lcd()
    host_name = "0.0.0.0"
    port = 8080
    server_address = (host_name, port)
    httpd = HTTPServer(server_address, CustomHandler)

    def shutdown_server(signal, frame):
        """优雅地关闭服务器"""
        print("\nShutting down server...")
        httpd.server_close()
        camera.release()
        GPIO.cleanup()
        pi.stop()
        print("Server stopped")
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_server)

    print(f"HTTP server started, visit http://<local_ip>:{port}/")
    httpd.serve_forever()

if __name__ == '__main__':
    run()