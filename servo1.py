from gpiozero import Servo
from time import sleep
servo = Servo(17, min_pulse_width=min,max_pulse_width=max)

try:
    while True:
        waarde = int(input("Wat is de hoek? "))
        graden = (waarde/90)-1
        if (graden < 0) or (graden > 180):
            print("Kies een cijfer tussen 0 en 180")
        else:
            servo.value = graden
except KeyboardInterrupt:
    print("Programma is gestopt.")
except ValueError:
    print("Fout gekozen datatype") # print dit                    