import naoqi
import sys
import motion
import time
import argparse
import thread
import serial
from naoqi import ALProxy

NAO_IP = "10.20.4.70"
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
    print "%s: Input = %d || Output = %d\n" %(names, angles, speed)

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


teensy3 = serial.Serial()
teensy3.baudrate = 9600
teensy3.port = 'COM5'
teensy3.flushInput()

while True:
    try:
        ser_bytes = tennsy3.readline()
        #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        #print(decoded_bytes)
    except:
        print("Keyboard Interrupt")
        break
    else:
        ser_bytes = tennsy3.readline()
             if ser_bytes
                    instruction_set = ser_bytes.split(";")
                        if instruction_set
                            thread.start_new_thread(move_arm("LShoulderPitch", instruction_set[0]))
                            thread.start_new_thread(move_arm("LShoulderRoll", instruction_set[1]))
                            thread.start_new_thread(move_arm("LElbowRoll", instruction_set[2]))
                            thread.start_new_thread(move_arm("LElbowYaw", instruction_set[3]))
                            thread.start_new_thread(move_arm("LWristYaw", instruction_set[4]))
                            thread.start_new_thread(move_arm("RShoulderPitch", instruction_set[6]))
                            thread.start_new_thread(move_arm("RShoulderRoll", instruction_set[7]))
                            thread.start_new_thread(move_arm("RElbowRoll", instruction_set[8]))
                            thread.start_new_thread(move_arm("RElbowYaw", instruction_set[9]))
                            thread.start_new_thread(move_arm("RWristYaw", instruction_set[10]))



