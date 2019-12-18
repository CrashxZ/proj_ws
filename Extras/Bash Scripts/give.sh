#!/bin/bash

echo "Setting Up!"
# ROS Master - UAV Jetson Xavier
# HOSt - 192.168.188.8
export ROS_HOSTNAME=192.168.188.8
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8

# shellcheck disable=SC2164
cd $HOME/dji_sdk
source devel/setup.bash

echo "Setting LocalPosition!"
rosservice call /dji_sdk/set_local_pos_ref {}

echo "Giving control to SDK (Autonomous Control)!"
rosservice call /dji_sdk/sdk_control_authority "control_enable: 1" 


$SHELL
