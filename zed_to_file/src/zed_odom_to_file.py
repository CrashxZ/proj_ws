#! /usr/bin/env python
import rospy
import json
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point
import time


class SavePoses(object):
    def __init__(self):

        self._pose = Pose()
        self._currentpose = ""
        self._pose_sub = rospy.Subscriber('/zed/zed_node/odom', Odometry, self.sub_callback)
        self.write_to_file()

    def sub_callback(self, msg):

        self._pose = msg.pose.pose
        self._currentpose = {"x": self._pose.position.x,
                             "y": self._pose.position.y,
                             "z": self._pose.position.z}

    # To write Odom data from RtabMap
    def write_to_file(self):

        rospy.loginfo("Writing Odometry data from Zed SDK.")

        rate = rospy.Rate(5)
        with open("ZED_Odom.json", "w") as file:
            while not rospy.is_shutdown():
                if (self._currentpose != ""):
                    rospy.loginfo(self._currentpose)
                    json.dump(self._currentpose, file)
                    file.write("\n")
                rate.sleep()

        rospy.loginfo("Written all Odometry data to ZED_Odom.json file")


if __name__ == "__main__":
    rospy.init_node('zed_odom_to_file', log_level=rospy.INFO)
    save_spots_object = SavePoses()
    rospy.spin()
