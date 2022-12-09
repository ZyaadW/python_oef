import gpiozero as io #importeer de 'io' modulo
from gpiozero import LED #importeer de 'led' modulo

knop1 = io.Button(17,pull_up=0) #declareer io-pin 3 als button
knop2 = io.Button(4,pull_up=0) #declareer io-pin 4 als button
led1 = LED(14) #declareer io pin 14 als led1
led2 = LED(15) #declareer io pin 15 als led2
led3 = LED(18) #declareer io pin 18 als led3


while True: # wanneer waar
    if (knop1.value and knop2.value == 1): # als knopstatussen 1 en 2 hoog zijn
        led1.off() #led1 uit
        led2.on() #led2 aan
        led3.on() #led3 aan
    else:
        led1.off() #led1 uit
        led2.off() #led2 uit
        led3.off() #led3 uit   

    if (knop1.value == 1 and knop2.value == 0): # als de knopstatus1 hoog is en knopstatus 2 laag
        led1.on() #led1 aan
        led2.on() #led2 aan
        led3.off() #led3 uit

    if (knop2.value == 1) and knop1.value == 0: # als de knopstatus2 hoog is en knopstatus 1 laag
        led1.on() #led1 aan
        led3.on() #led3 aan 
        led2.off() #led2 uit    
          