from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
   turtlesim=Node(
      package='turtlesim',
      executable='turtlesim_node',
      name='turtlesim'
   )
   turtle_chase=Node(
      package='turtlenew_pkg',
      executable='turtle_chase',
      output='screen'
      
   )
   return LaunchDescription([turtlesim,turtle_chase])