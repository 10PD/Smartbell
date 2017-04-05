#Program to get Lisa18's data and interpreit
#AVERAGES (from flat):
xAvg = -0.152029
yAvg = 0.291956
zAvg = 0.960752
import LIS3DH as Lisa
from time import sleep

Lisa18 = Lisa.LIS3DH(0x18, -1)
Lisa18.setRange(Lisa.LIS3DH.RANGE_2G)

print ("Starting stream")
while True:
    
    x = Lisa18.getX()
    y = Lisa18.getY()
    z = Lisa18.getZ()

    x_acc = (x - xAvg)
    y_acc = (y - yAvg)
    z_acc = (z - zAvg)
    
#raw values
    print(("\rX: %.6f\tY: %.6f\tZ: %.6f") % (x_acc,y_acc,z_acc))

    #Is this the hz we want??
    sleep(0.1)
