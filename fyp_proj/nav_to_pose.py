

from geometry_msgs.msg import PoseStamped
from fyp_proj.waypoint_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration



def robotPause():
    pass

def main():
    rclpy.init()

    navigator = BasicNavigator()

   

    goal_poses = []
    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 14.0
    goal_pose1.pose.position.y = -17.50
    goal_pose1.pose.orientation.w = 0.707
    goal_pose1.pose.orientation.z = 0.707
    goal_poses.append(goal_pose1)

    # additional goals can be appended
    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 7.0
    goal_pose2.pose.position.y = -17.50
    goal_pose2.pose.orientation.w = 0.707
    goal_pose2.pose.orientation.z = 0.707
    goal_poses.append(goal_pose2)


    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id = 'map'
    goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 0.0
    goal_pose3.pose.position.y = -17.50
    goal_pose3.pose.orientation.w = 0.707
    goal_pose3.pose.orientation.z = 0.707
    goal_poses.append(goal_pose3)


    goal_pose4 = PoseStamped()
    goal_pose4.header.frame_id = 'map'
    goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose4.pose.position.x = -7.0
    goal_pose4.pose.position.y = -17.50
    goal_pose4.pose.orientation.w = 0.707
    goal_pose4.pose.orientation.z = 0.707
    goal_poses.append(goal_pose4)


    goal_pose5 = PoseStamped()
    goal_pose5.header.frame_id = 'map'
    goal_pose5.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose5.pose.position.x = -14.0
    goal_pose5.pose.position.y = -17.50
    goal_pose5.pose.orientation.w = 0.707
    goal_pose5.pose.orientation.z = 0.707
    goal_poses.append(goal_pose5)


    goal_pose6 = PoseStamped()
    goal_pose6.header.frame_id = 'map'
    goal_pose6.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose6.pose.position.x = -21.0
    goal_pose6.pose.position.y = -17.50
    goal_pose6.pose.orientation.w = 0.707
    goal_pose6.pose.orientation.z = 0.707
    goal_poses.append(goal_pose6)

    goal_pose_extra = PoseStamped()
    goal_pose_extra.header.frame_id = 'map'
    goal_pose_extra.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose_extra.pose.position.x = -17.0
    goal_pose_extra.pose.position.y = -14.50
    goal_pose_extra.pose.orientation.w = -0.707
    goal_pose_extra.pose.orientation.z = -0.707
    goal_poses.append(goal_pose_extra)

    goal_pose7 = PoseStamped()
    goal_pose7.header.frame_id = 'map'
    goal_pose7.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose7.pose.position.x = -21.0
    goal_pose7.pose.position.y = -10.50
    goal_pose7.pose.orientation.w = 0.707
    goal_pose7.pose.orientation.z = 0.707
    goal_poses.append(goal_pose7)

    goal_pose8 = PoseStamped()
    goal_pose8.header.frame_id = 'map'
    goal_pose8.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose8.pose.position.x = -14.0
    goal_pose8.pose.position.y = -10.50
    goal_pose8.pose.orientation.w = 0.707
    goal_pose8.pose.orientation.z = 0.707
    goal_poses.append(goal_pose8)

    goal_pose9 = PoseStamped()
    goal_pose9.header.frame_id = 'map'
    goal_pose9.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose9.pose.position.x = -7.0
    goal_pose9.pose.position.y = -10.50
    goal_pose9.pose.orientation.w = 0.707
    goal_pose9.pose.orientation.z = 0.707
    goal_poses.append(goal_pose9)

    
    goal_pose10 = PoseStamped()
    goal_pose10.header.frame_id = 'map'
    goal_pose10.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose10.pose.position.x = 0.0
    goal_pose10.pose.position.y = -10.50
    goal_pose10.pose.orientation.w = 0.707
    goal_pose10.pose.orientation.z = 0.707
    goal_poses.append(goal_pose10)

    goal_pose11 = PoseStamped()
    goal_pose11.header.frame_id = 'map'
    goal_pose11.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose11.pose.position.x = 7.0
    goal_pose11.pose.position.y = -10.50
    goal_pose11.pose.orientation.w = 0.707
    goal_pose11.pose.orientation.z = 0.707
    goal_poses.append(goal_pose11)
 

    goal_pose12 = PoseStamped()
    goal_pose12.header.frame_id = 'map'
    goal_pose12.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose12.pose.position.x = 14.0
    goal_pose12.pose.position.y = -10.50
    goal_pose12.pose.orientation.w = 0.707
    goal_pose12.pose.orientation.z = 0.707
    goal_poses.append(goal_pose12)

    goal_pose13 = PoseStamped()
    goal_pose13.header.frame_id = 'map'
    goal_pose13.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose13.pose.position.x = 21.0
    goal_pose13.pose.position.y = -10.50
    goal_pose13.pose.orientation.w = 0.707
    goal_pose13.pose.orientation.z = 0.707
    goal_poses.append(goal_pose13)

    goal_pose14 = PoseStamped()
    goal_pose14.header.frame_id = 'map'
    goal_pose14.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose14.pose.position.x = 17.50
    goal_pose14.pose.position.y = -7.50
    goal_pose14.pose.orientation.w = 0.707
    goal_pose14.pose.orientation.z = 0.707
    goal_poses.append(goal_pose14)
    

    goal_pose15 = PoseStamped()
    goal_pose15.header.frame_id = 'map'
    goal_pose15.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose15.pose.position.x = 21.0
    goal_pose15.pose.position.y = -3.50
    goal_pose15.pose.orientation.w = 0.707
    goal_pose15.pose.orientation.z = 0.707
    goal_poses.append(goal_pose15)

    goal_pose16 = PoseStamped()
    goal_pose16.header.frame_id = 'map'
    goal_pose16.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose16.pose.position.x = 14.0
    goal_pose16.pose.position.y = -3.50
    goal_pose16.pose.orientation.w = 0.707
    goal_pose16.pose.orientation.z = 0.707
    goal_poses.append(goal_pose16)

    goal_pose17 = PoseStamped()
    goal_pose17.header.frame_id = 'map'
    goal_pose17.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose17.pose.position.x = 7.0
    goal_pose17.pose.position.y = -3.50
    goal_pose17.pose.orientation.w = 0.707
    goal_pose17.pose.orientation.z = 0.707
    goal_poses.append(goal_pose17)

    goal_pose18 = PoseStamped()
    goal_pose18.header.frame_id = 'map'
    goal_pose18.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose18.pose.position.x = 0.0
    goal_pose18.pose.position.y = -3.50
    goal_pose18.pose.orientation.w = 0.707
    goal_pose18.pose.orientation.z = 0.707
    goal_poses.append(goal_pose18)

  

    i = 0
    while i< len(goal_poses):
        navigator.goToPose(goal_poses[i])
        while not navigator.isTaskComplete():
            print("Going to the pose")

    
        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
            navigator.pauseRobot(5)
            i = i+1

        elif result == TaskResult.CANCELED:
            print('Goal was canceled!')
        elif result == TaskResult.FAILED:
            print('Goal failed!')
        else:
            print('Goal has an invalid return status!')

    exit(0)
   



if __name__ == '__main__':
    main()