
#!/bin/bash

echo "Setting Up!"

cd $HOME/dji_sdk
source devel/setup.bash
rosservice call /dji_sdk/activation {}
rosservice call /dji_sdk/set_local_pos_ref {}


$SHELL
