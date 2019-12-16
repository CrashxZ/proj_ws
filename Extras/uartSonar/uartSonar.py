import serial
import os

#Front Back Right Left
# 1   - 1  -  1  - 1 Movement Alowed
# 0   - 0  -  0  - 0 Movement Restricted


sonar = serial.Serial("/dev/ttyTHS0", baudrate=9600, timeout=1)
while sonar.is_open:
	input = sonar.readline()
	print input
# Uncomment for killing autonomous nodes
#	if(input[0]=='0' or input[1]=='0' or input[2]=='0' or input[3]=='0'):
#		os.system("rosnode kill go_home")
#		os.system("rosnode kill reach_target")
			
	

