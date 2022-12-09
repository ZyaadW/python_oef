import spidev,time # importeer beide modules

spi = spidev.SpiDev() #steek de module in de variabele
spi.open(0,0) # op deze positie open spi
spi.max_speed_hz=1000000 # max Hz is gelijk aan 

def readSPI(channel): 

    adc = spi.xfer2([1, (8+channel) <<4,0])
    data = ((adc[1] & 3) <<8) +adc[2]
    spanning = (data /1024.0) * 3.3
    temperature = ((spanning - 0.5) * 100.0)
    return(temperature)

channelLDR = 0 # variabele is gelijk aan 0
try:
    while True: # als waar 
        
        waarde = readSPI(channelLDR) # lees de waarde naar variabele
    

        print("temperatuur: {} degC".format(waarde))
    

        time.sleep(2) # wacht 1s
except KeyboardInterrupt:
    spi.close()
