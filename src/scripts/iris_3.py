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
    def separation(self):
	separation_list=rules.separation("iris_3",self.blockListDict)
	print separation_list
	return separation_list
    def flocking(self):
	separation=rules.separation("iris_3",self.blockListDict)
	cohesion=rules.cohesion("iris_3",self.blockListDict)
	self.vres[0]=separation[0] + (0.4*cohesion [0])+self.x_off
	self.vres[1]=separation[1] + (0.4*cohesion [1])+self.y_off
	return self.vres
	
    def spread(self):
	separation=rules.separation("iris_3",self.blockListDict)
	cohesion=rules.cohesion("iris_3",self.blockListDict)
	self.vres[0]=separation[0] + (-1*cohesion [0])
	self.vres[1]=separation[1] + (-1*cohesion [1])
	return self.vres
    
    def tend_to_place(self,x,y):
	v=numpy.array([0.0,0.0])
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates("iris_3", "")
	x2=input_drone_coordinates.pose.position.x
	y2=input_drone_coordinates.pose.position.y
	distance=math.sqrt(pow((x - x2), 2) + pow((y - y2), 2))
	v[0]=x-input_drone_coordinates.pose.position.x+self.x_off
	v[1]=y-input_drone_coordinates.pose.position.y+self.y_off
	magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
	v=(v/2*magnitude)
	#move 50% toward the goal			
	return v/20
	
    
    def locate_fire(self):
	self.count=self.count+1
	rospy.wait_for_service('/gazebo/get_model_state')
	random_position=numpy.array([0.0,0.0])
	position=numpy.array([0.0,0.0])
	fire=numpy.array([0.0,0.0])
	a = random.random()
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates("iris_3", "")
	x=input_drone_coordinates.pose.position.x
	y=input_drone_coordinates.pose.position.y
	if self.count==20:
		self.x_f= random.uniform(-0.1, 0.1)
		self.y_f= random.uniform(-0.1, 0.1)
		self.count=0
	if self.count==0:
		self.x_f= random.uniform(-0.1, 0.1)
		self.y_f= random.uniform(-0.1, 0.1)
	
	if self.x_f<=0:
		self.x_f=-0.1
	elif self.x_f>0:
		self.x_f=0.1
	
	if self.y_f<=0:
		self.y_f=-0.1
	elif self.y_f>0:
		self.y_f=0.1

	random_position[0]=x+self.x_f
	random_position[1]=y+self.y_f
	
	position[0]=x
	position[1]=y
	
	temperature=rules.temperature_sensor("iris_3")
	if temperature >= 500:
		fire=position
		self.count_back=self.count_back-1
		return (self.count_back*position)
	
	if temperature <= 75:
		self.count_back=0
	if self.count_back==4:
		self.count_back=0
	
	if self.bound_position():
	       return -1*position
	
	return random_position
	
    def bound_position(x,y,self):
		x_max=4
		y_max=4
		x_min=-4
		y_min=-4
		
		if x < x_min:
			return True
		elif x > x_max:
			return True
		if y < y_min:
			return True
		elif y > y_max:
			return True	
		return False
	
    def line_formation_y(self):
		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    		input_drone_coordinates = model_coordinates("iris_1", "")
		x=input_drone_coordinates.pose.position.x
		y=input_drone_coordinates.pose.position.y
		position=numpy.array([0.0,0.0])
		position[0]=x+4
		position[1]=y
		return position	
    def random_walk(self):
		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    		input_drone_coordinates = model_coordinates("iris_3", "")
		x=input_drone_coordinates.pose.position.x
		y=input_drone_coordinates.pose.position.y
		position=numpy.array([0.0,0.0])
		border=self.bound_position(x,y)
		
		if border:
			x=x*-1
			y=y*-1
			position[0]=x
			position[1]=y
			print "I am here"
			return position

		step_x = random.randint(0,1)
		if step_x == 1:
			x=x+1+numpy.random.normal()
		else:
			x=x-1+numpy.random.normal()
		
		step_y = random.randint(0,1)
		if step_y == 1:
			y=y+1+numpy.random.normal()
		else:
			y=y-1+numpy.random.normal()	
	
		
		separation=rules.separation("iris_3",self.blockListDict)
		spread=self.spread()
		position[0]=spread[0]+x
		position[1]=spread[1]+y
		return position
			 
	
if __name__ == '__main__':
	 rospy.init_node('iris_3')
	 drone_list=Tutorial()
	 arm_pub=rospy.Publisher("gazebo/iris_3/go_to_destination", PoseStamped,queue_size=1000)	 
   	
	 while True:	
		vres=drone_list.flocking()
		goal = PoseStamped()
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.velocity.x = vres[0] + drone_list.x_off
		goal.pose.velocity.y = vres[1] + drone_list.y_off              
		goal.pose.position.z = 1
		arm_pub.publish(goal)
		print vres
