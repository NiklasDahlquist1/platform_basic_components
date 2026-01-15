#!/bin/bash


# robot_name="panda1"
# agent_id="0"




send_command_to_all_panes_in_window() 
{
    for pane in `tmux list-panes -t $1 -F '#P' | sort`; do
        tmux send-keys -t "$pane" "$2" C-m
    done
}


session="auction_server"

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
send_command_to_all_panes_in_window 0 "export ROS_DOMAIN_ID=0"



tmux send-keys -t 0 "ros2 launch platform_components auction_server.launch.py" #C-m
tmux send-keys -t 1 "ros2 run domain_bridge domain_bridge /home/nuc1/ws/ros_ws/src/platform_basic_components/platform_components/params/auction_domain_bridge.yaml" #C-m
tmux send-keys -t 2 "ros2 run foxglove_bridge foxglove_bridge " #C-m
tmux send-keys -t 3 "cd ~/ws/bags/" C-m
tmux send-keys -t 3 "ros2 bag record --all" #C-m

tmux send-keys -t 4 "" #C-m
# tmux send-keys -t 5 "ros2 run auction_task_adder auction_task_adder_node --ros-args -r __ns:=/test_panel" #C-m
tmux send-keys -t 6 "bmon" C-m













tmux attach-session -t $session:0

