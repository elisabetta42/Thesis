#!/usr/bin/env python
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
    arm_pub=list()
    arm_pub.append(rospy.Publisher("gazebo/iris_1/go_to_destination", PoseStamped,queue_size=1000))
    arm_pub.append(rospy.Publisher("gazebo/iris_2/go_to_destination", PoseStamped,queue_size=1000))
    arm_pub.append(rospy.Publisher("gazebo/iris_3/go_to_destination", PoseStamped,queue_size=1000))
    coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)  
    max=0
    previous_temp_1=0
    previous_temp_2=0
    previous_temp_3=0
    
    previous_x_1=0
    previous_y_1=0
    
    previous_x_2=0
    previous_y_2=0
    
    previous_x_3=0
    previous_y_3=0
    
    vres=numpy.array([0.0,0.0])
    further_pose=PoseStamped()
    _blockListDict = {
        'block_a': Block('iris_1', 'base_link'),
	'block_b': Block('iris_2', 'base_link'),
        'block_c': Block('iris_3', 'base_link')
    }
    
    def separation(self,uav_name):
			model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    			input_drone_coordinates = model_coordinates(uav_name, "base_link")	
			c_x=input_drone_coordinates.pose.position.x
 			c_y=input_drone_coordinates.pose.position.y
			a = random.random()
			f= random.uniform( -0.005, 0.005 )
			#return vector	
			v=numpy.array([0.0,0.0])
			#add random quantity
			#position=numpy.array([c_x+f,c_y+f])
		        position=numpy.array([c_x,c_y])
			#radius
			radius=3	
			n_count=0			
    			for block in self._blockListDict.itervalues():
    				blockName = str(block._name)
				
    				if blockName!=uav_name:
					 resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
					 x1=resp_coordinates.pose.position.x
					 x2=input_drone_coordinates.pose.position.x
					 y1=resp_coordinates.pose.position.y
					 y2=input_drone_coordinates.pose.position.y
					 distance=math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
					 #Finding neibourghs
					 if distance < radius:
					 	v[0] += x1 - x2
						v[1] += y1 - y2
					        n_count=n_count+1
			#print "v after n count"
			#print v
			#Divide by the number of neibourgh
			if n_count==0:		
				print "I am moving randomly..."
				return position			
			v[0]=v[0]/n_count
			v[1]=v[1]/n_count
			#calculate magnitude
			magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
			print "magnitude separation"			
			print magnitude
			v=v/magnitude
			print "unitary vector"
			print v
			#print "v after n count division"
			#print v
			#Opposite direction
			v[0]*=-2
			v[1]*=-2
			print "negated vector"
			print v
			#print "v opposite direction"
			#print v
			#Normalize vector using min-max normalization
			
			#print "v after normalization"
			#print v
			return v		 	
					 
   #def alignment(self, uav_name):
    def cohesion(self, uav_name):
		        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    			input_drone_coordinates = model_coordinates(uav_name, "base_link")	
			c_x=input_drone_coordinates.pose.position.x
 			c_y=input_drone_coordinates.pose.position.y
			a = random.random()
			f= random.uniform( -0.005, 0.005 )
			
			#return vector	
			v=numpy.array([0.0,0.0])
			#add random quantity
			position=numpy.array([c_x+f,c_y+f])
			#radius
			radius=50	
			n_count=0			
    			for block in self._blockListDict.itervalues():
    				blockName = str(block._name)
				
    				if blockName!=uav_name:
					 resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
					 x1=resp_coordinates.pose.position.x
					 x2=input_drone_coordinates.pose.position.x
					 y1=resp_coordinates.pose.position.y
					 y2=input_drone_coordinates.pose.position.y
					 distance=math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
					 #Finding neibourghs
					 if distance < radius:
					 	v[0] += x1 
						v[1] += y1
					        n_count=n_count+1
			#print "v after n count"
			#print v
			#Divide by the number of neibourgh
			if n_count==0:
				return position	
			#return center of mass		
			v[0]=v[0]/n_count
			v[1]=v[1]/n_count
			#print "v after n count division"
			#print v
			#calculate directio for center of mass
			v[0]=v[0] - input_drone_coordinates.pose.position.x
			v[1]=v[1] - input_drone_coordinates.pose.position.y
			#Normalize vector using min-max normalization
			magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
			v=v/magnitude
			#print "v after normalization"
			#print v			
			return v
	
    def temperature_1(self,temperature):
	print "I am in temperature"
	print temperature
	goal = PoseStamped()
	x_off=0.0
	y_off=0.0
	separation=tuto.separation("iris_1")
	cohesion=tuto.cohesion("iris_1")
	model_coordinates_1 = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)  
	model_coordinates = model_coordinates_1("iris_1", "base_link")	
	v=numpy.array([0.0,0.0])			
	if temperature > 60:
		if self.previous_temp_1 < temperature:
			current_x=model_coordinates.pose.position.x 
			current_y=model_coordinates.pose.position.y
			v[0]=current_x-self.previous_x_1
			v[1]=current_y-self.previous_y_1
			magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
			v=(v+0.8)*(-1)
			goal.header.frame_id = "/base_link"
			goal.header.stamp = rospy.Time.now()
			goal.pose.position.x = 1.5*v[0] + (0.7*separation[0]) + (0.3*cohesion [0])+x_off
			goal.pose.position.y = 1.5*v[1] + (0.7*separation[1]) + (0.3*cohesion [1])+y_off
			goal.pose.position.z = 1
			self.arm_pub[0].publish(goal)
			rospy.sleep(0.5)
	self.previous_temp_1=temperature
	self.previous_x_1=model_coordinates.pose.position.x 
	self.previous_y_1=model_coordinates.pose.position.y 
   	
    def temperature_2(self,temperature):
	print "I am in temperature"
	print temperature
	goal = PoseStamped()
	x_off=-2.0
	y_off=-2.0
	separation=tuto.separation("iris_2")
	cohesion=tuto.cohesion("iris_2")
	model_coordinates_2 = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)  
	model_coordinates = model_coordinates_2("iris_2", "base_link")	
	v=numpy.array([0.0,0.0])			
	if temperature > 60:
		if self.previous_temp_2 < temperature:
			current_x=model_coordinates.pose.position.x 
			current_y=model_coordinates.pose.position.y
			v[0]=current_x-self.previous_x_2
			v[1]=current_y-self.previous_y_2
			magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
			v=(v+0.8)*(-1)
			print "vector"
			print v
			goal.header.frame_id = "/base_link"
			goal.header.stamp = rospy.Time.now()
			goal.pose.position.x = 1.5*v[0] + (0.7*separation[0]) + (0.3*cohesion [0])+x_off
			goal.pose.position.y = 1.5*v[1] + (0.7*separation[1]) + (0.3*cohesion [1])+y_off
			goal.pose.position.z = 1
			self.arm_pub[1].publish(goal)
			rospy.sleep(0.5)
	self.previous_temp_2=temperature
	self.previous_x_2=model_coordinates.pose.position.x 
	self.previous_y_2=model_coordinates.pose.position.y 

    def temperature_3(self,temperature):
	print "I am in temperature"
	print temperature
	goal = PoseStamped()
	x_off=-2.0
	y_off=2.0
	separation=tuto.separation("iris_3")
	cohesion=tuto.cohesion("iris_3")
	model_coordinates_3 = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)  
	model_coordinates = model_coordinates_3("iris_3", "base_link")	
	v=numpy.array([0.0,0.0])			
	if temperature > 60:
		if self.previous_temp_3 < temperature:
			current_x=model_coordinates.pose.position.x 
			current_y=model_coordinates.pose.position.y
			v[0]=current_x-self.previous_x_3
			v[1]=current_y-self.previous_y_3
			magnitude = math.sqrt(pow((v[0]), 2)+pow((v[1]), 2))
			v=(v+0.8)*(-1)
			print "vector"
			print v
			goal.header.frame_id = "/base_link"
			goal.header.stamp = rospy.Time.now()
			goal.pose.position.x = 1.5*v[0] + (0.7*separation[0]) + (0.3*cohesion [0])+x_off
			goal.pose.position.y = 1.5*v[1] + (0.7*separation[1]) + (0.3*cohesion [1])+y_off
			goal.pose.position.z = 1
			self.arm_pub[2].publish(goal)
			rospy.sleep(0.5)
	self.previous_temp_3=temperature
	self.previous_x_3=model_coordinates.pose.position.x 
	self.previous_y_3=model_coordinates.pose.position.y 
		
		
				         
