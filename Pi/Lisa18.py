#Program to get Lisa's data!
import LIS3DH as Lisa
from time import sleep

print("Trying to initialise Lisa18...")
Lisa18 = initLisa(0x18, -1)
Lisa19 = initLisa(0x19, -0)

def initLisa(add, bus):
    try:
        newLisa = Lisa.LIS3DH(add, bus)
        newLisa.setRange(Lisa.LIS3DH.RANGE_2G)
    except IOError:
        print("Failed to initialise Lisa%x" % add)

print ("Starting stream")
while True:
       
    x = Lisa18.getX()
    y = Lisa18.getY()
    z = Lisa18.getZ()

#raw values
    print(("\rX: %.6f\tY: %.6f\tZ: %.6f") % (x,y,z))
    sleep(0.1)
