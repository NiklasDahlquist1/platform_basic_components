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

    robot_name = "test" #os.getenv('USER')
    


    ld = LaunchDescription()

    #i = 80085



    # i = int(hashlib.sha256(robot_name.encode('utf-8')).hexdigest(), 16) % 10**10 # hash the namespace string to get a 'unique' id integer (10 digits here) 

    
    ld.add_entity(Node(
        namespace=robot_name,
        package='behaviors',
        executable='behaviors_test_node',
        # name='bt_test', # Dont use names since multiple nodes are launched from this process...
        output='screen',
        remappings=[ # (old_topic , new_topic),
        ],
        #parameters=[params],
        parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],
    ))

    
    ld.add_entity(Node(
        namespace=robot_name,
        package='px4_position_control',
        executable='px4_position_control_node',
        name='px4_controller',
        output='screen',
        remappings=[ # (old_topic , new_topic),
        ],
        #parameters=[params],
        parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],
    ))





    return ld
