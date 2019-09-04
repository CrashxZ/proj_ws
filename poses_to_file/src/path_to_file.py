#! /usr/bin/env python
import rospy
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point
import time
 
class SavePath(object):

    p1 = np.array([0,0,0])
    p2 = np.array([0,0,0])
    def __init__(self):
        self._path = Path()
        self._pose = PoseStamped()
	self._currentposition =  ""
	self._deltaQ = ""
        self._path_sub = rospy.Subscriber('/rtabmap/mapPath', Path , self.sub_callback)
        self.write_to_file()
	#rospy.loginfo(type(self._pose))
	#rospy.loginfo(type(self._path))
	#rospy.loginfo(type(self._path_sub))

 
 
    def sub_callback(self, msg):
	
	p1 = np.array([msg.poses[-1].pose.position.x, msg.poses[-1].pose.position.y, msg.poses[-1].pose.position.z])
    	p2 = np.array([msg.poses[-2].pose.position.x, msg.poses[-2].pose.position.y, msg.poses[-2].pose.position.z])
	deltaQ= p1-p2

	self._temp = msg.poses[-1]
	self._pose = str(self._temp.pose.position.x) + ' ' + str(self._temp.pose.position.y) + ' ' + str(self._temp.pose.position.z)
	self._currentposition = np.array([self._temp.pose.position.x,self._temp.pose.position.y,self._temp.pose.position.z])

	rospy.loginfo(self._currentposition)
	rospy.loginfo(" Delta Q =" +str(deltaQ))
	

	
    
    def write_to_file(self):
        
        rospy.loginfo("Start to write all poses from RtabMap.")
	#rospy.loginfo(self._pose)
	
	

        rate = rospy.Rate(20)
	with open('poses_from_path.txt', 'w') as file:
            
            while not rospy.is_shutdown():    
		    file.write(str(self._currentposition) + " Delta Q =" + str(self._currentposition) + ' \n')
                rate.sleep()
                    
        rospy.loginfo("Written all Poses to poses.txt file")
	
        
 
 
if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO) 
    save_spots_object = SavePath()
    #rospy.spin() 



    


