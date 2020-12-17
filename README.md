IMU tools for ROS
===================================

Overview
-----------------------------------

IMU-related filters and visualizers. The stack contains:

 * `imu_filter_madgwick`: a filter which fuses angular velocities,
accelerations, and (optionally) magnetic readings from a generic IMU 
device into an orientation. Based on the work of [1].

 * `imu_complementary_filter`: a filter which fuses angular velocities,
accelerations, and (optionally) magnetic readings from a generic IMU 
device into an orientation quaternion using a novel approach based on a complementary fusion. Based on the work of [2].

 * `rviz_imu_plugin` a plugin for rviz which displays `sensor_msgs::Imu`
messages

Installing
-----------------------------------

### From source ###

[Create a catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
(e.g., `~/ros-hydro-ws/`) and source the `devel/setup.bash` file.

Make sure you have git installed:

    sudo apt-get install git-core

Download the stack from our repository into your catkin workspace (e.g.,
`ros-hydro-ws/src`; use the proper branch for your distro, e.g., `groovy`,
`hydro`...):

    git clone -b <distro> https://github.com/ccny-ros-pkg/imu_tools.git

Install any dependencies using [rosdep](http://www.ros.org/wiki/rosdep).

    rosdep install imu_tools

Compile the stack:

    cd ~/ros-hydro-ws
    catkin_make

More info
-----------------------------------

http://wiki.ros.org/imu_tools

License
-----------------------------------

 * `imu_filter_madgwick`: currently licensed as GPL, following the original implementation
 
 * `imu_complementary_filter`: BSD

 * `rviz_imu_plugin`: BSD


Usage
-----------------------------------


`
rosparam set use_sim_time true
`

`
rosrun imu_filter_madgwick imu_filter_node _publish_debug_topics:=true
`

`
rosbag play ~/catkin_ws/src/imu_tools/imu_filter_madgwick/sample/ardrone_imu.bag /ardrone/imu:=/imu/data_raw /ardrone/mag:=/imu/mag
`

`
rosbag play --clock /mnt/c/bag/gps-imu-2020-12-14-campus-12-40.bag /gps/duro/imu:=/imu/data_raw /gps/duro/mag:=/imu/mag
`

`
rosrun imu_filter_madgwick tf_to_topic.py
`


References
-----------------------------------
 [1] http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/

 [2] http://www.mdpi.com/1424-8220/15/8/19302
