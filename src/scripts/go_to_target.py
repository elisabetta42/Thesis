#!/usr/bin/env python
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from gazebo_msgs.srv import GetModelState
import sys
import rospy
import numpy
import math
import random

class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name

class Tutorial:
    
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
			f= random.uniform( -0.2, 0.2 )
			#return vector	
			v=numpy.array([0.0,0.0])
			#add random quantity
			position=numpy.array([c_x+f,c_y+f])
			#radius
			radius=2.5
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
			f= random.uniform( -0.2, 0.2 )
			
			#return vector	
			v=numpy.array([0.0,0.0])
			#add random quantity
			position=numpy.array([c_x+f,c_y+f])
			#radius
			radius=30	
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
				         
if __name__ == '__main__':
	rospy.init_node("go_to_destination") 
	tuto = Tutorial()
	var1, var2, var3 = raw_input("Enter target position").split()
	
	while True:
		
		
		vres=numpy.array([0.0,0.0])		
		arm_pub_1 = rospy.Publisher("gazebo/iris_1/go_to_destination", PoseStamped,queue_size=1000)
		arm_pub_2 = rospy.Publisher("gazebo/iris_2/go_to_destination", PoseStamped,queue_size=1000)
		arm_pub_3 = rospy.Publisher("gazebo/iris_3/go_to_destination", PoseStamped,queue_size=1000)
		#iris_1
		goal = PoseStamped()
		x_off=0.0
		y_off=0.0
		separation=tuto.separation("iris_1")
		cohesion=tuto.cohesion("iris_1")
		#v2=numpy.array([(float(var1)+x_off),float(var2)+y_off])
		#vres=r1*v1+r2*v2
		vres[0]=separation[0] + (0.3*cohesion [0])
		vres[1]=separation[1] + (0.3*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = vres[0] + x_off
		goal.pose.position.y = vres[1] + y_off
		goal.pose.position.z = float(var3)
		arm_pub_1.publish(goal)  
		
		#iris_2		
		goal = PoseStamped()
		x_off=-6
		y_off=-6
		separation=tuto.separation("iris_2")
		cohesion=tuto.cohesion("iris_2")
		#v2=numpy.array([(float(var1)+x_off),float(var2)+y_off])
		#vres=r1*v1+r2*v2
		vres[0]=separation[0] + (0.3*cohesion [0])
		vres[1]=separation[1] + (0.3*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = vres[0] + x_off
		goal.pose.position.y = vres[1] + y_off
		goal.pose.position.z = float(var3)
		arm_pub_2.publish(goal)
		
		#iris_3		
		goal = PoseStamped()
		x_off=-6
		y_off=6
		separation=tuto.separation("iris_3")
		cohesion=tuto.cohesion("iris_3")
		#v2=numpy.array([(float(var1)+x_off),float(var2)+y_off])
		#vres=r1*v1+r2*v2
		vres[0]=separation[0] + (0.3*cohesion [0])
		vres[1]=separation[1] + (0.3*cohesion [1])
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.pose.position.x = vres[0] + x_off
		goal.pose.position.y = vres[1] + y_off
		goal.pose.position.z = float(var3)		
		arm_pub_3.publish(goal)
		
		
if __name__ == '__main__':
    main()

