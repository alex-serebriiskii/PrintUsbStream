#!/usr/bin/python3
#Based on https://www.raspberrypi.org/forums/viewtopic.php?t=106468

import serial, string, time, os, getpass

user = os.getlogin()
path = '/home/%s/test.txt' %(user)
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1)
ser.timeout = 10
def main():
  if(filewriter()):
    exit

def filewriter():
  
  file = open(path, 'wb')
  contenttoprint = False;
  print(ser.name) 
  output = " "
  while True:
    print ("####New Transmission####\n")
    while output != "":
      output = ser.readline()
      print (output)
      file.write(output)
      if(output == b''):
        print("Output is empty")
        if contenttoprint == True:
          print("printing")
          file.close()
          #os.system("lpr /home/alex/test.txt")
          #print something here
          file = open(path, 'wb')
        contenttoprint = False
      else:
        contenttoprint = True

    print("#### End of Transmission####\n")
    return True
    output = " "

def timedfilewriter(file, timeout):
  print(ser.name)
  print("Start Reading\n")
  tic = time.time()
  while (time.time() - tic) < timeout:
    output = ser.readline()
    file.write(output.decode('UTF8'))
    print(output)
    tic = time.time
  return True
main()