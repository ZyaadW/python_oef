import RPi.GPIO as GPIO  #importeer de rpi module
import time # sleep-module
from w1thermsensor import W1ThermSensor #van deze module importeer dit

GPIO.setmode(GPIO.BCM) # kies BCM of het bord 
GPIO.setwarnings(False) # zet de waarschuwingen uit (false)

GPIO.setup(21, GPIO.OUT) # zet GPIO21 als een uitgang
p = GPIO.PWM(21, 100) #deze variable wordt toegekend aan GPIO21 en dat die op een frequentie van 100Hz werkt
p.start(100) # de motor werkt met een frequentie van 100Hz
sensor = W1ThermSensor() # variabele is gelijk aan module         

while True: # als waar
    try: #probeer dit
        temp = sensor.get_temperature # stop de temp in de variabele
        print("De temperatuur in graden Celcius is nu", temp) # print dit met waarde op einde
        time.sleep(1) # wacht 1s

        if temp <= 20: # als de temperatuur kleiner dan of gelijk is aan 20 graden
            p.ChangeDutyCycle(0) # verander de snelheid naar 0%
        elif temp > 20 and temp < 30: # anders-als de temp groter is dan 20 graden en kleiner dan 30 graden
            y1 = 50 + 5*(temp-20) # formule (lineaire) voor temperatuur
            p.ChangeDutyCycle(y1) # verander de snelheid naar de waarde van de variabele
        else: # anders
            p.ChangeDutyCycle(100) # verander de snelheid naar 100%
    except KeyboardInterrupt: # behalve bij een keyboardInterrupt
        GPIO.cleanup # reset alle GPIO pinnen
        p.ChangeDutyCycle(0) # verander de snelheid naar 0%