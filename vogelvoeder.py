from gpiozero import Servo,MotionSensor,DistanceSensor
from time import sleep

sensor = DistanceSensor(18,24)
pir = MotionSensor(23)
teller = 0
myGPIO=17
servo = Servo(myGPIO)
huidige_status = False
vorige_status = False

def teller1(teller):
    teller+=1
    print(f"Het aantal vogels is: {teller}")
    return teller

def servo1():
    servo.min()
    print('dicht')
    sleep(5)
    servo.max()
    print('open')
    sleep(2)

def distance(afstand):
    afstand = sensor.distance * 30
    print(f"{afstand} cm")
    return afstand



while True:
    vorige_status = huidige_status
    huidige_status = pir.motion_detected
    print(pir.motion_detected)
    if vorige_status == False and huidige_status == True:
        teller = teller1(teller)
    sleep(0.1)

   
    
    

