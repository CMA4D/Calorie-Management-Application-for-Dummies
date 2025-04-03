import cv2
import matplotlib.pyplot as plt

def capture_photo():
    # 使用V4L2驱动避免警告
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    
    # 设置合适的分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        # 保存原始图片
        cv2.imwrite('capture.jpg', frame)
        
        # 转换为RGB并显示
        plt.figure(figsize=(10, 6))
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.title("树莓派拍摄的照片")
        plt.axis('off')
        plt.show()
        return True
    return False

if capture_photo():
    print("拍照成功！")
else:
    print("拍照失败，请检查摄像头连接")