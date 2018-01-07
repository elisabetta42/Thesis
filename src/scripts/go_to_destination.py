#!/usr/bin/env python
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
import sys
import rospy

#insert an help
def main():
	
	rospy.init_node("go_to_dest") 
	arm_pub = rospy.Publisher("gazebo/iris_1/go_to_destination", PoseStamped,queue_size=10)
	rospy.sleep(2)
	goal = PoseStamped()
	#goal.header.frame_id = "/base_link"
	#goal.header.stamp = rospy.Time.now()
	var1, var2, var3 = raw_input("Enter target position").split()
	goal.pose.position.x = float(var1)
	goal.pose.position.y = float(var2)
	goal.pose.position.z = float(var3)
	goal.pose.orientation.w = 1.0
	arm_pub.publish(goal)  
	rospy.spin()


if __name__ == '__main__':
    main()

