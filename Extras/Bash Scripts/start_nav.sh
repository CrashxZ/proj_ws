#!/bin/bash
# ROS Master - NUC
# HOST - 10.0.0.1 Ethernet 
export ROS_HOSTNAME=10.0.0.1
export ROS_MASTER_URI=http://10.0.0.1:11311/
export ROS_MASTER_IP=10.0.0.1
gnome-terminal -- bash -c "cd $HOME/velodyne_ws;
source devel/setup.bash; roslaunch velodyne_poincloud VLP16_points.launch;
exec bash"

gnome-terminal -- bash -c "export ROS_HOSTNAME=10.0.0.1;export ROS_MASTER_URI=http://10.0.0.1:11311/;export ROS_MASTER_IP=10.0.0.1;sleep 5; roslaunch usb_cam usb_cam_test.launch; exec bash" #инициализация драйвера видеокамеры для получения входнго потока визуальной информации

gnome-terminal -- bash -c "export ROS_HOSTNAME=10.0.0.1;export ROS_MASTER_URI=http://10.0.0.1:11311/;export ROS_MASTER_IP=10.0.0.1;sleep 10;cd $HOME/orb_slam;source devel/setup.bash;roslaunch orb_slam_2_ros  my_cam.launch;exec bash" #инициализация монокуляного модуля ORB_SLAM2

gnome-terminal -- bash -c "export ROS_HOSTNAME=10.0.0.1;export ROS_MASTER_URI=http://10.0.0.1:11311/;export ROS_MASTER_IP=10.0.0.1;sleep 10;cd $HOME/orb_slam_path_publisher; ./path_publisher;exec bash" #инициализация модуля построения пройденного пути

gnome-terminal -- bash -c "export ROS_HOSTNAME=10.0.0.1;export ROS_MASTER_URI=http://10.0.0.1:11311/;export ROS_MASTER_IP=10.0.0.1;./lego_loam_start.sh; exec bash"  # инициализация bash-#скрипта модуля построения карты на основе #данных облака #точек лидара средствами #пакета LeGO-LOAM

cd $HOME/Octomap
roslaunch octomap_mapper.launch #инициализация модуля построения карты на основе данных #облака точек лидара и одометрии orb_slam2 на исходном языке


$SHELL


