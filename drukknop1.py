import gpiozero as io
from gpiozero import LED
from time import sleep

knop = io.Button(4,pull_up=0)
led = LED(18)

laatsteKnopstatus = 0
knopTeller = 0
while True:
    knopstatus = knop.value
    if knopstatus != laatsteKnopstatus:
        if knopstatus == True:
            knopTeller+=1    
    laatsteKnopstatus = knopstatus
    if knopTeller % 2 == 0:
        led.on()
    else:
        led.off()    