#!/usr/bin/env python3

import os
import yaml

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def dict2string(d):
    if isinstance(d, dict):
        return [{str(k) + "/" + list(s.keys())[0] : list(s.values())[0]} if isinstance(s, dict) else {str(k) : s} 
                for (k, v) in d.items() for s in dict2string(v)]
    else:
        return [d]

def generate_launch_description():

    node_name = 'apriltag_node'

    param_dir = LaunchConfiguration(
        "param_dir",
        default=os.path.join(
            get_package_share_directory('apriltag_ros'),
            'cfg',
            'px4.yaml'
        ) 
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'param_dir',
            default_value=param_dir,
            description="Full path of parameter file"
        ),
        Node(
            package='apriltag_ros',
            executable=node_name,
            name=node_name,
            namespace=node_name,
            output='screen',
            parameters = [param_dir],
            remappings = [("image_rect", "/typhoon_h480/flow_camera/image_raw"),
                          ("camera_info", "/typhoon_h480/flow_camera/camera_info")]
            # prefix=['gdb -ex=r --args'],
        ),
    ])