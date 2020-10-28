import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM5'
ser.open()

fig, ax = plt.subplots()

ydata = []


def update_data(i):
    newpoint = float(ser.readline())
    ydata.append(newpoint)
    ax.clear()
    ax.plot(ydata)


ani = animation.FuncAnimation(fig, update_data, interval=1000)
plt.show()