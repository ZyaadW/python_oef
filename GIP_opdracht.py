from gpiozero import DistanceSensor
import time
from hx711 import HX711
from tkinter import *

sensor = DistanceSensor(18,24)
teller = 0

def teller1(teller):
    teller+=1
    print(f"Het aantal vogels is: {teller}")
    return teller

def distance(afstand):
    afstand = sensor.distance * 30
    print(f"{afstand} cm")
    return afstand

brocheDT = 5   # DT van HX711 aangesloten op GPIO5
brocheSCK = 6  # SCK van HX711 aangesloten op GPIO6

hx = HX711(brocheDT, brocheSCK) 

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(382.6) #calibration: le nombre dépend de votre balance
hx.reset()
hx.tare()

venster = Tk()    # création d'une fenêtre
venster.geometry("300x100+150+150")  # positie voor venster
venster.title("Evenwicht")  # titel voor vensterpje

label = Label(venster, text=" ")  # ligne vide
label.pack()

label1 = Label(venster, fg="red", text="Gemeten massa:")
label1.pack()

label = Label(venster, text=" ")  # ligne vide
label.pack()

label2 = Label(venster, text=" ")  # totale gemeten waarde
label2.pack()

def gewicht():
    label2['text'] = "{0:0.1f}".format(hx.get_weight(5)) + " gram"
    venster.after(1000, gewicht) # wacht 1s

venster.after(1000, gewicht)

venster.mainloop()