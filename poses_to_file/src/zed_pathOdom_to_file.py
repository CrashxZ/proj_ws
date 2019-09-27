#! /usr/bin/env python
import rospy
import json
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point
import time
 
class SavePath(object):

    def __init__(self):

	self._currentposition =  ""
        self._path_sub = rospy.Subscriber('/zed/zed_node/path_odom', Path , self.sub_callback)
        self.write_to_file()
 
    def sub_callback(self, msg):
	
	self._temp = msg.poses[-1]
	self._currentposition = {"x": self._temp.pose.position.x, 
				 "y": self._temp.pose.position.y, 
			         "z": self._temp.pose.position.z}

	rospy.loginfo(self._currentposition)
	

	
    
    def write_to_file(self):
        
        rospy.loginfo("Writing Odometry Path from Zed SDK.")
	
        rate = rospy.Rate(20)
	with open("Zed_Path_Odom.json", "w") as file:
            while not rospy.is_shutdown():
                if (self._currentposition != ""):
			json.dump(self._currentposition, file)
			file.write("\n")
            	rate.sleep()
                    
        rospy.loginfo("Written Path to Zed_Path_Odom.json file")
	
        
 
 
if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO) 
    save_spots_object = SavePath()
    #rospy.spin() 
