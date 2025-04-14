import pigpio
import time

# 初始化 pigpio
pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("pigpio")

# 引脚定义
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
pi.write(PSB,1)

# 发送 4-bit 数据

def send_nibble(data, is_command=True):
    pi.write(RS, 0 if is_command else 1)  # RS=0:命令, RS=1:数据
    for i in range(4):
        pi.write(DATA_PINS[i], (data >> i) & 1)  # 写入高 4 位
    pi.write(E, 1)  # 使能脉冲
    time.sleep(0.001)
    pi.write(E, 0)
    time.sleep(0.001)

# 发送完整字节（分两次发送）
def send_byte(data, is_command=True):
    send_nibble(data >> 4, is_command)  # 先发送高 4 位
    send_nibble(data & 0x0F, is_command)  # 再发送低 4 位

# 初始化 LCD
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

# 显示字符串
def display_string(text, line=0, col=0):
    # 行地址偏移：第一行 0x80，第二行 0x90
    line_addr = 0x80 + (0x10 * line)  
    # 列偏移（每行最多16字符）
    addr = line_addr + col  
    send_byte(addr, True)  # 设置DDRAM地址
    for char in text:
        send_byte(ord(char), False)  # 写入字符数据
import time

def display_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        display_string(current_time, 1, 0)  # 第一行显示时间
        time.sleep(1)

# 主程序
try:
    init_lcd()
    display_string("Hello", 0, 0)   # 第一行开头
    display_string("World", 1, 5)   # 第二行第6列
    display_time()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pi.stop()