if __name__ == '__main__':
	rospy.init_node("go_to_destination") 
	tuto = Tutorial()
	var1, var2, var3 = raw_input("Enter target position").split()
	sub_temp1=rospy.Subscriber("/gazebo/iris_1/temperature", Float64 , tuto.temperature_1)
        sub_temp2=rospy.Subscriber("/gazebo/iris_2/temperature", Float64 , tuto.temperature_2)
        sub_temp2=rospy.Subscriber("/gazebo/iris_3/temperature", Float64 , tuto.temperature_3)
	
	#sub_dist1=rospy.Subscriber("/gazebo/iris_1/fire_dist", Float64 , tuto.dist_1)
        #sub_dist2=rospy.Subscriber("/gazebo/iris_2/fire_dist", Float64 , tuto.dist_2)
        #sub_dist3=rospy.Subscriber("/gazebo/iris_3/fire_dist", Float64 , tuto.dist_3)
	while True:
		var=0
		vres=numpy.array([0.0,0.0])		
		#iris_1
		goal = PoseStamped()
		x_off=0.0
		y_off=0.0
		separation=tuto.separation("iris_1")
		cohesion=tuto.cohesion("iris_1")
		v2=numpy.array([(float(var1)+x_off),float(var2)+y_off])
		tuto.vres[0]=separation[0] + (0.3*cohesion [0])
		tuto.vres[1]=separation[1] + (0.3*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = tuto.vres[0] + x_off
		goal.pose.position.y = tuto.vres[1] + y_off
		goal.pose.position.z = float(var3)
		tuto.arm_pub[0].publish(goal)
		tuto.vres=numpy.array([0.0,0.0])
		#iris_2		
		goal = PoseStamped()
		x_off=-2
		y_off=-2
		separation=tuto.separation("iris_2")
		cohesion=tuto.cohesion("iris_2")
		v2=numpy.array([(float(var1)+x_off),float(var2)+y_off])
		tuto.vres[0]=separation[0] + (0.3*cohesion [0])
		tuto.vres[1]=separation[1] + (0.3*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = tuto.vres[0] + x_off
		goal.pose.position.y = tuto.vres[1] + y_off
		goal.pose.position.z = float(var3)
		tuto.arm_pub[1].publish(goal)
		tuto.vres=numpy.array([0.0,0.0])
		#iris_3		
		goal = PoseStamped()
		x_off=-2
		y_off=2
		separation=tuto.separation("iris_3")
		cohesion=tuto.cohesion("iris_3")
		v2=numpy.array([(float(var1)+x_off),float(var2)+y_off])
		tuto.vres[0]=separation[0] + (0.3*cohesion [0])
		tuto.vres[1]=separation[1] + (0.3*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = tuto.vres[0] + x_off
		goal.pose.position.y = tuto.vres[1] + y_off
		goal.pose.position.z = float(var3)		
		tuto.arm_pub[2].publish(goal)
		tuto.vres=numpy.array([0.0,0.0])
		
		

