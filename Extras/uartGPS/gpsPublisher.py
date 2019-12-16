#! /usr/bin/env python
import serial
import os
import rospy
import numpy as np
import json
import importlib
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import time


class gpsPublisher(object):

    def __init__(self):
        #Publisher to send delta values to the drone for flying
        self.setpoint = rospy.Publisher('/gpsTarget', String, queue_size=0)
        self.gps = serial.Serial("/dev/ttyTHS0", baudrate=57600, timeout=1)


        
    # Subscriber callback to listen to rc channels
    def manual_override(self, msg):
	#rospy.loginfo(msg.axes[4])
	if msg.axes[4] != 1:
                self._coordinate = ""
                rospy.logfatal("Manual Override")
		rospy.signal_shutdown("Manual Override")
        
    #Function to read the JSON information from file (Previously saved by local_path packege)
    def gpsPublish(self):
        while gps.is_open:
                position = gps.readline()
                rospy.loginfo(position)
                self.gps.publish(position)

   

if __name__ == "__main__":
    rospy.init_node('gps_publisher', log_level=rospy.INFO)
    go_home_object = gpsPublisher()
    rospy.spin()



	

			
	

