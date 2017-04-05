# Smartbell
Repository making the Dumbell Smart.

Framework.py (py3+):
*Formats data to JSON to be passed to server.

Accelerometer.py (py2.7):
*Filters and interpreits sensor stream.

testMPU6050.py (py ?):
*Example code to read from MPU6050
*Should stream gyro and accel data

Pi/Lisa.py (py2.7):
*Test to read data from Lisa18 / Lisa19
*Lisa19 may never exist! New component on its way!

Pi/Average.py (py2.7):
*Calculates average of 100 Lisa sensor readings

Pi/testLIS3DH.py (py2.7):
*Came with the chip's python library, and the inspiration for many of the programs.
*Don't change me!