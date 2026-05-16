
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    
    return LaunchDescription([
        Node(
            package="kamp_uygulama",
            executable="dolas",
            name="osmanaga",
            remappings=[("turtle1/cmd_vel", "kangal"), ("turtle1/pose", "/pose")],
            namespace="ahmet",
            parameters=[{
                "lin_hiz": 10.0
            }]

        ),
        Node(
            package="turtlesim",
            executable="turtlesim_node",
            name="eyvah",
            remappings=[("turtle1/cmd_vel", "kangal"), ("turtle1/pose", "/pose")],
            namespace="ahmet"

        ),
        ExecuteProcess(
            cmd=["ros2", "topic", "echo", "/turtle1/pose"],
            output='screen'
        )
    ])