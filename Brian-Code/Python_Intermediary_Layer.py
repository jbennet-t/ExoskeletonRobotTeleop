import naoqi
import sys
import motion
import time
import argparse
import threading
import serial
from naoqi import ALProxy

#IP and Port of the Nao
NAO_IP = "192.168.1.149"
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
        instruction_set = ser_bytes.split(" ")
    #Try statements to ensure data isn't missing
    #Replaces with zero if there is an issue with one of the potentiometers
    #Creates a new thread in order to interpt multiple movement commands at once
        try:
            angle1 = float(instruction_set[0])
        except:
            angle1 = 0
        th1 = threading.Thread(target=move_arm, args = ("LShoulderPitch", angle1))
        th1.start()
        #thread.start_new_thread(move_arm, ("LShoulderPitch", angle1))
        try:
            angle2 = float(instruction_set[1])
        except:
            angle2 = 0
        #thread.start_new_thread(move_arm, ("LShoulderRoll", angle2))
        th2 = threading.Thread(target=move_arm, args = ("LShoulderRoll", angle2))
        th2.start()
        try:
            angle3 = float(instruction_set[2])
        except:
            angle3 = 0
        #thread.start_new_thread(move_arm("LElbowRoll", angle3))
        th3 = threading.Thread(target=move_arm, args = ("LElbowRoll", angle3))
        th3.start()
        try:
            angle4 = float(instruction_set[3])
        except:
            angle4 = 0
        #thread.start_new_thread(move_arm("LElbowYaw", angle4))
        th4 = threading.Thread(target=move_arm, args = ("LElbowYaw", angle4))
        th4.start()
        try:
            angle5 = float(instruction_set[4])
        except:
            angle5 = 0
        #thread.start_new_thread(move_arm("LWristYaw", angle5))
        th5 = threading.Thread(target=move_arm, args = ("LWristYaw", angle5))
        th5.start()
        try:
            angle6 = float(instruction_set[6])
        except:
            angle6 = 0
        #thread.start_new_thread(move_arm("RShoulderPitch", angle6))
        th6 = threading.Thread(target=move_arm, args = ("RShoulderPitch", angle6))
        th6.start()
        try:
            angle7 = float(instruction_set[7])
        except:
            angle7 = 0
        #thread.start_new_thread(move_arm("RShoulderRoll", angle7))
        th7 = threading.Thread(target=move_arm, args = ("RShoulderRoll", angle7))
        th7.start()
        try:
            angle8 = float(instruction_set[8])
        except:
            angle8 = 0
        #thread.start_new_thread(move_arm("RElbowRoll", angle8))
        th8 = threading.Thread(target=move_arm, args = ("RElbowRoll", angle8))
        th8.start()
        try:
            angle9 = float(instruction_set[9])
        except:
            angle9 = 0
        #thread.start_new_thread(move_arm("RElbowYaw", angle9))
        th9 = threading.Thread(target=move_arm, args = ("RElbowYaw", angle9))
        th9.start()
        try:
            angle10 = float(instruction_set[10])
        except:
            angle10 = 0
        #thread.start_new_thread(move_arm("RWristYaw", angle10))
        th10 = threading.Thread(target=move_arm, args = ("RWristYaw", angle10))
        th10.start()


