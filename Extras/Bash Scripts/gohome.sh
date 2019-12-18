#!/bin/bash
# ROS Master - UAV Jetson Xavier
# HOSt - 192.168.188.8
export ROS_HOSTNAME=192.168.188.8
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8

echo "Starting to trace Path!"

# shellcheck disable=SC2164
cd $HOME/proj_ws
source devel/setup.bash
rosrun homecomming go_home.py
$SHELL
