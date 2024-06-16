import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM模式
GPIO.setmode(GPIO.BCM)

# 定义要使用的GPIO引脚
led_pin = 18
button_pin = 23

# 设置GPIO引脚为输出模式
GPIO.setup(led_pin, GPIO.OUT)

# 设置GPIO引脚为输入模式，并上拉
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 控制LED灯的状态
def toggle_led():
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin, GPIO.LOW)

# 检测按钮的状态，并控制LED灯
try:
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            toggle_led()
            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()