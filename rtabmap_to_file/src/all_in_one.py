#! /usr/bin/env python
import rospy
import json
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point
import time


class SaveRtabMap(object):
    def __init__(self):

        self._currentPath = ""
        self._currentOdom = ""
        self._odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self._path_sub = rospy.Subscriber('/rtabmap/mapPath', Path, self.path_callback)
        self.write_to_file()

    def odom_callback(self, msg):

        _pose = msg.pose.pose
        self._currentOdom = {"x": _pose.position.x,
                             "y": _pose.position.y,
                             "z": _pose.position.z}

    def path_callback(self, msg):

        _temp = msg.poses[-1]
        self._currentPath = {"x": _temp.pose.position.x,
                             "y": _temp.pose.position.y,
                             "z": _temp.pose.position.z}

    # To write all data from RtabMap
    def write_to_file(self):

        rospy.loginfo("All data from RtabMap.")
        rate = rospy.Rate(5)
        with open("RtabMap_Odom.json", "w") as odom, open("rtabMap_path.json", "w") as path:
            while not rospy.is_shutdown():
                if self._currentOdom != "":
                    rospy.loginfo(self._currentOdom)
                    json.dump(self._currentOdom, odom)
                    odom.write("\n")
                if self._currentPath != "":
                    rospy.loginfo(self._currentPath)
                    json.dump(self._currentPath, path)
                    path.write("\n")
                rate.sleep()

        rospy.loginfo("Finished")


if __name__ == "__main__":
    rospy.init_node('all_in_one', log_level=rospy.INFO)
    save_spots_object = SaveRtabMap()
    rospy.spin()
