from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
# from ament_index_python import get_package_share_directory
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, TextSubstitution, PythonExpression

from launch_ros.substitutions import FindPackageShare


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


    config_path = PathJoinSubstitution([
        FindPackageShare("platform_components"),
        PythonExpression(["'", robot_name, "_domain_bridge.yaml", "'"])
    ])
    # print(config_path)




    # i = int(hashlib.sha256(robot_name.encode('utf-8')).hexdigest(), 16) % 10**10 # hash the namespace string to get a 'unique' id integer (10 digits here) 


    ld.add_entity(Node(
        namespace=robot_name,
        package='domain_bridge',
        executable='domain_bridge',
        # name='domain_bridge',
        output='screen',
        remappings=[ # (old_topic , new_topic),
        ],
        # parameters=[get_package_share_directory('platform_components')+"/{}_domain_bridge.yaml".format(robot_name)],
        arguments=[config_path],
    ))

    






    return ld


