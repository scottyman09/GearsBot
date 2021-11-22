#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
import random
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
radio = Radio()

gyro_sensor_in1 = GyroSensor(INPUT_1)
gps_sensor_in2 = GPSSensor(INPUT_2)

motorC = LargeMotor(OUTPUT_C) # Magnet
motorD = LargeMotor(OUTPUT_D) # Magnet

# Here is where your code starts

tank_drive.on_for_rotations(-20, -20, 9)

tank_drive.on_for_rotations(-20, 20, 0.68)

tank_drive.on_for_rotations(-20, -20, 3)

while True: 
    tank_drive.on_for_rotations(20, 20, 5)
    tank_drive.on_for_rotations(-20, -20, 5)
