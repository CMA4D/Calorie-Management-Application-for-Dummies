from hx711 import HX711
import time
import RPi.GPIO as GPIO

# 初始化 HX711
hx = HX711(5, 6)

# 校准参数（需根据实际传感器调整）
reference_unit = 40  # 初始值，后续通过校准确定
from collections import deque

samples = deque(maxlen=10)  # 存储最近10次读数

def read_smoothed_weight():
    raw = hx.get_weight()
    samples.append(raw)
    return sum(samples) / len(samples)

def setup():
    hx.set_reading_format("MSB", "MSB")  # 数据格式（大多数传感器适用）
    hx.set_reference_unit(reference_unit)
    hx.reset()
    hx.tare()  # 去皮（清零初始偏移）

def read_weight():
    try:
        val = hx.get_weight(5)  # 读取5次取平均
        print(f"重量: {val:.2f} g")  # 单位需根据校准调整
        hx.power_down()  # 省电模式
        hx.power_up()
        return val
    except Exception as e:
        print("读取错误:", e)
        return None

# 主程序
if __name__ == "__main__":
    setup()
    try:
        while True:
            weight = read_weight()
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程序终止")