#!/usr/bin/python3
#Based on https://www.raspberrypi.org/forums/viewtopic.php?t=106468

import serial, string

path = '/home/alex/test.txt'

def main():
  file = open(path, 'w')
  if(filewriter(file)):
    file.close

def filewriter(file):
  ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1)
  print(ser.name) 
  output = " "
  while True:
    print ("####New Transmission####\n")
    while output != "":
      output = ser.readline()
      file.write(output.decode('UTF8'))
      print (output)
    print("#### End of Transmission####\n")
    return True
    output = " "
main()