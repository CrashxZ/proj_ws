#! /usr/bin/env python
import rospy
import numpy as np
import json
from ast import literal_eval
import importlib
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import time
import os


class reachTarget(object):

    def __init__(self):
	self.target = ""
	self.position = ""
        self.delta = ""
	self.aligntarget_x = 0.5
	self.aligntarget_y = 0.5
	self.probabilityThreshlold = 0.80
        #Subscriber to get Target Position
        self._hunter = rospy.Subscriber('/drone_hunter_topic', String, self.get_target_location)
	self.rc = rospy.Subscriber('/dji_sdk/rc', Joy, self.manual_override)
        #Publisher to send delta values to the drone for flying
        self.setpoint = rospy.Publisher('/dji_sdk/flight_control_setpoint_ENUvelocity_yawrate', Joy, queue_size=0)
        self.goToTarget()


    # Subscriber callback for Target Position Information
    def get_target_location(self, msg):
	#rospy.loginfo(msg)
	if msg.data != "-999":
		self.target = literal_eval(msg.data);
		if type(self.target) is not dict : 
			self.target = self.target[0]
	if msg.data == "-999":
		self.target = ""
		#rospy.loginfo(self.target )
		#rospy.loginfo(self.target["x"] )



    # Subscriber callback to listen to rc channels
    def manual_override(self, msg):
	#rospy.loginfo(msg.axes[4])
	if msg.axes[4] != 1:
                self._coordinate = ""
                rospy.logfatal("Manual Override")
		rospy.signal_shutdown("Manual Override")
		


    #Function to Publish data to the publisher
    def goToTarget(self):
	rate = rospy.Rate(1)
	kill_code = 0
	while not rospy.is_shutdown():
		if(self.target !=""):
		    	if (self.target != "" and self.target["prob"] > self.probabilityThreshlold):
                                #kill trajectory control
                                if(kill_code == 0):
                                    os.system("rosnode kill go_home")
									os.system("rosnode kill path_to_file")
                                    kill_code = 1
                                    
				#relative distance calculation
				#right movement
				movement_offset = Joy()
				while(self.target != "" and self.target["x"] + (self.target["w"]/2) > self.aligntarget_x):
					movement_offset.axes = [0.2, 0, 0] 
					self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)
					rate.sleep()

				#left movement
				movement_offset = Joy()
				while(self.target != "" and self.target["x"] + (self.target["w"]/2) < self.aligntarget_x):
					movement_offset.axes = [-0.2, 0, 0] 
					self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)
					rate.sleep()

				#front movement
				movement_offset = Joy()
				while(self.target != "" and self.target["y"] + (self.target["h"]/2) < self.aligntarget_y):
					movement_offset.axes = [0, 0.2, 0] 
					self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)
					rate.sleep()
				#back movement
				movement_offset = Joy()
				while(self.target != "" and self.target["y"] + (self.target["h"]/2) > self.aligntarget_y):
					movement_offset.axes = [0, -0.2, 0] 
					self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)
					rate.sleep()
				if self.target != "" and (self.target["y"] + (self.target["h"]/2)> (self.aligntarget_y-0.1) and (self.target["y"] + (self.target["h"]/2)< self.aligntarget_y+0.1) and (self.target["x"] + (self.target["w"]/2)> self.aligntarget_x-0.1 ) and (self.target["x"] + (self.target["w"]/2)< self.aligntarget_x+0.1)):
					rospy.loginfo("Fire!")
					#GPIO : send PVM signal for relay to fire and close pwm
					os.system("rosservice call /dji_sdk/mfio_config \"mode: 0 channel: 0 init_on_time_us: 2500 pwm_freq: 50\"")
					rospy.loginfo("Reseting PWM!")
					os.system("sleep 10; rosservice call /dji_sdk/mfio_config \"mode: 0 channel: 0 init_on_time_us: 500 pwm_freq: 50\"")
					# calling gohome
					os.system("sleep 50;./gohome.sh")
					break



if __name__ == "__main__":
    rospy.init_node('reach_target', log_level=rospy.INFO)
    go_home_object = reachTarget()
    rospy.spin()
