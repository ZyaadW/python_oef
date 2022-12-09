import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
p = GPIO.PWM(21, 100)
p.start(100)

while True:
    try:

        p.ChangeDutyCycle(75)
        time.sleep(3)
        p.ChangeDutyCycle(50)
        time.sleep(3)
        p.ChangeDutyCycle(95)
        time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup    