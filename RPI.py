import RPi.GPIO as GPIO
import time as sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


LED = 19
button = 10

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
    try:
        button_state = GPIO.input(button)
        if button_state == GPIO.HIGH:
            GPIO.output(LED, True)
            print("knop ingedrukt")
        else:
            print("niet")
            GPIO.output(LED, GPIO.LOW)

    except:
        GPIO.cleanup()


