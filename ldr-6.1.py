from gpiozero import LightSensor

varSensor = LightSensor(18)

while True: 
    print(varSensor.value)
    varSensor.wait_for_light()
    print("Er is licht")
    varSensor.wait_for_dark()
    print("Het is donker")