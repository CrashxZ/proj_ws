cd $HOME/dji_sdk
source devel/setup.bash

rosservice call /dji_sdk/mission_waypoint_upload {
velocity_range
idle_velocity
action_on_finish
mission_exec_times
yaw_mode
trace_mode
action_on_rc_lost
gimbal_pitch_mode
MissionWaypoint[] mission_waypoint } #инициализация загрузки GPS #точки c указанными параметрами. Параметры целевой точки задаются в #ручную

#инициализация команды вылета в указанную GPS точку
rosservice call /dji_sdk/mission_waypoint_action "action: 0"

gnome-terminal -- bash -c "cd $HOME/orb_slam_path_publisher;./ path_to_file;exec bash"

$SHELL
