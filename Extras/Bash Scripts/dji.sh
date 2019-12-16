
#!/bin/bash
sudo usermod -a -G dialout $USER
echo "Starting DJI SDK!"



cd $HOME/dji_sdk
source devel/setup.bash
roslaunch dji_sdk sdk.launch


$SHELL
