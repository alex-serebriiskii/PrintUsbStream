#!/usr/bin/python3
#Based on https://www.raspberrypi.org/forums/viewtopic.php?t=106468

import serial, string

output = " "
ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 9600
ser.open
output = " "
while True:
   print ("----")
   while output != "":
     output = ser.readline()
     print (output)
   output = " "