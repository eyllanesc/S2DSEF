import serial, sys
import time
import string
"""Accel 20:15:02:02:01:06"""
port = "/dev/rfcomm0"

# main() function
def main():
  # open serial ports
  ser = serial.Serial(port, 9600)
  while True:
  #device1
    ser.write('0')
    while (ser.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    line = ser.readline()
    data = data = [float(val) for val in line.split()]
    if len(data)>2:
	print(str(data[0])+" "+str(data[1])+" "+str(data[2]))
    time.sleep(0.01)
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
