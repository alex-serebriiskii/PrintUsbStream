import os.path
from os import path
class config:
	timeout = 10
	usb_port= '/dev/ttyUSB0'
	baud_rate: 9600
	bits: 8
	letter: 'N'
	other_thing: 1
	print_command: 'lp'

	def _init__(self):
		if(path.exists('settings.conf')):
			conf = open('settings.conf',"r")
			for line in conf:
				opts = line.split(" ")
				if opts[0] == "timeout:":
					timeout = int(opts[1])
				elif opts[0] == "usb_port:":
					usb_port = opts[1]
				elif opts[0] == "baud_rate:":
					baud_rate = int(opts[1])
				elif opts[0] == "bits":
					bits = int(opts[1])
				elif opts[0] ==  "letter:":
					letter = opts[1]
				elif opts[0] == "other_thing:":
					other_thing = int(opts[1])
				elif opts[0] == "print_command:":
					print_command = opts[1]









