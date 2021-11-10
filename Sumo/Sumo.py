#!/usr/bin/env python3

# USE THE SINGLE SENSOR LINE FOLLOWER ROBOT

# Import the necessary libraries
import time
import math
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

color_sensor_in1 = ColorSensor(INPUT_1)
ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)
gyro_sensor_in3 = GyroSensor(INPUT_3)
gps_sensor_in4 = GPSSensor(INPUT_4)
pen_in5 = Pen(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts

while True:
    distance = ultrasonic_sensor_in2.distance_centimeters
    print(color_sensor_in1.color )
    if(color_sensor_in1.color != 5):
        if(distance != 255):
            tank_drive.on(70,70)
        else:
            tank_drive.on(20, -20)
    else:
        tank_drive.on(-60, -60)
        time.sleep(1.5)
