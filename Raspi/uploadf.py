import requests
import os
import logging
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 树莓派配置
RASPBERRY_PI_IP = '127.0.0.1'  # 替换为您的树莓派IP地址
SERVER_PORT = 5000
DEFAULT_IMAGE_DIR = ''  # 树莓派上的默认图片目录

def upload_image(image_path):
    """
    上传图片到服务器
    
    Args:
        image_path: 图片文件的路径
    Returns:
        响应文本和状态码
    """
    try:
        # 确保图片路径是绝对路径
        image_path = os.path.abspath(image_path)
        
        # 检查文件是否存在
        if not os.path.exists(image_path):
            logger.error(f"图片文件不存在: {image_path}")
            return "图片文件不存在", 404
            
        # 服务器URL
        url = f'http://{RASPBERRY_PI_IP}:{SERVER_PORT}/upload'
        logger.info(f"正在上传图片到服务器: {url}")
        
        # 打开图片文件
        with open(image_path, 'rb') as f:
            # 准备文件数据
            files = {'file': f}
            
            # 发送POST请求
            response = requests.post(url, files=files, timeout=30)  # 添加超时设置
            
            logger.info(f"上传完成，状态码: {response.status_code}")
            return response.text, response.status_code
            
    except FileNotFoundError:
        logger.error(f"找不到图片文件: {image_path}")
        return "图片文件不存在", 404
    except requests.exceptions.ConnectionError:
        logger.error("无法连接到服务器，请检查网络连接和服务器状态")
        return "无法连接到服务器", 503
    except requests.exceptions.Timeout:
        logger.error("上传超时，请检查网络连接")
        return "上传超时", 504
    except Exception as e:
        logger.error(f"上传失败: {str(e)}")
        return f"上传失败: {str(e)}", 500

if __name__ == "__main__":
    # 创建默认图片目录（如果不存在）
    Path(DEFAULT_IMAGE_DIR).mkdir(parents=True, exist_ok=True)
    
    # 测试上传
    image_path = os.path.join(DEFAULT_IMAGE_DIR, "temp.jpg")  # 使用树莓派上的默认路径
    logger.info(f"开始上传图片: {image_path}")
    result, status_code = upload_image(image_path)
    print(f"状态码: {status_code}")
    print(f"响应: {result}")
