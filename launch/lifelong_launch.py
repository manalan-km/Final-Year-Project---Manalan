from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument

from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    
    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = get_package_share_directory("fyp_proj") + '/config/mapper_params_lifelong.yaml'
    lifelong_slam_toolbox = launch_ros.actions.Node(
          parameters=[
            params_file,
            {'use_sim_time':use_sim_time}
          ],
          package='slam_toolbox',
          executable='lifelong_slam_toolbox_node',
          name='slam_toolbox',
          output='screen'
        )
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
            lifelong_slam_toolbox
    ])








