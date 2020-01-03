#!/bin/bash
sudo usermod -a -G dialout $USER

# ROS Master - UAV Jetson Xavier
# HOSt - 192.168.188.8
export ROS_HOSTNAME=192.168.188.8
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8


export DISPLAY=:0.0

#takeoff
cd $HOME/proj_ws
./takeoff.sh

#send GPS Coordinates
gnome-terminal -- bash -c "cd $HOME/proj_ws;./target_GPS.sh;exec bash"

cd $HOME/dji_sdk
source devel/setup.bash
$speed=rosservice call "/dji_sdk/mission_waypoint_getSpeed {}"
#check speed of the drone (idling speed), waypoint reached! set speed while calling superbashscript(./exmachina.sh)
if $speed<=0.1
then
    gnome-terminal -- bash -c "cd $HOME/proj_ws;./findReach.sh;exec bash"