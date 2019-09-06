#! /usr/bin/env python
import rospy
import numpy as np
import json
import matplotlib.pyplot as plt
import importlib
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
import time


class GoHome(object):

    def __init__(self):
        self._currentPoint = PointStamped()
        self._coordinate = ""
        self.pathData = ""
        self.pathArray = []
        self.delta =""
        self._point_sub = rospy.Subscriber('/dji_sdk/local_position', PointStamped, self.sub_callback)

    def sub_callback(self, msg):
        self._coordinate = {
            "x": msg.point.x,
            "y": msg.point.y,
            "z": msg.point.z
        }

    def loadJSON(self):
        with open("/src/local_path/data/coordinates.json", "r") as file:
           self.pathData = json.load(file)
            for point in self.pathData:
                rospy.loginfo(point)
                self.pathArray.append(point)



    def deltaQ(self):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            self.delta= {
                "x" : (self._coordinate["x"] - self.pathArray["x"])

            }


        

if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO)
    go_home_object = GoHome()
    # rospy.spin()