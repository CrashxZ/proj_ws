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
        self.error = 0.001
        self._currentPoint = PointStamped()
        self._coordinate = ""
        self.pathData = ""
        self.pathArray = []
        self.delta = ""
        self._point_sub = rospy.Subscriber('/dji_sdk/local_position', PointStamped, self.sub_callback)
        self.loadJSON()

    def sub_callback(self, msg):
        self._coordinate = {
            "x": msg.point.x,
            "y": msg.point.y,
            "z": msg.point.z
        }

    def loadJSON(self):
        with open("coordinates.json", "r") as file:
            self.pathData = file.readlines()
            rospy.loginfo("part1")
            for point in self.pathData:
                point = eval(point)
                rospy.loginfo(point)
                self.pathArray.append(point)
        rospy.loginfo(self.pathArray)

    def deltaQ(self):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            self.delta = {
                "x": (self._coordinate["x"] - self.pathArray["x"]),
                "y": (self._coordinate["y"] - self.pathArray["y"]),
                "z": (self._coordinate["z"] - self.pathArray["z"])
            }
            # if self.delta["x"] < self.error && self.delta["y"] < self.error && self.delta["z"] < self.error:


if __name__ == "__main__":
    rospy.init_node('spot_recorder', log_level=rospy.INFO)
    go_home_object = GoHome()
    # rospy.spin()
