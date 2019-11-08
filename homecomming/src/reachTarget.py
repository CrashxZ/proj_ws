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


class reachTarget(object):

    def __init__(self):
	self.target = ""
	self.position = ""
        self.delta = ""
	self.aligntarget_x = 0.5
	self.aligntarget_y = 0.5
	self.probabilityThreshlold = 0.50
        #Subscriber to get Target Position
        self._hunter = rospy.Subscriber('/drone_hunter_topic', String, self.get_target_location)
	
        #Publisher to send delta values to the drone for flying
        self.setpoint = rospy.Publisher('/dji_sdk/flight_control_setpoint_ENUvelocity_yawrate', Joy, queue_size=0)
        self.goToTarget()


    # Subscriber callback for Target Position Information
    def get_target_location(self, msg):
	#rospy.loginfo(msg)
	if msg.data != "-999":
		self.target = literal_eval(msg.data);
	
		#rospy.loginfo(self.target )
		#rospy.loginfo(self.target["x"] )
		


    #Function to Publish data to the publisher
    def goToTarget(self):
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		if(self.target !=""):
		    	while (self.target["prob"] > self.probabilityThreshlold):
				#relative distance calculation
				#right movement
				movement_offset = Joy()
				while(self.target["x"] + (self.target["w"]/2) > self.aligntarget_x):
					movement_offset.axes = [0.5, 0, 0] 
					#self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)

				#left movement
				movement_offset = Joy()
				while(self.target["x"] + (self.target["w"]/2) < self.aligntarget_x):
					movement_offset.axes = [-0.5, 0, 0] 
					#self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)

				#front movement
				movement_offset = Joy()
				while(self.target["y"] + (self.target["h"]/2) < self.aligntarget_y):
					movement_offset.axes = [0, 0.5, 0] 
					#self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)
				#back movement
				movement_offset = Joy()
				while(self.target["y"] + (self.target["h"]/2) > self.aligntarget_y):
					movement_offset.axes = [0, -0.5, 0] 
					#self.setpoint.publish(movement_offset)
					rospy.loginfo(movement_offset.axes)
		rate.sleep();
    


if __name__ == "__main__":
    rospy.init_node('reach_target', log_level=rospy.INFO)
    go_home_object = reachTarget()
    rospy.spin()
