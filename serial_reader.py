#!/usr/bin/python3
#Based on https://www.raspberrypi.org/forums/viewtopic.php?t=106468

import serial, string, time, os, getpass

user = getpass.getuser()
path = '/tmp/radiooutput'
printcommand = 'lp %s'%(path)
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1)
ser.timeout = 10
def main():
  if(filewriter()):
    exit

def filewriter():
  
  file = open(path, 'wb')
  contenttoprint = False
  #print(ser.name) 
  output = " "
  while True:
    print ("#### Awating Transmissions ####\n")
    while output != "":
      output = ser.readline()
      file.write(output)
      if(output == b''):
        if contenttoprint == True:
          print("printing")
          file.close()
          os.system(printcommand)
          file = open(path, 'wb')
        contenttoprint = False
      else:
        print(output)
        contenttoprint = True

    return True
    output = " "

main()