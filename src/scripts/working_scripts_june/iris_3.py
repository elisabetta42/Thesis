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
    x_off=-2.0
    y_off=2.0
    count=0
    x_f=0
    y_f=0
    count_back=0
    vres=numpy.array([0.0,0.0])
    blockListDict = {
        'block_a': Block('iris_1', ""),
	'block_b': Block('iris_2', ""),
        'block_c': Block('iris_3', "")
    }
    def swarm(self,uav_name, blockListDict):
	#separation=rules.separation("iris_1",self.blockListDict)
	#cohesion=rules.cohesion("iris_1",self.blockListDict)
	self.vres[0]=rules.flocking(uav_name, blockListDict)[0] + self.x_off
	self.vres[1]=rules.flocking(uav_name, blockListDict)[1] + self.y_off
	return self.vres

	
if __name__ == '__main__':
	 rospy.init_node('iris_3')
	 drone_list=Tutorial()
	 arm_pub=rospy.Publisher("gazebo/iris_3/go_to_destination", PoseStamped,queue_size=1000)	 
   	
	 while True:	
		vres=drone_list.swarm("iris_3", drone_list.blockListDict)		
		goal = PoseStamped()
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = vres[0] + drone_list.x_off
		goal.pose.position.y = vres[1] + drone_list.y_off              
		goal.pose.position.z = 1
		arm_pub.publish(goal)
		print vres
		
               
