import pigpio
import time

# ��ʼ�� pigpio
pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("pigpio")

# ���Ŷ���
RS = 17       # RS (����/ָ��ѡ��)
E = 18        # E (ʹ���ź�)
PSB = 21
VO = 26
DATA_PINS = [22, 23, 24, 25]  # DB4-DB7

# ��ʼ�� GPIO
pi.set_mode(RS, pigpio.OUTPUT)
pi.set_mode(E, pigpio.OUTPUT)
pi.set_mode(PSB, pigpio.OUTPUT)
pi.set_mode(VO, pigpio.OUTPUT)
for pin in DATA_PINS:
    pi.set_mode(pin, pigpio.OUTPUT)
pi.write(PSB,1)

# ���� 4-bit ����

def send_nibble(data, is_command=True):
    pi.write(RS, 0 if is_command else 1)  # RS=0:����, RS=1:����
    for i in range(4):
        pi.write(DATA_PINS[i], (data >> i) & 1)  # д��� 4 λ
    pi.write(E, 1)  # ʹ������
    time.sleep(0.001)
    pi.write(E, 0)
    time.sleep(0.001)

# ���������ֽڣ������η��ͣ�
def send_byte(data, is_command=True):
    send_nibble(data >> 4, is_command)  # �ȷ��͸� 4 λ
    send_nibble(data & 0x0F, is_command)  # �ٷ��͵� 4 λ

# ��ʼ�� LCD
def init_lcd():
    time.sleep(0.05)
    send_nibble(0x03)  # ��ʼ������
    time.sleep(0.005)
    send_nibble(0x03)
    time.sleep(0.001)
    send_nibble(0x03)
    send_nibble(0x02)  # �л��� 4-bit ģʽ
    send_byte(0x28)    # 2����ʾ, 4-bit ����
    send_byte(0x0C)    # ��ʾ�����޹��
    send_byte(0x01)    # ����
    time.sleep(0.002)

# ��ʾ�ַ���
def display_string(text, line=0, col=0):
    # �е�ַƫ�ƣ���һ�� 0x80���ڶ��� 0x90
    line_addr = 0x80 + (0x10 * line)  
    # ��ƫ�ƣ�ÿ�����16�ַ���
    addr = line_addr + col  
    send_byte(addr, True)  # ����DDRAM��ַ
    for char in text:
        send_byte(ord(char), False)  # д���ַ�����
import time

def display_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        display_string(current_time, 1, 0)  # ��һ����ʾʱ��
        time.sleep(1)

# ������
try:
    init_lcd()
    display_string("Hello", 0, 0)   # ��һ�п�ͷ
    display_string("World", 1, 5)   # �ڶ��е�6��
    display_time()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pi.stop()