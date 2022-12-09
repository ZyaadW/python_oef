from gpiozero import LED
from time import sleep

varLed1 = LED(18) # variabele led is gelijk aan gpio-pin 18
varLed2 = LED(23) # variabele led is gelijk aan gpio-pin 23
varLed3 = LED(25) # variabele led is gelijk aan gpio-pin 25
varled4 = LED(8)  # variabele led is gelijk aan gpio-pin 8

while True: #als waar 
    varLed1.on() #led1 aan
    sleep(0.4) #wacht 1s
    varLed1.off()#led1 uit
    varLed2.on() #led2 aan
    sleep(0.4) #wacht 1s
    varLed2.off() #led2 aan
    varLed3.on() #led3 aan
    sleep(0.4) #wacht 1s
    varLed3.off() #led3 uit
    varled4.on() #led4 aan
    sleep(0.4) #wacht 1s
    varled4.off() #led4 uit
    varLed3.on() #led3 aan
    sleep(0.4) #wacht 1s
    varLed3.off() #led3 uit
    varLed2.on() #led2 aan
    sleep(0.4) #wacht 1s
    varLed2.off() #led2 uit
