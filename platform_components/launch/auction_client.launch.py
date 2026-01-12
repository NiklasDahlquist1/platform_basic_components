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


    # robot_name = "panda0" #os.getenv('USER')
    robot_name = LaunchConfiguration("robot_name") #

    # robot_namespace = "test" #os.getenv('USER')
    auction_namespace = "/auction_server"




    #i = 80085



    # i = int(hashlib.sha256(robot_name.encode('utf-8')).hexdigest(), 16) % 10**10 # hash the namespace string to get a 'unique' id integer (10 digits here) 

    ld.add_entity(Node(
        package='auction_client',
        namespace=robot_name,
        executable='auction_client_test_node',
        name='auction_client',
        output='screen',
        remappings=[ # (old_topic , new_topic),
            ('add_bid', auction_namespace + '/add_bid'),
            ('confirm_task_finished', auction_namespace + '/confirm_task_finished'),
            ('auction_available', auction_namespace + '/auction_available'),
            ('task_allocated', auction_namespace + '/task_allocated'),
            ('not_allocated_to_task', auction_namespace + '/not_allocated_to_task'),
            ('client_task_finished', 'client_task_finished'),
            ('client_task_allocated', 'client_task_allocated'),                
        ],
        parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],

        #parameters=[get_package_share_directory('auction_server')+"/params.yaml"],
    ))
    


    ld.add_entity(Node(
        package='cost_calculator',
        namespace=robot_name,
        executable='cost_calculator_node',
        name='cost_calculator',
        output='screen',
        #remappings=[ # (old_topic , new_topic),
        #    ('odometry', "/" + robot + '/odometry'),
        #    ('reference_pose', "/" + robot + '/reference_pose'),
        #    ('cmd_vel', "/" + robot + '/cmd_vel'),
        #],
        #parameters=[get_package_share_directory('auction_server')+"/params.yaml"],
    ))











    return ld
