from gpiozero import DistanceSensor,LED,Button # importeer de afstand,led en knop vanuit de library gpiozero

sensor = DistanceSensor(18,23) # gpio-pin 18 is v/d trigger en 23 v/d echo en wordt in de vraiabele geplaatst
Led1 = LED(17) # variabele led is gelijk aan gpio-pin 23
Led2 = LED(27) # variabele led is gelijk aan gpio-pin 23
Led3 = LED(13) # variabele led is gelijk aan gpio-pin 23
Led4 = LED(19) # variabele led is gelijk aan gpio-pin 23
Led5 = LED(26) # variabele led is gelijk aan gpio-pin 23-
knop = Button(21) # de knop is gelijk aan gpio-pin 21

while True: # als het waar is
    distance = 0 # de afstand is gelijk aan 0
    if knop.value: # als de knop hoog is
        distance = sensor.distance * 1000 #formule voor afstand in mm naar variabele "distance"
    if distance < 200: # als de afstand kleiner is dan 200mm
        Led1.on() #led1 aan
        Led2.on() #led2 aan
        Led3.on() #led3 aan
        Led4.on() #led4 aan
        Led5.on() #led5 aan
    elif distance < 400: # anders als de afstand kleiner is dan 400mm
        Led1.on() #led1 aan
        Led2.on() #led2 aan
        Led3.on() #led3 aan
        Led4.on() #led4 aan
        Led5.off() #led5 uit
    elif distance < 600: # anders als de afstand kleiner is dan 600mm
        Led1.on() #led1 aan
        Led2.on() #led2 aan
        Led3.on() #led3 aan
        Led4.off() #led4 uit
        Led5.off() #led5 uit
    elif distance < 800: # anders als de afstand kleiner is dan 800mm
        Led1.on() #led1 aan
        Led2.on() #led2 aan
        Led3.off() #led3 uit
        Led4.off() #led4 uit
        Led5.off() #led5 uit
    elif distance < 1000: # anders als de afstand kleiner is dan 1000mm   
        Led1.on() #led1 aan
        Led2.off() #led2 uit
        Led3.off() #led3 uit
        Led4.off() #led4 uit
        Led5.off() #led5 uit
    else: # anders doe dit
        Led1.off() #led1 uit
        Led2.off() #led2 uit
        Led3.off() #led3 uit
        Led4.off() #led4 uit
        Led5.off() #led5 uit

