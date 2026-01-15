#!/bin/bash


robot_name="panda1"
agent_id="1"




send_command_to_all_panes_in_window() 
{
    for pane in `tmux list-panes -t $1 -F '#P' | sort`; do
        tmux send-keys -t "$pane" "$2" C-m
    done
}


session="px4_testing"

tmux new-session -d -s $session





window=0
tmux rename-window -t $session:$window 'start_window'

tmux split-window -t 0 -v

tmux split-window -t 0 -h
tmux split-window -t 1 -h
tmux split-window -t 3 -h
tmux split-window -t 4 -h
tmux split-window -t 3 -v



send_command_to_all_panes_in_window 0 "cd ~/ws/ros_ws"
#send_command_to_all_panes_in_window 0 "source /opt/ros/jazzy/setup.bash"
#send_command_to_all_panes_in_window 0 "source ~/ws/ros_ws/install/setup.bash"
# This has been moved to ~/.bashrc for now


tmux send-keys -t 0 "sleep 3 && ros2 launch platform_components auction_client.launch.py robot_name:=$robot_name" #C-m
tmux send-keys -t 1 "ros2 launch platform_components bridge.launch.py robot_name:=$robot_name" #C-m
tmux send-keys -t 2 "ros2 run auction_task_adder client_task_adder_node --ros-args -r __ns:=/$robot_name" #C-m
tmux send-keys -t 3 "ros2 launch platform_components task_client.launch.py robot_name:=$robot_name" #C-m
tmux send-keys -t 4 "MicroXRCEAgent serial --dev /dev/px4_serial -b 921600" #C-m
tmux send-keys -t 5 "ros2 launch platform_components monitoring.launch.py robot_name:=$robot_name" #C-m



# Testing direct task assignments
# tmux send-keys -t 6 "ros2 run auction_task_adder auction_task_adder_node --ros-args -r __ns:=/test_panel -r client_task_allocated:=/$robot_name/client_task_allocated -r clicked_geopose:=clicked_geopose_2" #C-m




window=1
tmux new-window -t $session:$window -n 'camera'
tmux split-window -t 0 -v
tmux split-window -t 0 -h
tmux split-window -t 2 -h
tmux split-window -t 1 -h
# tmux split-window -t 3 -h


tmux send-keys -t 0 "cd ~/ws/bags" C-m
tmux send-keys -t 0 "ros2 run video_streaming video_streaming_node   --ros-args     -p topic:=/detector/frames     -p out_width:=480     -p out_height:=360     -p out_fps:=10.0     -p receiver:=172.30.30.100     -p port:=5000     -p bitrate_kbps:=300    -p record_mode:=single -p record_path:=video_detector" #C-m

tmux send-keys -t 1 "cd ~/ws/bags" C-m
tmux send-keys -t 1 "ros2 run video_streaming video_streaming_node   --ros-args     -p topic:=/camera/camera/color/image_raw     -p out_width:=480     -p out_height:=360     -p out_fps:=20.0     -p receiver:=127.0.0.1     -p port:=5000     -p bitrate_kbps:=2500    -p record_mode:=single -p record_path:=video_raw" #C-m

# tmux send-keys -t 2 "ros2 run realsense2_camera realsense2_camera_node --ros-args -p rgb_camera.color_profile:=640x480x15 -p depth_module.depth_profile:=848x480x15" #C-m
tmux send-keys -t 2 "ros2 run usb_cam usb_cam_node_exe" #C-m
# tmux send-keys -t 2 "ros2 launch depthai_ros_driver camera.launch.py" #C-m


tmux send-keys -t 3 "cd ~/Documents/yolo_test" C-m
tmux send-keys -t 3 "source py312/bin/activate" C-m
tmux send-keys -t 3 "python rosnode.py --ros-args -r image_raw:=/oak/rgb/image_raw # or for oak_d, just leave image_raw for usb_cam" #C-m

# tmux send-keys -t 4 "cd ~/ws/ros_ws/src/platform_basic_components/start_scripts" C-m
tmux send-keys -t 4 "cd ~/ws/bags" C-m

# tmux send-keys -t 4 "bash rosbag.sh" #C-m



window=2
tmux new-window -t $session:$window -n 'aux'
tmux split-window -t 0 -v
tmux split-window -t 0 -h
tmux split-window -t 1 -h


send_command_to_all_panes_in_window 0 "cd ~/ws/ros_ws"






# window=2
# tmux new-window -t $session:$window -n 'tmp_init_pub'
# tmux split-window -t 0 -v


# tmux send-keys -t 0 "export ROS_DOMAIN_ID=0" C-m
# tmux send-keys -t 0 "ros2 topic pub /clicked_geopose_TEST geographic_msgs/msg/GeoPose 'position:
#   latitude: 0.0
#   longitude: 0.0
#   altitude: 0.0
# orientation:
#   x: 0.0
#   y: 0.0
#   z: 0.0
#   w: 1.0
# '
# " #C-m












tmux attach-session -t $session:0

