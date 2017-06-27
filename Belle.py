#!/usr/bin/python
#Smartbell project in culmination!
#Featuring:
#BELLE: Neural Network classifier
#LISA: Interface and complex filter of MPU6050 chip
#Framework: Posts data to server upon program completion
#Rep calculation
#Vibration motor controls

#Library imports
from nimblenet.activation_functions import sigmoid_function
from nimblenet.cost_functions import cross_entropy_cost
from nimblenet.learning_algorithms import *
from nimblenet.neuralnet import NeuralNet
from nimblenet.preprocessing import construct_preprocessor, standarize
from nimblenet.data_structures import Instance
from nimblenet.tools import print_test
import random
import smbus
import math
import time
import os
import RPi.GPIO as GPIO
import requests
import json
import datetime

##-------------------BELLE--------------------

## Loads Belle's beautiful brain
network = NeuralNet.load_network_from_file( "Brains/Belle_1.pkl" )

# Print a network test
#print_test( network, training_data, cost_function )


##------------------LISA--------------------
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

bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

now = time.time()

K = 0.98
K1 = 1 - K

time_diff = 0.01

(gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()

last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

gyro_offset_x = gyro_scaled_x 
gyro_offset_y = gyro_scaled_y

gyro_total_x = (last_x) - gyro_offset_x
gyro_total_y = (last_y) - gyro_offset_y


#Returns current time in JS format
def getDate():
    d = datetime.datetime.utcnow()
    #Remember! JS takes miliseconds, Python gives seconds.
    return str(time.mktime(d.timetuple())) * 1000 #Sec*1000 = MilSec

##------------Vibration motor setup-----------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#BCM or BOARD
pin = 23
GPIO.setup(pin, GPIO.OUT)

#Variables used whilst data streaming
nSlice = list()
reps = 0
N = 20
#preprocess = construct_preprocessor( dataset, [standarize] ) 

##-------Data streaming---------
try:
    while True:
        time.sleep(time_diff - 0.005) 
    
        (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()

        ##-----Lisa finishing complex filter job--------
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

        #[X1,Y1,X2,Y2]
        nSlice.append(last_x)
        nSlice.append(last_y)

        #When N values have been recorded
        if len(nSlice) == N:

            ##----------Predictions------------
            #Throws nSlice to Belle
            #prediction_set = preprocess( nSlice )
            #Prints a prediction!
            #HIGH LOW = Bicep Curl!
            #LOW HIGH = Trash!
            print network.predict( Instance (nSlice) )

 
            ##----------Rep Calculation--------
            temp_x = nSlice[0]
            temp_y = nSlice[1]
            total = 0

            for i in range(len(nSlice)):
                if i % 2 == 0:
                    total += (nSlice[i] - temp_x)    
                else:
                    total += (nSlice[i] - temp_y)

            #Pops X1,Y1 for sliding window
            nSlice = nSlice[2:]

            #Value needs testing
            if total < 10:            
                #Sets vibration on then off
                GPIO.output(pin, True)
                #System sleeps - Curl not rated whilst stationary
                time.sleep(1)
                GPIO.output(pin, False)
                #Incriments rep counter
                reps += 1
            
         
#Breaks on Control+C
#REFACTOR FOR LIVE USE
except KeyboardInterrupt:
        ##-------------Testing----------------
        print("Rep count:" + str(reps))
        

    
##    ##-----------Framework----------------
##    #Outputs to new JSON post each time
##    jsonString = '[{"dumbbell_id":"serialID","user_id":"TBI","date":' + getDate() + ,',"workout":"bicepcurl","reps":' + reps + ',"form":404}]'
##    #HTTP Post request on z
##    head = {'Content-Type': 'application/json'}
##    
##    r = requests.post('http://46.101.3.244:8080/api/workoutData', data = json.dumps(z.data), headers=head)

