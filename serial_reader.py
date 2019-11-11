#!/usr/bin/python3
#Based on https://www.raspberrypi.org/forums/viewtopic.php?t=106468

import serial, string

ser = serial.Serial('/dev/ttyUSB0', 9600)
print(ser.name) 
output = " "
while True:
   print ("----")
   while output != "":
     output = ser.readline()
     print (output)
   output = " "