import adafruit_dht,time,board # importeer de nodige modules
import gpiozero as GPIO # importeer deze module en benoem als variabele
from gpiozero import LED # van de gpiozero-module importeer je de LED-module


dhtDevice = adafruit_dht.DHT11(board.D12) # de pin D12 is voor de dht11 sensor en stel je gelijk aan de variabele
led1 = LED(14) # variabele led1 als gpio-pin 14
led2 = LED(15) # variabele led2 als gpio-pin 15
led3 = LED(18) # variabele led3 als gpio-pin 18
led4 = LED(23) # variabele led4 als gpio-pin 23
led5 = LED(24) # variabele led5 als gpio-pin 24

GPIO.setup(21,GPIO.OUT) # zet GPIO21 als een uitgang
ventilator = GPIO.PWM(21, 100) #deze variable wordt toegekend aan GPIO21 en dat die op een frequentie van 100Hz werkt
ventilator.start(100) # de motor werkt met een frequentie van 100Hz
teller = 0 # variabele is gelijk aan nul

while True: # wanneer waar
    try: # probeer
        time(5) #wacht 5 seconden
        teller+=1 # doe teller + 1
        temperature_c = dhtDevice.temperature # haal de temp op en stop in variabele
        humidity = dhtDevice.humidity # haal de vochtigheid op en stop in variabele
        if humidity >= 20: # als de vochtigheid groter dan of gelijk is dan 20%
            ventilator.ChangeDutyCycle(20) # laat de ventilator op 20% draaien
            print("De snelheid vqn de ventilator is op 20%\n") # print deze tekst
        elif humidity > 40: # als de vochtigheid groter dan 40% is
            ventilator.ChangeDutyCycle(25) # laat de ventilator op 25% draaien
            print("De snelheid vqn de ventilator is op 25%\n") # print deze tekst 
        elif humidity > 60: # als de vochtigheid groter dan 60% is
            ventilator.ChangeDutyCycle(50) # laat de ventilator op 50% draaien
            print("De snelheid vqn de ventilator is op 50%\n") # print deze tekst
        elif humidity > 80: # als de vochtigheid groter dan 80% is
            ventilator.ChangeDutyCycle(75) # laat de ventilator op 75% draaien
            print("De snelheid vqn de ventilator is op 75%\n") # print deze tekst
        else: # anders doe dit
            ventilator.ChangeDutyCycle(0)  # laat de ventilator op 0% draaien 
            print("De snelheid vqn de ventilator is op 0%\n") # print deze tekst

        if temperature_c >= 15: # als de temp groter dan of gelijk dan 15 graden
            led1.on() # led1 is aan
            led2.off() # led2 is uit
            led3.off() # led3 is uit
            led4.off() # led4 is uit
            led5.off() # led5 is uit
            print("led1 is aan") # print welke led(s) gestuurd word(en)
        elif temperature_c > 18: # als de temp groter dan 18 graden is
            led1.on() # led1 is aan 
            led2.on() # led2 is aan
            led3.off() # led3 is uit
            led4.off()  # led4 is uit 
            led5.off()  # led5 is uit
            print("led1 led2\n") # print welke led(s) gestuurd word(en)
        elif temperature_c > 21: # als de temp groter dan 21 graden is
            led1.on() # led1 is aan
            led2.on() # led2 is aan
            led3.on() # led3 is aan
            led4.off()  # led4 is uit
            led5.off()  # led5 is uit
            print("led1 led2\n led3\n") # print welke led(s) gestuurd word(en)   
        elif temperature_c > 24: # als de temp groter dan 24 graden is
            led1.on() # led1 is aan
            led2.on() # led2 is aan
            led3.on() # led3 is aan
            led4.on() # led4 is aan
            led5.off() # led5 is uit
            print("led1 led2\n led3\n led4\n") # print welke led(s) gestuurd word(en)
        elif temperature_c > 27: # als de temp groter dan 27 graden is
            led1.on() # led1 is aan
            led2.on() # led2 is aan
            led3.on() # led3 is aan
            led4.on() # led4 is aan
            led5.on() # led5 is aan
            print("led1 led2\n led3\n led4\n led5\n") # print welke led(s) gestuurd word(en)
        else: # anders doe dit
            led1.off() # led1 is uit
            led2.off() # led2 is uit
            led3.off() # led3 is uit
            led4.off() # led4 is uit
            led5.off() # led5 is uit
            print("alles uit") # print dat alle ledjes uit zijn
        if teller == 12: # als de teller gelijk is aan 12
            humidity_gemid = humidity/12 # doe de vochtigheid delen door het aantal keren dat er gemeten is, en dat is dus 12 keren en stop in variabele
            temperature_c_gemid = temperature_c_gemid/12 # doe de temp delen door het aantal keren dat er gemeten is, en dat is dus 12 keren en stop in variabele
            print("Temperatuur gemiddelde:  {:.1f} C    Humidity gemiddelde: {}% ".format( #print de gemiddelde temp en vochtigheid met de benodigde symbolen en percentage
                 temperature_c_gemid, humidity_gemid)) # deze variabele worden gebruikt bij het uitprinten
            teller = 0 # teller is gelijk aan 0 
    except RuntimeError as error: # behalve als er een fout tijdens het doorlopen van je code optreedt, en benoem dit als de variabele
        print(error.args[0]) # print dit
        time.sleep(2) # wacht 2 seconden
        continue # ga door
    except KeyboardInterrupt: # behalve als er een onderbreking komt van het toetsenbord (control + c)
        print("programma is onderbroken") # print deze tekst
    except Exception as error: # behalve als er een onbekende fout isn en benoem dit als variabele
        dhtDevice.exit() # ga uit de sensor (dht11)
        raise error # stuur een foutmelding
