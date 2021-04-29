# ExoskeletonRobotTeleop
Project centered around development of a wearable exoskeleton that translates user joint positions and movements in real time to a humanoid robot.
Developed by Jordan Sinoway and Brian Dawson for Senior Capstone Project @ TCNJ

## Exoskeleton Overview Model
![Pic](https://github.com/jbennet-t/ExoskeletonRobotTeleop/blob/master/Diagrams/Exoskeleton_DoF_Diagram2.png)

## Abstract

The goal of this project is to create a novel exoskeleton apparatus that captures the movements of the wearer, and then translates these movements to a humanoid robot, granting approximately real-time teleoperation. The robot utilized for this project is Aldebaran Robotics’ NAO, a ⅓ scale humanoid robot. Teleoperation has many practical applications, including hazardous waste disposal, robotics surgery, and tasks in the military, space, sea, and medical sectors. Potentiometers are integrated into the mechanical design at key joints in the wrist, elbow, and shoulder of the exoskeleton. These sensors vary their voltage depending on the joint angle and these values are passed to the Teensy 3.5 microcontroller via a 13-bit ADC. The microcontroller then converts the data into usable angle measurements and passes them to a Python layer, via a serial data line, which in turn converts the angle measurements into commands the robot can interpret. The embedded code in the microcontroller is written in C++ and the Python intermediary layer utilizes Python 2.7 and the NAOqi SDK to control the robot. 

