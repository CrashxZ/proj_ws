
#!/bin/bash

echo "Landing!"

cd $HOME/dji_sdk
source devel/setup.bash
rosservice call /dji_sdk/drone_task_control "task: 6"


$SHELL
