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
    


Lisa18 = initLisa(0x18, -1)
Lisa19 = initLisa(0x19, -0)

print ("Starting stream")
while True:
       
    x = Lisa18.getX()
    y = Lisa18.getY()
    z = Lisa18.getZ()

#raw values
    print(("\rX: %.6f\tY: %.6f\tZ: %.6f") % (x,y,z))
    sleep(0.1)
