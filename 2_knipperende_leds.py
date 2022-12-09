from gpiozero import LED
from time import sleep

varLed1 = LED(18) # variabele led is gelijk aan gpio-pin 18
varLed2 = LED(23) # variabele led is gelijk aan gpio-pin 23

while True: #als waar 
    varLed1.on() #led1 aan
    sleep(1) #wacht 1s
    varLed1.off()#led1 uit
    varLed2.on() #led2 aan
    sleep(1) #wacht 1s
    varLed2.off() #led2 aan
    