#Program to get Lisa18's data and interpreit
import LIS3DH as Lisa
from time import sleep

Lisa18 = Lisa.LIS3DH(0x18, -1)
Lisa18.setRange(Lisa.LIS3DH.RANGE_2G)

#Loop stuff
xList = []
yList = []
zList = []
i = 0

def avg(dataList):
    temp = 0
    for data in dataList:
        temp += data
    temp = temp / dataList.length()
    return temp

print ("Starting stream")
while i < 100:
    
    x = Lisa18.getX()
    y = Lisa18.getY()
    z = Lisa18.getZ()

#raw values
    print(("\rX: %.6f\tY: %.6f\tZ: %.6f") % (x,y,z))
    
    xList.append(x)
    yList.append(y)
    zList.append(z)
    #Is this the hz we want??
    i += 1
    sleep(0.1)

print(("\r\nAVERAGES: X: %.6f\tY: %.6f\tZ: %.6f") % ( avg(xList) , avg(yList) , avg(zList) ))
