import spidev,time # importeer beide modules


spi = spidev.SpiDev() #steek de module in de variabele
spi.open(0,0) # op deze positie open spi
spi.max_speed_hz=1000000 # max Hz is gelijk aan 

def readSPI(channel): #
    adc = spi.xfer2([1, (8+channel) <<4,0])
    x = ((adc[1] & 3) <<8) +adc[2]
    y = 3000-13*x
    return(y)

channelLDR = 0 # variabele is gelijk aan 0

while True: # als waar 
    
    licht_intensiteit = readSPI(channelLDR) # lees de waarde naar variabele
    if licht_intensiteit < 0: # als de waarde kleiner is dan 0
        print(0) # print 0
    else: # anders
        print(licht_intensiteit)    #print de licht-waarde


    time.sleep(5) # wacht 5s
