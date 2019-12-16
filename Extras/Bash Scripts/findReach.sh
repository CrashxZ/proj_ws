
#!/bin/bash

echo "Starting Detection!"

gnome-terminal -- bash -c "sleep 10;cd $HOME/hunter/droneHunter/build;./DroneHunter;exec bash"

echo "Starting Reach Target!"

cd $HOME/proj_ws
source devel/setup.bash
rosrun homecomming reachTarget.py


$SHELL
