#!/usr/bin/env python
import rules
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from gazebo_msgs.srv import GetModelState
import sys
import rospy
import numpy
import math
import random
from std_msgs.msg import Float64
class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name
class Tutorial:
    blockListDict = {
        'block_a': Block('iris_1', 'base_link'),
	'block_b': Block('iris_2', 'base_link'),
        'block_c': Block('iris_3', 'base_link')
    }
if __name__ == '__main__':
	 rospy.init_node('iris_3')
	 arm_pub=rospy.Publisher("gazebo/iris_3/go_to_destination", PoseStamped,queue_size=1000)
	 x_off=-2.0
	 y_off=+2.0
	 drone_list=Tutorial()
	 vres=numpy.array([0.0,0.0])
	 while True:
		goal = PoseStamped()
		separation=rules.separation("iris_3",drone_list.blockListDict)
	        cohesion=rules.cohesion("iris_3",drone_list.blockListDict)
	        vres[0]=separation[0] + (0.2*cohesion [0])
		vres[1]=separation[1] + (0.2*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = vres[0] + x_off
		goal.pose.position.y = vres[1] + y_off
		goal.pose.position.z = 1
		arm_pub.publish(goal)

		print "iris_3"
		print vres 
