



ros2 bag record --topics \
    /camera/camera/color/image_raw \
    /camera/camera/depth/image_rect_raw \
    /fmu/in/goto_setpoint \
    /fmu/in/offboard_control_mode \
    /fmu/in/vehicle_command \
    /fmu/out/manual_control_setpoint \
    /fmu/out/vehicle_control_mode \
    /fmu/out/vehicle_global_position \
    /fmu/out/vehicle_land_detected \
    /fmu/out/vehicle_local_position \
    /fmu/out/vehicle_status_v1 \
    /fmu/out/vehicle_attitude \
    /panda1/heartbeat_status \
    /target_reference_visualization \
    /test_panel/clicked_geopose_2 \
    /test_panel/path_from_ui \
    /test_panel/point_from_ui



