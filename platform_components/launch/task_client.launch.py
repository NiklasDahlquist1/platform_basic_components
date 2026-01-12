from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from ament_index_python import get_package_share_directory

import os
#from glob import glob
from launch_ros.parameter_descriptions import Parameter


import hashlib



def generate_launch_description():

    ld = LaunchDescription()
    robot_name_arg = DeclareLaunchArgument(
        "robot_name",
        default_value="test_name",
        description="Argument for custom robot name."
    )
    ld.add_entity(robot_name_arg)

    # robot_name = "test" #os.getenv('USER')
    robot_name = LaunchConfiguration("robot_name") #



    ld = LaunchDescription()

    #i = 80085



    # i = int(hashlib.sha256(robot_name.encode('utf-8')).hexdigest(), 16) % 10**10 # hash the namespace string to get a 'unique' id integer (10 digits here) 

    
    ld.add_entity(Node(
        namespace=robot_name,
        package='task_client',
        executable='task_client_px4_node',
        name='task_client',
        output='screen',
        remappings=[ # (old_topic , new_topic),
        ],
        #parameters=[params],
        parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],
    ))


    ld.add_entity(Node(
        namespace=robot_name,
        package='px4_position_control',
        executable='px4_position_control_goto_setpoint_node',
        name='px4_controller',
        output='screen',
        remappings=[ # (old_topic , new_topic),
        ],
        #parameters=[params],
        parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],
    ))





    return ld
