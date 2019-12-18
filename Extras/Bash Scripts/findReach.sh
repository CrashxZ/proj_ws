#!/bin/bash
# ROS Master - UAV Jetson Xavier
# HOSt - 192.168.188.8
export ROS_HOSTNAME=192.168.188.8
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8


echo "Starting Detection!"
gnome-terminal -- bash -c "sleep 10;cd $HOME/hunter/droneHunter/build;./DroneHunter;exec bash"
echo "Starting Reach Target!"

# shellcheck disable=SC2164
cd $HOME/proj_ws
source devel/setup.bash
rosrun homecomming reachTarget.py
$SHELL
