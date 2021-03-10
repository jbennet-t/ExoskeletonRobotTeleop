import naoqi
import sys
import motion
import time
import argparse
import thread
import serial
from naoqi import ALProxy

#IP and Port of the Nao
NAO_IP = "192.168.1.103"
PORT = 9559

#Ensuring the Nao Robot can be connected to properly
#Tries the varies different ALProxy methods used in code
try:
    motionProxy = ALProxy("ALMotion", NAO_IP, PORT)
except Exception, e:
    print "Could not create proxy to ALMotion"
    print "Error is ", e
else:
    motionProxy = ALProxy("ALMotion", NAO_IP, PORT)

try:
    autolifeProxy = ALProxy("ALAutonomousLife", NAO_IP, PORT)
except Exception, e:
    print "Could not create proxy to ALAutonomousLife"
    print "Error is ", e
else:
    autolifeProxy = ALProxy("ALAutonomousLife", NAO_IP, PORT)
    
try:
    postureProxy = ALProxy("ALRobotPosture", NAO_IP, PORT)
except Exception, e:
    print "Could not create proxy to ALRobotPosture"
    print "Error is", e
else:
    postureProxy = ALProxy("ALRobotPosture", NAO_IP, PORT)

#Disables the autonomous life mode
autolifeProxy.setState("disabled")

#Sets the sleeptime between commands to zero
#Sets speed of how fast robot moves from one position to another
sleeptime = 0.0
speed = 0.6


#Method used to control robot
#Takes in name of joint and the angle requested
def move_arm(names, angles):
    
    motionProxy.setAngles(names, angles, speed)
    time.sleep(sleeptime)


#Sets stiffness to zero and back to one in order to properly function
#Setting angles doesn't work without these commands
motionProxy.setStiffnesses("LArm", 0.0)
motionProxy.setStiffnesses("RArm", 0.0)
motionProxy.setStiffnesses("Body", 1.0)

#Go to sitting position to set robot to predetermined position
postureProxy.goToPosture("Stand" , 1.0)


#Setting serial port and baudrate for serial connection
print("Pre-serial test okay")
port = 'COM3'
baudrate = 9600

#Creating serial connection and flushing input
teensy3 = serial.Serial(port,baudrate)
teensy3.flushInput()

#Reference Information
# Shoulder Roll Range: -18 to 76 degrees (-.3142 to 1.3265 radians)
# Shoulder Pitch Range: -119.5 to 119.5 degrees (-2.0857 to 2.0857 radians)
# Elbow Yaw Range: -119.5 to 119.5 degrees (-2.0857 to 2.0857 radians)
# Elbow Roll Range: -88.5 to -2 degrees (-1.5446 to -0.0349 radians)
# Wrist Yaw Range: -104.5 to 104.5 degrees (-1.8238 to 1.8238 radians)

move_arm("LShoulderPitch", -.3142)
time.sleep(1)
move_arm("LShoulderPitch", 1.3265)
time.sleep(1)
move_arm("LShoulderPitch", 0)
time.sleep(1)
move_arm("LShoulderRoll", -2.0857)
time.sleep(1)
move_arm("LShoulderRoll", 2.0857)
time.sleep(1)
move_arm("LShoulderRoll", 0)
time.sleep(1)
move_arm("LElbowRoll", -1.5446)
time.sleep(1)
move_arm("LElbowRoll", -0.0349)
time.sleep(1)
move_arm("LElbowRoll", 0)
time.sleep(1)
move_arm("LElbowYaw", -2.0857)
time.sleep(1)
move_arm("LElbowYaw", 2.0857)
time.sleep(1)
move_arm("LWristYaw", -1.8238)
time.sleep(1)
move_arm("LWristYaw", 1.8238)
time.sleep(1)
move_arm("LWristYaw", 0)
time.sleep(1)

postureProxy.goToPosture("Stand" , 1.0)

move_arm("RShoulderPitch", -.3142)
time.sleep(1)
move_arm("RShoulderPitch", 1.3265)
time.sleep(1)
move_arm("RShoulderPitch", 0)
time.sleep(1)
move_arm("RShoulderRoll", -2.0857)
time.sleep(1)
move_arm("RShoulderRoll", 2.0857)
time.sleep(1)
move_arm("RShoulderRoll", 0)
time.sleep(1)
move_arm("RElbowRoll", -1.5446)
time.sleep(1)
move_arm("RElbowRoll", -0.0349)
time.sleep(1)
move_arm("RElbowRoll", 0)
time.sleep(1)
move_arm("RElbowYaw", -2.0857)
time.sleep(1)
move_arm("RElbowYaw", 2.0857)
time.sleep(1)
move_arm("RWristYaw", -1.8238)
time.sleep(1)
move_arm("RWristYaw", 1.8238)
time.sleep(1)
move_arm("RWristYaw", 0)
time.sleep(1)

postureProxy.goToPosture("Stand" , 1.0)

#Always runs to ensure constant stream of information
while True:
    
    #Checking if the serial connection is open
    
    try:
        ser_bytes = teensy3.readline()
    except:
        print("Error in serial connection")
        break
    else:
    #Splitting the data into individual components
        ser_bytes = teensy3.readline()
        instruction_set = ser_bytes.split(",")
        #print (ser_bytes)
        #print (instruction_set)
    #Try statements to ensure data isn't missing
    #Replaces with zero if there is an issue with one of the potentiometers
    #Creates a new thread in order to interpt multiple movement commands at once
        try:
            angle1 = float(instruction_set[0])
        except:
            angle1 = 0
        thread.start_new_thread(move_arm, ("LShoulderPitch", angle1))
        try:
            angle2 = float(instruction_set[1])
        except:
            angle2 = 0
        thread.start_new_thread(move_arm, ("LShoulderRoll", angle2))
        try:
            angle3 = float(instruction_set[2])
        except:
            angle3 = -1
        thread.start_new_thread(move_arm, ("LElbowRoll", angle3))
        try:
            angle4 = float(instruction_set[3])
        except:
            angle4 = 0
        thread.start_new_thread(move_arm, ("LElbowYaw", angle4))
        try:
            angle5 = float(instruction_set[4])
        except:
            angle5 = 0
        thread.start_new_thread(move_arm, ("LWristYaw", angle5))
        try:
          angle6 = float(instruction_set[6])
        except:
            angle6 = 0
        thread.start_new_thread(move_arm, ("RShoulderPitch", angle6))
        try:
            angle7 = float(instruction_set[7])
        except:
            angle7 = 0
        thread.start_new_thread(move_arm, ("RShoulderRoll", angle7))
        try:
            angle8 = float(instruction_set[8])
        except:
            angle8 = -1
        thread.start_new_thread(move_arm, ("RElbowRoll", angle8))
        try:
            angle9 = float(instruction_set[9])
        except:
            angle9 = 0
        thread.start_new_thread(move_arm, ("RElbowYaw", angle9))
        try:
            angle10 = float(instruction_set[10])
        except:
            angle10 = 0
        thread.start_new_thread(move_arm, ("RWristYaw", angle10))
