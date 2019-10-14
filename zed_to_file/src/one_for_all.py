#! /usr/bin/env python
import rospy
import json
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point
import time


class zedData(object):
    def __init__(self):

        self._currentOdom = ""
        self._currentPath = ""
        self._currentPathOdom = ""
        self._odom_sub = rospy.Subscriber('/zed/zed_node/odom', Odometry, self.odom_callback)
        self._path_sub = rospy.Subscriber('/zed/zed_node/path_map', Path, self.path_callback)
        self._pathOdom_sub = rospy.Subscriber('/zed/zed_node/path_odom', Path, self.pathodom_callback)
        self.write_to_file()

    def odom_callback(self, msg):

        _pose = msg.pose.pose
        self._currentOdom = {"x": _pose.position.x,
                             "y": _pose.position.y,
                             "z": _pose.position.z}

    def path_callback(self, msg):

        _temp = msg.poses[-1]
        self._currentPath = {"x": self._temp.pose.position.x,
                             "y": self._temp.pose.position.y,
                             "z": self._temp.pose.position.z}

    def pathodom_callback(self, msg):

        _temp = msg.poses[-1]
        self._currentPathOdom = {"x": _temp.pose.position.x,
                                 "y": _temp.pose.position.y,
                                 "z": _temp.pose.position.z}

    # To write Odom data from RtabMap
    def write_to_file(self):

        rospy.loginfo("Writing Odometry data from Zed SDK.")

        rate = rospy.Rate(5)
        with open("ZED_Odom.json", "w") as odom, open("Zed_Path.json", "w") as path, open("Zed_Path_Odom.json", "w") as pathodom:
            while not rospy.is_shutdown():
                if self._currentOdom != "":
                    rospy.loginfo(self._currentOdom)
                    json.dump(self._currentOdom, odom)
                    odom.write("\n")
                if self._currentPath != "":
                    json.dump(self._currentPath, path)
                    path.write("\n")
                if self._currentPathOdom != "":
                    json.dump(self._currentPathOdom, pathodom)
                    pathodom.write("\n")
                rate.sleep()

        rospy.loginfo("Written all Odometry data to ZED_Odom.json file")


if __name__ == "__main__":
    rospy.init_node('all_for_one', log_level=rospy.INFO)
    save_spots_object = zedData()
    rospy.spin()