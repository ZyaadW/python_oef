from gpiozero import Servo # van gpiozero importeer Servo
servo = Servo(17, min_pulse_width=min,max_pulse_width=max) # servo op pin 17 met een max en min puls gelijk aan max en min

try:# probeer dit
    while True: # wanneer waar
        waarde = int(input("Wat is de hoek? ")) # wat je intypt wordt omgezet naar een int getal en benoemd door deze variabele
        graden = (waarde/90)-1 # formule voor hoek graden naar variabele omzetten 
        if (graden < 0) or (graden > 180): # als de hoek graden kleiner is dan 0 OF groter dan 180
            print("Kies een cijfer tussen 0 en 180") # print dit
        else: # anders
            servo.value = graden # geef servo waarde om te bewegen
except KeyboardInterrupt: # behalve bij een toetsenbord onderbrekening (control + c)
    print("Programma is gestopt.") # print dit
except ValueError: # behalve bij een waarde fout
    print("Fout gekozen datatype") # print dit                    