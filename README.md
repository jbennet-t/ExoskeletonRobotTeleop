# ExoskeletonRobotTeleop
Project centered around development of a wearable exoskeleton that translates user joint positions and movements in real time to a humanoid NAO robot.
Developed by Jordan Sinoway and Brian Dawson for 2021 Senior Capstone Project @ TCNJ

Exoskeleton embedded and Python code developed for Teensy 3.5 and NAO v4 robot, however could easily be reapplied to a new microcontroller and robot. Would suggest not using the NAO in the future due to reliability issues. 

If you have any questions about the project, feel free to contact me.

## Exoskeleton Overview Model
![Pic](https://github.com/jbennet-t/ExoskeletonRobotTeleop/blob/master/Diagrams/Exoskeleton_DoF_Diagram2.png)


## Abstract
The goal of this project is to create a novel exoskeleton apparatus that captures the movements of the wearer, and then translates these movements to a humanoid robot, granting approximately real-time teleoperation. The robot utilized for this project is Aldebaran Robotics’ NAO, a ⅓ scale humanoid robot. Teleoperation has many practical applications, including hazardous waste disposal, robotics surgery, and tasks in the military, space, sea, and medical sectors. Potentiometers are integrated into the mechanical design at key joints in the wrist, elbow, and shoulder of the exoskeleton. These sensors vary their voltage depending on the joint angle and these values are passed to the Teensy 3.5 microcontroller via a 13-bit ADC. The microcontroller then converts the data into usable angle measurements and passes them to a Python layer, via a serial data line, which in turn converts the angle measurements into commands the robot can interpret. The embedded code in the microcontroller is written in C++ and the Python intermediary layer utilizes Python 2.7 and the NAOqi SDK to control the robot. 


### What's Important
- Python_Intermediary_Layer.py - https://github.com/jbennet-t/ExoskeletonRobotTeleop/blob/master/Brian-Code/Python_Intermediary_Layer.py
- Everything in the Diagrams subdirectory
- Exoskeleton_main.ino https://github.com/jbennet-t/ExoskeletonRobotTeleop/blob/master/EmbeddedCode/exoskeleton_main/exoskeleton_main.ino
- Everything in the Exoskeleton_Models subdirectory (all stls are not up to date, should be regenerated)
- Exoskeleton_PCBv3: https://github.com/jbennet-t/ExoskeletonRobotTeleop/tree/master/PCB/Exoskeleton_PCBv3
- 

### Materials List
Items required: (Approximate Cost ~$250)
- Teensy 3.5 Microcontroller (x1)
- Bourns PDF241-S425F Potentiometers (x12)
- STM LD1117 3.3V Fixed Voltage Regulator (x1)
- 3-Terminal Might-SPOX Molex Male Header (x12)
- 3-Terminal Might-SPOX Molex Female Header (x12)
- Film Capacitors (x3)
- Green Through-hole LED (x1)
- 2 Pole Switch (x1)
- M5 Bolts and Nuts (x20)
- 12ft USB 2.0 Cable (x1)
- ¾” PVC Pipe - 4ft Segment (x5)
- Backpack Straps (x2)
- 22 AWG Silicone Wire 40ft (x1)
- 3D Printed Components
- Printed Circuit Board


