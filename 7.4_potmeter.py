import spidev
import time
import RPi.GPIO as GPIO 

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
p = GPIO.PWM(18, 100)
p.start(100)

def readSPI (channel):
    adc = spi.xfer2 ([1, (8+channel) <<4,0])
    data = ((adc[1] & 3) <<8) +adc[2]
    return(data)

channelPot = 0
try:
    while True: 
        waarde_pot = readSPI (channelPot)
        print (waarde_pot)
        teller = int((waarde_pot/1023)*100)
        print(teller)
        time.sleep(0.8)
        p.ChangeDutyCycle(teller)
except KeyboardInterrupt:
    p.ChangeDutyCycle(0)        

