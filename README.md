Source files for autonomous trajectory control and navigation using ROS and DJI Onboard-SDK.

homecomming/gohome.py - trajectory control using "coordiates.json"

Scripts for recording tragectory macro - local_path 


Steps to Use:
1. catkin_make or catkin_make_isolated for the workspace.
2. cd <workspace_name>/src 
3. git clone <repository_src>

Install DJI Onboard-SDK and SDK and use "sudo usermod -a -G dialout $USER" and check the correct baudrate and the TX/RX connections.

Extras:
Bash Scripts and UART Scripts.
Run "sudo usermod tty -a -G $USER" to get access to tty.
Run chmod +x *.sh : on the bash scripts
