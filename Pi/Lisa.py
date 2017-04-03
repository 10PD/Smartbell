#Program to get Lisa's data!
import LIS3DH as Lisa
from time import sleep

#Takes memory address (0x18 / 0x19)
#Takes bus (-1 / -0)
def initLisa(add, bus):
    print("Trying to initialise Lisa%x..." % add)
    try:
        newLisa = Lisa.LIS3DH(add, bus)
        newLisa.setRange(Lisa.LIS3DH.RANGE_2G)
        print("Lisa%x initialised!" % add)
        return newLisa
    except IOError:
        print("Failed to initialise Lisa%x" % add)
    
#Tries to pull data from Lisa
def testLisa(Lisa):
    print ("Starting stream")
    while True:
        
        x = Lisa.getX()
        y = Lisa.getY()
        z = Lisa.getZ()

    #raw values
        print(("\rX: %.6f\tY: %.6f\tZ: %.6f") % (x,y,z))
        #Is this the hz we want??
        sleep(0.1)


Lisa18 = initLisa(0x18, -1)
Lisa19 = initLisa(0x19, -0)

testLisa(input("Test Lisa18 or Lisa19?\n"))
