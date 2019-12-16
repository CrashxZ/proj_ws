import serial
import os




gps = serial.Serial("/dev/ttyTHS0", baudrate=56700, timeout=1)
while gps.is_open:
	input = gps.readline()
	print input

			
	

