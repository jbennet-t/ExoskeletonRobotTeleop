import naoqi
import sys
import motion
import time
import argparse
import thread
import serial
from naoqi import ALProxy

NAO_IP = "10.20.4.61"
PORT = 9559

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
    
autolifeProxy.setState("disabled")


sleeptime = 0.0
speed = 0.6

def move_arm(names, angles):
    
    motionProxy.setAngles(names, angles, speed)
    time.sleep(sleeptime)
    #print "%s: Input = %d || Output = %d\n" %(names, angles, speed)

motionProxy.setStiffnesses("LArm", 0.0)
motionProxy.setStiffnesses("RArm", 0.0)
motionProxy.setStiffnesses("Body", 1.0)

postureProxy.goToPosture("Sit" , 1.0)

#move_arm("RShoulderPitch", 2.0)
#move_arm("RShoulderRoll", -0.1)
#move_arm("RElbowRoll", -0.5)
#move_arm("RElbowYaw", 1.3)
#move_arm("RElbowYaw", -1.5)
#move_arm("RElbowRoll", 1.0)

port = 'COM3'
baudrate = 9600

teensy3 = serial.Serial(port,baudrate)
teensy3.flushInput()

# Shoulder Roll Range: -18 to 76 degrees (-.3142 to 1.3265 radians)
# Shoulder Pitch Range: -119.5 to 119.5 degrees (-2.0857 to 2.0857 radians)
# Elbow Yaw Range: -119.5 to 119.5 degrees (-2.0857 to 2.0857 radians)
# Elbow Roll Range: -88.5 to -2 degrees (-1.5446 to -0.0349 radians)
# Wrist Yaw Range: -104.5 to 104.5 degrees (-1.8238 to 1.8238 radians)

while True:
    try:
        ser_bytes = teensy3.readline()
    except:
        print("Keyboard Interrupt")
        break
    else:
        ser_bytes = teensy3.readline()
        print(ser_bytes)
        instruction_set = ser_bytes.split(" ")
        print(instruction_set)
        print(instruction_set[0])
##        try:
##            angle1 = float(instruction_set[0])
##        except:
##            angle1 = 0
##        thread.start_new_thread(move_arm, ("LShoulderPitch", angle1))
##        try:
##            angle2 = float(instruction_set[1])
##        except:
##            angle2 = 0
##        thread.start_new_thread(move_arm, ("LShoulderRoll", angle2))
##        try:
##            angle3 = float(instruction_set[2])
##        except:
##            angle3 = 0
##            thread.start_new_thread(move_arm("LElbowRoll", angle3))
##        try:
##            angle4 = float(instruction_set[3])
##        except:
##            angle4 = 0
##            thread.start_new_thread(move_arm("LElbowYaw", angle4))
##        try:
##            angle5 = float(instruction_set[4])
##        except:
##            angle5 = 0
##            thread.start_new_thread(move_arm("LWristYaw", angle5))
        try:
            angle6 = float(instruction_set[6])
        except:
            angle6 = 0
            thread.start_new_thread(move_arm("RShoulderPitch", angle6))
        try:
            angle7 = float(instruction_set[7])
        except:
            angle7 = 0
            thread.start_new_thread(move_arm("RShoulderRoll", angle7))
        try:
            angle8 = float(instruction_set[8])
        except:
            angle8 = 0
            thread.start_new_thread(move_arm("RElbowRoll", angle8))
        try:
            angle9 = float(instruction_set[9])
        except:
            angle9 = 0
            thread.start_new_thread(move_arm("RElbowYaw", angle9))
        try:
            angle10 = float(instruction_set[10])
        except:
            angle10 = 0
            thread.start_new_thread(move_arm("RWristYaw", angle10))


