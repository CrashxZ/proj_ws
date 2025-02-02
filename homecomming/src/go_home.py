#! /usr/bin/env python
import rospy
import numpy as np
import json
import importlib
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
from sensor_msgs.msg import Joy
import time
import os


class GoHome(object):

    def __init__(self):
        #Values for P Control System
        self.error = 0.2
        self.pval = 0.5
        #Initilization of Variables
        self._currentPoint = PointStamped()
        self._coordinate = ""
        self.pathData = ""
        self.pathArray = []
        self.delta = ""
        #Subscriber to get Local Position
        self._point_sub = rospy.Subscriber('/dji_sdk/local_position', PointStamped, self.sub_callback)
        #Publisher to send delta values to the drone for flying
        self.setpoint = rospy.Publisher('/dji_sdk/flight_control_setpoint_ENUvelocity_yawrate', Joy, queue_size=0)
        self.rc = rospy.Subscriber('/dji_sdk/rc', Joy, self.manual_override)
        self.loadJSON()
        self.deltaQ()

    # Subscriber callback function to save the coordinate data from local position.
    def sub_callback(self, msg):
        self._coordinate = {
            "x": msg.point.x,
            "y": msg.point.y,
            "z": msg.point.z
        }
        # rospy.loginfo(self._coordinate)
        
    # Subscriber callback to listen to rc channels
    def manual_override(self, msg):
	#rospy.loginfo(msg.axes[4])
	if msg.axes[4] != 1:
                self._coordinate = ""
                rospy.logfatal("Manual Override")
		rospy.signal_shutdown("Manual Override")
        
    #Function to read the JSON information from file (Previously saved by local_path packege)
    def loadJSON(self):
        with open("coordinates.json", "r") as file:
            self.pathData = file.readlines()
            rospy.loginfo("part1")
            for point in self.pathData:
                point = json.loads(point)
                self.pathArray.append(point)
                # rospy.loginfo(point)
        # rospy.loginfo(self.pathArray)
        rospy.loginfo("Finished reading file")

    #Function to Publish data to the publisher
    def deltaQ(self):
        rate = rospy.Rate(1)
        counter = 0
        landing_flag = 0
        while not rospy.is_shutdown():
            while not self._coordinate == "":
                #calculating delta for each point implimenting the P Control System
                if counter < len(self.pathArray):
                    self.delta = {
                        "x": ((self.pathArray[counter]["x"] - self._coordinate["x"]) * self.pval),
                        "y": ((self.pathArray[counter]["y"] - self._coordinate["y"]) * self.pval),
                        "z": ((self.pathArray[counter]["z"] - self._coordinate["z"]) * 0.1)
                    }
                    # rospy.loginfo(self.delta)
                    #converting messages to Joy class for sending
                    temp = Joy()
                    #temp.header.stamp = rospy.Time.now()
                    temp.axes = [self.delta["x"], self.delta["y"], self.delta["z"]]
                    #Publish messages to the topic
                    self.setpoint.publish(temp)
                    rospy.loginfo(counter)
                    #checking distance from local position and moving to the next point on the list if the point is reached
                    if abs(self.delta["x"]) < self.error and abs(self.delta["y"]) < self.error and abs(self.delta["z"]) < self.error:
                        counter += 1
                        # self.setpoint.publish(temp)
                        rospy.loginfo("Moving On")
                        if counter >= len(self.pathArray):
                            #altitude adjustment to place the captured target on the ground
                            if landing_flag == 1:
                                os.system("sleep 5;./land.sh")
                                break
                            if landing_flag == 0:
                                self.pathArray.append('{"y": 0, "x": 0, "z": 5}')
                                self.pathArray.append('{"y": 1, "x": 0, "z": 5}')
                                landing_flag == 1



            rate.sleep()


if __name__ == "__main__":
    rospy.init_node('go_home', log_level=rospy.INFO)
    go_home_object = GoHome()
    # rospy.spin()
