import LIS3DH as Lisa
from time import sleep

Lisa18 = Lisa.LIS3DH(0x18, -1)
Lisa18.setRange(Lisa.LIS3DH.RANGE_2G)

print ("Starting stream")
while True:
       
    x = Lisa18.getX()
    y = Lisa18.getY()
    z = Lisa18.getZ()

#raw values
    print(("\rX: %.6f\tY: %.6f\tZ: %.6f") % (x,y,z))
    sleep(0.1)
