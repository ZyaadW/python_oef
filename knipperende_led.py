from gpiozero import LED
from time import sleep

varLed = LED(18) # variabele led is gelijk aan pin 18

while True: #als waar 
    varLed.on() #led aan
    sleep(1) #wacht 1s
    varLed.off()#led uit
    sleep(1) #wacht 1s