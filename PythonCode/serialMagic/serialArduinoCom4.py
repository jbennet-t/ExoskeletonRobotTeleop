# Program for basic communication between microcontroller and python
# pair with basicSerial_Python arduino program
# reference: https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
# reference: https://pyserial.readthedocs.io/en/latest/shortintro.html#


# first run --    python -m serial.tools.list_ports
# ^ finds which COM port
# also, arduino serial monitor must be closed to transmit serial data


import serial
import time

ser = serial.Serial('COM5', baudrate=9600)
ser.flushInput() # clears queue so that data doesn't overlap

while True:
    #try:
    ser_decoded = ser.readline().decode('utf-8')
    print(ser_decoded)
   # except:
    #    print("Keyboard Interrupt")
     #   break