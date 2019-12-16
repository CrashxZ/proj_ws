
#!/bin/bash

echo "Starting to trace Path!"


cd $HOME/proj_ws
source devel/setup.bash
rosrun homecomming go_home.py


$SHELL
