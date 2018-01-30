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
    x_off=0.0
    y_off=0.0

    vres=numpy.array([0.0,0.0])
    blockListDict = {
        'block_a': Block('iris_1', 'base_link'),
	'block_b': Block('iris_2', 'base_link'),
        'block_c': Block('iris_3', 'base_link')
    }
    def flocking(self):
	goal = PoseStamped()
	separation=rules.separation("iris_1",self.blockListDict)
	cohesion=rules.cohesion("iris_1",self.blockListDict)
	self.vres[0]=separation[0] + (0.2*cohesion [0])+self.x_off
	self.vres[1]=separation[1] + (0.2*cohesion [1])+self.y_off
	return self.vres
    
    def tend_to_place(x,y):
	result=numpy.array([0.0,0.0])
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates("iris_1", "base_link")
	result[0]=x-input_drone_coordinates.pose.x
	result[1]=y-input_drone_coordinates.pose.y
	magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
	result=2*(result/magnitude)
	#move 50% toward the goal			
	return result/50
	
	
if __name__ == '__main__':
	 rospy.init_node('iris_1')
	 drone_list=Tutorial()
	 arm_pub=rospy.Publisher("gazebo/iris_1/go_to_destination", PoseStamped,queue_size=1000)	 
   
	 while True:		
		
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		vres=drone_list.flocking()
		obstacle=drone_list.tend_to_place(0,0)
		goal.pose.position.x = vres[0] + (-1*obstacle[0]) + 2
		goal.pose.position.y = vres[1] + (-1*obstacle[1]) + 2
		goal.pose.position.z = 1
		self.arm_pub.publish(goal)
                print "iris_1"
		print drone_list.vres 
