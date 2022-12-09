from gpiozero import LED
from time import sleep

varLedG = LED(18) # variabele led is gelijk aan gpio-pin 18
varLedB = LED(23) # variabele led is gelijk aan gpio-pin 23
varLedR = LED(25) # variabele led is gelijk aan gpio-pin 25
delay = 0.3 #variabeleis gelijk aan 300ms

while True: #als waar 
   varLedB.off() #blauw uit
   varLedG.off() #groen uit
   varLedR.off() #rood uit
   sleep(delay) #wacht 300ms
   varLedB.on() #blauw aan
   varLedG.on() #groen aan
   varLedR.on() #rood aan
   sleep(delay) #wacht 300ms
   varLedB.on() #blauw aan
   varLedG.off() #groen uit
   varLedR.off() #rood uit
   sleep(delay) #wacht 300ms
   varLedB.off() #blauw uit
   varLedG.on() #groen aan
   varLedR.off() #rood uit
   sleep(delay) #wacht 300ms
   varLedB.off() #blauw uit
   varLedG.off() #groen uit
   varLedR.on() #rood aan
   sleep(delay) #wacht 300ms
   varLedB.on() #blauw aan
   varLedG.on() #groen aan
   varLedR.off() #rood uit
   sleep(delay)#wacht 300ms
   varLedB.off() #blauw uit
   varLedG.on() #groen aan
   varLedR.on() #rood aan
   sleep(delay) #wacht 300ms
   varLedB.on() #blauw aan
   varLedG.off() #groen uit
   varLedR.on() #rood aan
   sleep(delay) #wacht 300ms

