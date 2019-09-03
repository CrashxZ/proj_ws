#! /usr/bin/env python
import rospy
import numpy as np
import matplotlib.pyplot as plt
import importlib 
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
import time
 
class SavePath(object):

    p1 = np.array([0,0,0])
    p2 = np.array([0,0,0])
    
    def __init__(self):
        self._point = PointStamped()
        self._currentPoint = PointStamped()
        self._point_sub = rospy.Subscriber('/dji_sdk/local_position', PointStamped, self.sub_callback)
        self.write_to_file()




 
 
    def sub_callback(self, msg):

        self._point = [msg.point.x,msg.point.y,msg.point.z]
        #rospy.loginfo(self._point)


	
    
    def write_to_file(self):
        
        rospy.loginfo("Start to write all poses from RtabMap.")
	    #rospy.loginfo(self._pose)
        
        #rospy.loginfo(self._currentPoint)
        rate = rospy.Rate(20)
        with open('localPoseStamped.txt', 'w') as file:
            while not rospy.is_shutdown():
                file.write(str(self._point) + ' \n')
                rospy.loginfo(self._point)
                rate.sleep()
        rospy.loginfo("Written all Poses to poses.txt file")



	
	


	
        
 
 
if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO) 
    save_spots_object = SavePath()
    #rospy.spin() 



    


