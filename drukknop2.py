import gpiozero as io #importeer de 'io' modulo
from gpiozero import LED #importeer de 'led' modulo
import time #importeer de 'sleep' modulo

knop1 = io.Button(17,pull_up=0) #declareer io-pin 3 als button
knop2 = io.Button(4,pull_up=0) #declareer io-pin 4 als button
led = LED(18) #declareer pin 18 als variabele led

huidigeTijd = 0 # variabele is gelijk aan 0
vorigeTijd = 0 # variabele is gelijk aan 0
status = 0 # variabele is gelijk aan 0

while True: # wanneer waar
    if ((knop1.value or knop2.value) and status == 0): # als de waarde van EEN van de druknoppen hoog is
        huidigeTijd = time.time() #huidigeTijd is gelijk aan millis
        status = 1 # variabele is gelijk aan 0
        if (knop1.value and knop2.value): # als beide knoppen hoog zijn
            vorigeTijd = time.time() #vorigeTijd is gelijk aan millis
            if ((huidigeTijd - vorigeTijd) <= 0.2): # als het verschil van de huidigeTijd en vorigeTijd groter is dan 200
                led.on() # led aan
        else: # anders
            led.off() # led uit
    else: # anders
        status = 0 # variabele is gelijk aan 0
        