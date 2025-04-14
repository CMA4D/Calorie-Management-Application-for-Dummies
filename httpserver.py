from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import cv2
import signal
import sys

# Read from the camera, 0 represents the built-in camera, 1, 2, 3... can call other cameras
camera = cv2.VideoCapture(0)

def capture_image(image_path):
    """Capture an image from the camera and save it to the specified path"""
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
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')  # 设置编码为 UTF-8
            self.end_headers()
            # 修改为中文提示语并编码为 UTF-8
            self.wfile.write("<html><body><h1>欢迎使用简易的下载、上传和拍摄服务</h1></body></html>".encode("utf-8"))

    def do_POST(self):
        """Handle POST requests for image upload"""
        if self.path == "/upload":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            # Extract the uploaded file content
            boundary = self.headers['Content-Type'].split("boundary=")[1]
            parts = post_data.split(boundary.encode())
            for part in parts:
                if b"Content-Disposition" in part and b"filename=" in part:
                    filename = part.split(b"filename=")[1].split(b"\r\n")[0].strip(b'"').decode()
                    file_data = part.split(b"\r\n\r\n")[1].rsplit(b"\r\n", 1)[0]

                    # Save the uploaded file
                    with open(filename, "wb") as f:
                        f.write(file_data)
                    print(f"Uploaded file saved as {filename}")

                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"File uploaded successfully")
                    return

            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Failed to upload file")

def run():
    """Start the HTTP server"""
    # Get the local IP address
    host_name = "0.0.0.0"  # Listen on all available network interfaces
    port = 8080
    server_address = (host_name, port)
    httpd = HTTPServer(server_address, CustomHandler)

    def shutdown_server(signal, frame):
        """Gracefully stop the server and release resources"""
        print("\nShutting down server...")
        httpd.server_close()  # 关闭 HTTP 服务器
        camera.release()  # 释放摄像头资源
        print("Server stopped")
        sys.exit(0)

    # 捕获终止信号（如 Ctrl+C）
    signal.signal(signal.SIGINT, shutdown_server)

    print(f"HTTP server started, visit http://<local_ip>:{port}/download to download the image, /upload to upload an image, or /capture to capture and download an image")
    httpd.serve_forever()

if __name__ == '__main__':
    run()