from gpiozero import LED # van gpiozero importeer led
from time import sleep # van tijd importeer sleep
import spidev # importeer de nodige modules
from gpiozero import Servo # van gpiozero importeer led

knop = io.Button(17)

varLedG = LED(18) # variabele led is gelijk aan gpio-pin 18
varLedB = LED(23) # variabele led is gelijk aan gpio-pin 23
varLedR = LED(25) # variabele led is gelijk aan gpio-pin 25
delay = 0.3 #variabeleis gelijk aan 300ms

gemid_temp = 0 # gem temp is 0

spi = spidev.SpiDev() #steek de module in de variabele
spi.open(0,0) # op deze positie open spi
spi.max_speed_hz=1000000 # max Hz is gelijk aan 

def readSPI(channel): 

    adc = spi.xfer2([1, (8+channel) <<4,1]) # kies kanaal1 en schuif 4 op naar links (bits)
    data = ((adc[2] & 3) <<8) +adc[2] # formule voor de data te berekenen/verwerken
    spanning = (data /1024.0) * 3.3 # formule om met de data de spanninbgswaarde te berekenen
    temperature = ((spanning - 0.5) * 100.0) # formule voor de temperatuur
    return(temperature) # geef de temp terug

channel = 1 # variabele is gelijk aan 1
try: # probeer
    while True: # als waar 
        
        waarde1 = readSPI(channel) # lees de waarde naar variabele
        waarde2 = readSPI(channel) # lees de waarde naar variabele

        gemid_temp = (waarde1+waarde2)/2 #gemiddelde temp isgelijk aan de optelling van de waardes en deel door elkaar (aanta)
        print("temperatuur: {}, degC".format(round(gemid_temp, 1))) # print gemid temp met 1 getal afgerond
    

        sleep(2) # wacht 2s
except KeyboardInterrupt: # behalve bij deze onderbreking
    spi.close() # sluit spi

try: # probeer
    while True: # wanneer waar
        if (knop.value == 0): # als er gedrukt is
            servo.max() # maak de deur volledig open
        elif (gemid_temp < 2): # als de temp lager is dan 2
            servo.min() # sluit de deur volledig
        elif (gemid_temp > 2): # als temp hoger is dan
            varLedB.on() #blauw aan
            varLedG.on() #groen aan
            varLedR.on() #rood aan
        else: # anders
            varLedB.off() #blauw uit
            varLedG.off() #groen uit
            varLedR.off() #rood uit

except KeyboardInterrupt:
    print("programma is gestopt") # print dat programma is gestopt
    while True: #als waar 

        if (gemid_temp <= 0): # anders als de gemiddelde tempe kleiner is of gelijk aan 0
            varLedB.on() #blauw aan
            varLedG.off() #groen uit
            varLedR.off() #rood uit
            sleep(delay) # wacht volgens variabele
            varLedB.off() # blauw uit
        elif (gemid_temp < 2): # anders als de gemiddelde temp kleiner is dan 2    
            varLedB.on() #blauw aan
            varLedG.off() #groen aan
            varLedR.off() #rood aan
        elif (gemid_temp < 4): # anders als de gemiddelde temp kleiner is  dan 4   
            varLedB.off() #blauw uit
            varLedG.on() #groen aan
            varLedR.off() #rood uit
        elif (gemid_temp < 6): # anders als de gemiddelde temp kleiner is dan 6
            varLedB.off() #blauw uit
            varLedG.on() #groen aan
            varLedR.on() #rood uit
        elif (gemid_temp < 8): #anders als de gemiddelde temp kleiner is dan 8 
            varLedB.off() #blauw uit
            varLedG.off() #groen uit
            varLedR.on() #rood aan
        elif (gemid_temp < 10): # anders als de gemiddelde temp kleiner is  dan 10 
            varLedB.off() #blauw uit
            varLedG.off() #groen uit
            varLedR.on() #rood aan
            sleep(delay) #wacht 300ms
            varLedR.off() #rood uit
        else: # anders
            varLedB.off() #blauw uit
            varLedG.off() #groen uit
            varLedR.off() #rood uit