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
speed = 0.8


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
postureProxy.goToPosture("Sit" , 1.0)
