import gpiozero as io
from gpiozero import LED
from time import sleep

knop = io.Button(4,pull_up=0)
led = LED(10)

while True:
    sleep(0.1)
    if knop.value:
        print("Button is ingedrukt")
        led.on()
    else:
        print("Button is in rust ")    
        led.off()