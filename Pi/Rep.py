#!/usr/bin/python
#Program to give a TRUE to a BCM Pin
#Triggered when system is not moving for time
import smbus
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

gyro_scale = 131.0
accel_scale = 16384.0

address = 0x68  # This is the address value read via the i2cdetect command

def read_all():
    raw_gyro_data = bus.read_i2c_block_data(address, 0x43, 6)
    raw_accel_data = bus.read_i2c_block_data(address, 0x3b, 6)

    gyro_scaled_x = twos_compliment((raw_gyro_data[0] << 8) + raw_gyro_data[1]) / gyro_scale
    gyro_scaled_y = twos_compliment((raw_gyro_data[2] << 8) + raw_gyro_data[3]) / gyro_scale
    gyro_scaled_z = twos_compliment((raw_gyro_data[4] << 8) + raw_gyro_data[5]) / gyro_scale

    accel_scaled_x = twos_compliment((raw_accel_data[0] << 8) + raw_accel_data[1]) / accel_scale
    accel_scaled_y = twos_compliment((raw_accel_data[2] << 8) + raw_accel_data[3]) / accel_scale
    accel_scaled_z = twos_compliment((raw_accel_data[4] << 8) + raw_accel_data[5]) / accel_scale

    return (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z)
    
def twos_compliment(val):
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

#Sets the plane of orientation
def initPlane():
    (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()

    last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

    gyro_offset_x = gyro_scaled_x 
    gyro_offset_y = gyro_scaled_y

    gyro_total_x = (last_x) - gyro_offset_x
    gyro_total_y = (last_y) - gyro_offset_y

    #print ("{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f}").format( time.time() - now, (last_x), gyro_total_x, (last_x), (last_y), gyro_total_y, (last_y))
    return (last_x, last_y, gyro_offset_x, gyro_offset_y, gyro_total_x, gyro_total_y)
    
#(gyro_scaled_x, gyro_scaled_y, gyro_scaled_z,
#accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()
       

    
bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards
# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

now = time.time()
K = 0.98
K1 = 1 - K
time_diff = 0.01

(last_x, last_y, gyro_offset_x, gyro_offset_y, gyro_total_x, gyro_total_y) = initPlane()
    

while True:
    #Lists holding filtered values over time
    rep_x = list()
    rep_y = list()
    #int / time_diff = samples
    for i in range(0, int(3 / time_diff)):
        time.sleep(time_diff - 0.005) 
        
        (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()
        
        gyro_scaled_x -= gyro_offset_x
        gyro_scaled_y -= gyro_offset_y
        
        gyro_x_delta = (gyro_scaled_x * time_diff)
        gyro_y_delta = (gyro_scaled_y * time_diff)

        gyro_total_x += gyro_x_delta
        gyro_total_y += gyro_y_delta

        rotation_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
        rotation_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

        last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
        last_y = K * (last_y + gyro_y_delta) + (K1 * rotation_y)
        
        rep_x.append(last_x)
        rep_y.append(last_y)

    #Calculates whether still
    total = 0
    for q in range(0,len(rep_x)):
        try:
            #May want one axis to be more valuable?
            #i.e. weight down x movements if y is more important
            total += (rep_x[q+1] - rep_x[q]) + (rep_y[q+1] - rep_y[q])
        except IndexError:
            total += 0

    print(total)
    #CHANGEME:
    #Needs testing to determine apropriate value
    if total > 10:
        print("Rep!")
    
        
        
