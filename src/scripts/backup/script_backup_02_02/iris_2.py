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
    y_off=-2.0
    count=0
    x_f=0
    y_f=0
    vres=numpy.array([0.0,0.0])
    blockListDict = {
        'block_a': Block('iris_1', ""),
	'block_b': Block('iris_2', ""),
        'block_c': Block('iris_3', "")
    }
    def separation(self):
	separation_list=rules.separation("iris_2",self.blockListDict)
	print separation_list
	return separation_list
    def flocking(self):
	separation=rules.separation("iris_2",self.blockListDict)
	cohesion=rules.cohesion("iris_2",self.blockListDict)
	self.vres[0]=separation[0] + (0.2*cohesion [0])+self.x_off
	self.vres[1]=separation[1] + (0.2*cohesion [1])+self.y_off
	return self.vres
    
    def tend_to_place(self,x,y):
	v=numpy.array([0.0,0.0])
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates("iris_2", "")
	x2=input_drone_coordinates.pose.position.x
	y2=input_drone_coordinates.pose.position.y
	distance=math.sqrt(pow((x - x2), 2) + pow((y - y2), 2))
	if distance < 2:
		v[0]=x-input_drone_coordinates.pose.position.x
		v[1]=y-input_drone_coordinates.pose.position.y
		magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
		v=(v/2*magnitude)
		#move 50% toward the goal			
		return v/50
	v[0]=x2
	v[1]=y2
	return v
    
    def locate_fire(self):
	self.count=self.count+1
	rospy.wait_for_service('/gazebo/get_model_state')
	random_position=numpy.array([0.0,0.0])
	position=numpy.array([0.0,0.0])
	fire=numpy.array([0.0,0.0])
	a = random.random()
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates("iris_2", "")
	x=input_drone_coordinates.pose.position.x
	y=input_drone_coordinates.pose.position.y
	if self.count==15:
		self.x_f= random.uniform(-0.2, 0.2)
		self.y_f= random.uniform(-0.2, 0.2)
		self.count=0
	if self.count==0:
		self.x_f= random.uniform(-0.2, 0.2)
		self.y_f= random.uniform(-0.2, 0.2)
	
	if self.x_f<=0:
		self.x_f=-0.2
	elif self.x_f>0:
		self.x_f=0.2
	
	if self.y_f<=0:
		self.y_f=-0.2
	elif self.y_f>0:
		self.y_f=0.2

	random_position[0]=x+self.x_f
	random_position[1]=y+self.y_f
	
	position[0]=x
	position[1]=y
	
	temperature=rules.temperature_sensor("iris_2")
	if temperature >= 100:
		fire=position
		return (-1*position)
	
	if self.bound_position():
	       return -1*position

	return random_position
	
    def bound_position(self):
		rospy.wait_for_service('/gazebo/get_model_state')
		x_max=5
		y_max=5
		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    		input_drone_coordinates = model_coordinates("iris_2", "")
		x=input_drone_coordinates.pose.position.x
		y=input_drone_coordinates.pose.position.y
		position=numpy.array([0.0,0.0])
		position[0]=x
		position[1]=y
		if (x>=x_max or x<=-x_max) or (y>=y_max or y<=-y_max):
			return True		
		return False
		
			 
	
if __name__ == '__main__':
	 rospy.init_node('iris_2')
	 drone_list=Tutorial()
	 arm_pub=rospy.Publisher("gazebo/iris_2/go_to_destination", PoseStamped,queue_size=1000)	 
   
	 while True:		
		goal = PoseStamped()
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		explore=drone_list.locate_fire()
		vres=drone_list.flocking()
		obstacle=drone_list.tend_to_place(0,0)
		separation=drone_list.separation()
		#goal.pose.position.x = vres[0] + (-1*obstacle[0]) + 2
		#goal.pose.position.y = vres[1] + (-1*obstacle[1]) + 2
                
		goal.pose.position.x = explore[0] + drone_list.x_off + (0.5*separation[0])
		goal.pose.position.y = explore[1] + drone_list.y_off + (0.5*separation[1])
		goal.pose.position.z = 1
		arm_pub.publish(goal)

		rospy.sleep(0.05)
                #print "iris_2"
		#print drone_list.vres 
