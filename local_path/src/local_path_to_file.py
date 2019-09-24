#! /usr/bin/env python
import rospy
import numpy as np
import json
import matplotlib.pyplot as plt
import importlib
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
import time
class SavePath(object):

    def __init__(self):
        self._currentPoint = PointStamped()
        self._coordinate = ""
        #Subscriber to get local position from the drone.
        self._point_sub = rospy.Subscriber('/dji_sdk/local_position', PointStamped, self.sub_callback)
        self.saveJSON()
    # Subscriber callback function to save the coordinate data from local position.
    def sub_callback(self, msg):
        self._coordinate = {
            "x": msg.point.x,
            "y": msg.point.y,
            "z": msg.point.z
            }
        
    #To save data to JSON File
    def saveJSON(self):
        rate = rospy.Rate(20)
        rospy.loginfo("Start to write all points.")
        with open("coordinates.json", "w") as file:
            while not rospy.is_shutdown():
                if(self._coordinate != ""):
                    json.dump(self._coordinate, file)
                    file.write("\n")
                    rospy.loginfo(self._coordinate)
                rate.sleep()
    #Testing function
    def loadJSON(self):
        with open("coordinates.json", "r") as file:
            pathData = json.load(file)


if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO)
    save_spots_object = SavePath()
    # rospy.spin()
