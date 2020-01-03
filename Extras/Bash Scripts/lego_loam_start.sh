#!/bin/bash
gnome-terminal -- bash -c "cd $HOME/xsens_ws;source devel/setup.bash; roslaunch xsens_mti_driver xsens_mti_node.launch;exec bash" #инициализация #драйвера IMU Xsens MTI

cd $HOME/loam_ws
source devel/setup.bash #указание скрипта, содержащего все символьные ссылки для #запуска модуля
roslaunch lego_loam_bor run.launch #инициализация модуля построения карты на #основе данных облака точек лидара средствами пакета LeGO-LOAM
