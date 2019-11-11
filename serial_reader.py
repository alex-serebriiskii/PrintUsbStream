#!/usr/bin/python3
#Based on https://www.raspberrypi.org/forums/viewtopic.php?t=106468

import serial, string

output = " "
ser = serial.Serial('/dev/ttyUSB0')
print(ser.name)
# while True:
#   print "----"
#   while output != "":
#     output = ser.readline()
#     print (output)
#   output = " "