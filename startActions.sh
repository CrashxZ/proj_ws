#!/bin/bash

echo "Starting Services!"

cd /dji_sdk
source devel/setup.bash
roslaunch dji_sdk sdk.launch

gnome-terminal -e "bash -c cd /dji_sdk;source devel/setup.bash;rosservice call /dji_sdk/activation {};rosservice call /dji_sdk/set_local_pos_ref {};bash"
echo "Drone activated and local position set!"

gnome-terminal -e "bash -c cd /proj_ws;source devel/setup.bash;roslaunch local_path local_path_to_file.py.py;bash"
echo "Dji SDK Local position recording!"
gnome-terminal -e "bash -c cd /proj_ws;source devel/setup.bash;roslaunch rtabmap_to_file all_in_one.py;bash"

gnome-terminal -e "bash -c cd /proj_ws;source devel/setup.bash;roslaunch zed_to_file one_for_all.py;bash"

$SHELL