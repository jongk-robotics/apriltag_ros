#!/bin/bash
set -e



SCRIPT_DIR=$0
if [[ ${SCRIPT_DIR:0:1} != '/' ]]; then
  SCRIPT_DIR=$(dirname $(realpath -s "$PWD/$0"))
fi

source /opt/ros/$ROS_DISTRO/setup.bash

# setup the required path variables
ROS_REPO_DIR=$(cd "$(dirname "$SCRIPT_DIR")" && pwd)
ROS_WS_SRC_DIR=$(cd "$(dirname "$ROS_REPO_DIR")" && pwd)
ROS_WS_DIR=$(cd "$(dirname "$ROS_WS_SRC_DIR")" && pwd)

# build px4_ros_com package
cd $ROS_WS_DIR && colcon build --cmake-args -DCMAKE_BUILD_TYPE=RELWITHDEBINFO --symlink-install --packages-select apriltag_ros

# source the ROS2 workspace environment so to have it ready to use
source $ROS_WS_DIR/install/setup.bash

printf $ROS_WS_DIR
printf "\nperching node ready...\n\n"
