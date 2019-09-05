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
        self._point = PointStamped()
        self._currentPoint = PointStamped()
        self.coordinate = ""
        self._point_sub = rospy.Subscriber('/dji_sdk/local_position', PointStamped, self.sub_callback)
        #self.write_to_file()
        self.saveJSON()

    def sub_callback(self, msg):
        self.coordinate = {
            "x": msg.point.x,
            "y": msg.point.y,
            "z": msg.point.z
            }
        
        rospy.loginfo(self.coordinate)

    def saveJSON(self):
        rate = rospy.Rate(20)
        with open("coordinates.json", "w") as file:
            while not rospy.is_shutdown():
                json.dump(self.coordinate, file)
                file.write("\n")
                rospy.loginfo(self.coordinate)
                rate.sleep()

    def loadJSON(self):
        with open("coordinates.json", "r") as file:
            pathData = json.load(file)

        # for coordinate in pathData:
        #     print(coordinate)

    def write_to_file(self):
        rospy.loginfo("Start to write all poses from RtabMap.")
        # rospy.loginfo(self._pose)

        # rospy.loginfo(self._currentPoint)
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
    # rospy.spin()
