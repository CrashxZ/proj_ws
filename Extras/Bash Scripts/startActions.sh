#!/bin/bash

echo "Starting Services!"




sudo usermod -a -G dialout nvidia


gnome-terminal -- bash -c "sleep 40;cd $HOME/dji_sdk;source devel/setup.bash;rosservice call /dji_sdk/activation {};rosservice call /dji_sdk/set_local_pos_ref {};exec bash"


gnome-terminal -- bash -c "sleep 45;cd $HOME/proj_ws;source devel/setup.bash;rosrun local_path local_path_to_file.py;exec bash"

gnome-terminal -- bash -c "sleep 45;cd $HOME/proj_ws;source devel/setup.bash;rosrun rtabmap_to_file all_in_one.py;exec bash"

gnome-terminal -- bash -c "sleep 45;cd $HOME/proj_ws;source devel/setup.bash;rosrun zed_to_file one_for_all.py;exec bash"

cd $HOME/dji_sdk
source devel/setup.bash
roslaunch dji_sdk sdk.launch


$SHELL
