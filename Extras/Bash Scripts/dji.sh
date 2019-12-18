#!/bin/bash
sudo usermod -a -G dialout $USER

# ROS Master - UAV Jetson Xavier
# HOSt - 192.168.188.8
export ROS_HOSTNAME=192.168.188.8
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8

echo "Starting DJI SDK!"

# shellcheck disable=SC2164
cd $HOME/dji_sdk
source devel/setup.bash
roslaunch dji_sdk sdk.launch
$SHELL
