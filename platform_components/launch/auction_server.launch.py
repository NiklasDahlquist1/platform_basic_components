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

    auction_namespace = "/auction_server"



    ld = LaunchDescription()

    #i = 80085



    # i = int(hashlib.sha256(robot_name.encode('utf-8')).hexdigest(), 16) % 10**10 # hash the namespace string to get a 'unique' id integer (10 digits here) 

    ld.add_entity(Node(
        package='auction_server',
        namespace=auction_namespace,
        executable='auction_server_node',
        name='auction_server_node',
        output='screen',
        #remappings=[ # (old_topic , new_topic),
        #    ('output_telemetry', 'output_telemetry'),
        #],
        parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],
    ))


    ld.add_entity(Node(
        package='auction_task_adder',
        namespace=auction_namespace,
        executable='auction_task_adder_node',
        name='auction_task_adder',
        output='screen',
        #remappings=[ # (old_topic , new_topic),
        #    ('output_telemetry', 'output_telemetry'),
        #],
        # parameters=[get_package_share_directory('platform_components')+"/platform_params.yaml"],
    ))


    # ld.add_entity(Node(
    #     package='auction_task_visualizer',
    #     namespace=auction_namespace,
    #     executable='auction_task_visualizer_node',
    #     name='auction_task_visualizer',
    #     output='screen',
    # ))






    return ld
