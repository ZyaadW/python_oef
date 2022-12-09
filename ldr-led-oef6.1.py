from gpiozero import LightSensor
from gpiozero import LED

varSensor = LightSensor(18)
led = LED(15)

while True:
    print(varSensor.value)
 
    varSensor.wait_for_light()
    print("Er is licht")
    led.off()   
    varSensor.wait_for_dark()
    print("Het is donker")
    led.on() 