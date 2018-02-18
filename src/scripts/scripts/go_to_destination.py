#!/usr/bin/env python
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
import sys
import rospy

#insert an help
def main():
	rospy.init_node("go_to_dest") 
	
	while True:
		x_off=0.0
		y_off=0.0
		var1, var2, var3, var4 = raw_input("Enter target position").split()
		if var4=="iris_2":
			x_off=-2
			y_off=-2
		elif var4=="iris_3":
			x_off=-2
			y_off=2
			
		arm_pub = rospy.Publisher("gazebo/"+var4+"/go_to_destination", PoseStamped,queue_size=1000)
		print "gazebo/"+var4+"/go_to_destination"
		goal = PoseStamped()
		#goal.header.frame_id = "/base_link"
		#goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = float(var1)+x_off
		goal.pose.position.y = float(var2)+y_off
		goal.pose.position.z = float(var3)
		#goal.pose.orientation.w = 1.0
		arm_pub.publish(goal)  
	#rospy.spin()


if __name__ == '__main__':
    main()

