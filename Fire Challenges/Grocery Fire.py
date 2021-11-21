#!/usr/bin/env python3

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
drops = 0
currentColour = 0
leftTurn = 0
rightTurn = 0
path = []

def Reverse():
    tank_drive.off(brake=True)
    tank_drive.on_for_rotations(-20, -20, 4)
    

while True: 
    if(currentColour):
        for(turn in path):
            print(turn)
    else:
        if(gps_sensor_in4.y < -71):
            tank_drive.on(20, 20)
        else: 
            # 3 = green
            if(ultrasonic_sensor_in2.distance_centimeters < 30):
                tank_drive.on(20, 20)
                if(color_sensor_in1.color == 3):
                    motorC.on(100)
                    currentColour = "green"
                    time.sleep(500 / 1000)
                    Reverse()
                elif(color_sensor_in1.color == 5):
                    motorC.on(100)
                    currentColour = "red"
                    time.sleep(500 / 1000)
                    Reverse()
            else: 
                offset = color_sensor_in1.reflected_light_intensity - 50
                steering_drive.on(offset * 2, 20)
                if(gyro_sensor_in3.angle == -90 or gyro_sensor_in3.angle == -180):
                    leftTurn =+ 1
                    path.append('left')
                    print("left Turns", leftTurn)
                elif(gyro_sensor_in3.angle == 90 or gyro_sensor_in3.angle == 180):
                    rightTurn =+ 1
                    path.append('right')
                    print("right Turns", rightTurn)
