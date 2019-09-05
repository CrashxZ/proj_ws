#! /usr/bin/env python
import rospy
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped
import time
 
 
class SavePoses(object):
    def __init__(self):
        
        self._pose = Pose()
        self._pose_sub = rospy.Subscriber('/odom', Odometry , self.sub_callback)
        self.write_to_file()
 
    def sub_callback(self, msg):
        
        self._pose = msg.pose.pose
    
    def write_to_file(self):
        
        rospy.loginfo("Professor Dmitry, Hello!")
        rospy.loginfo("Start to write all poses from RtabMap.")
        rate = rospy.Rate(5)
	with open('poses.txt', 'w') as file:
            
            while self._pose:
                    
		file.write(str(self._pose.position.x) + ' ' + str(self._pose.position.y) + ' ' + str(self._pose.position.z) + '\n')
                rate.sleep()
                    
        rospy.loginfo("Written all Poses to poses.txt file")
        
 
 
if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO) 
    save_spots_object = SavePoses()
    rospy.spin() 
