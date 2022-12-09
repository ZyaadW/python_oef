from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(18,23)


while True:
    distance = sensor.distance * 1000
    print("De afstand tot het object is", distance, "mm")
    fp = open("Afstand.txt", "a")
    fp.writelines(f"De afstand is {distance}\n")
    fp.close()
    sleep(1)
    