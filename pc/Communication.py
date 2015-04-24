import serial, sys
import time

port1 = "/dev/rfcomm0"
port2 = "/dev/rfcomm1"

# main() function
def main():
  # open serial ports
  ser1 = serial.Serial(port1, 9600)
  ser2 = serial.Serial(port2, 9600)
  while True:
  #device1
    ser1.write('0')
    while (ser1.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    line = ser1.readline()
    line = line.replace("\n","")
    print '0: '+line
    time.sleep(0.01)
   #device2
    ser2.write('0')
    line = ""
    while (ser2.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    line = ser2.readline()
    line = line.replace("\n","")
    print '1: '+line
    time.sleep(0.01)

  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
