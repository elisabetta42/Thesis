#!/usr/bin/env python
from pvector import PVector
import numpy
import math
import temperature_function as temp
import plugin
import time
from random import randint
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from gazebo_msgs.srv import GetModelState
import sys
import rospy
import numpy
import math
import random
from std_msgs.msg import Float64	
def sub_all_x(uav_name,blockListDict):
	dx=0
        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "")	
	c_x=input_drone_coordinates.pose.position.x
 	#c_y=input_drone_coordinates.pose.position.y
	for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	       x1=resp_coordinates.pose.position.x
	       dx+=c_x-x1	
	#for other in close_drones:
	#	dx+=current.xyz[0]-other.xyz[0]
	dx=(-1)*dx
	return dx					
def sub_all_y(uav_name,blockListDict):
	dy=0
        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "")	
	#c_x=input_drone_coordinates.pose.position.y
 	c_y=input_drone_coordinates.pose.position.y
	for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	       y1=resp_coordinates.pose.position.y
	       dy+=c_y-y1	
	#for other in close_drones:
	#	dx+=current.xyz[0]-other.xyz[0]
	dy=(-1)*dy
	return dy	
def sum_all_x(uav_name,blockListDict):
	dx=0
        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	       x1=resp_coordinates.pose.position.x
	       dx+=x1
	return dx
						
def sum_all_y(uav_name,blockListDict):
	dy=0
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	       y1=resp_coordinates.pose.position.y
	       dy+=y1
	return dy
		
def get_position(uav_name,blockListDict):
	 model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	 input_drone_coordinates = model_coordinates(uav_name, "")	
	 c_x=input_drone_coordinates.pose.position.x
 	 c_y=input_drone_coordinates.pose.position.y
	 comulative_distance=0
	 v=numpy.array([0.0,0.0])
	 position=numpy.array([c_x,c_y])
	 return position
	
def separation (uav_name,blockListDict):
	alt_d=8
        pos=get_position(uav_name,blockListDict)
        close_drones=blockListDict
	position=PVector(pos[0],pos[1])
	#close_drones=find_neighbours_in_radius(current,1000)
	if len(close_drones)==0:
		empty=PVector(0,0)
		#velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		#current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	dx=sub_all_x(uav_name,blockListDict)
	dx=(dx/len(blockListDict))
	dy=sub_all_y(uav_name,blockListDict)
	dy=(dy/len(blockListDict))	
	sep_vector=numpy.array([dx,dy])
	sep_vector=normalize(sep_vector)
	return sep_vector

def cohesion (uav_name,blockListDict):
	alt_d=8
        pos=get_position(uav_name,blockListDict)
	position=PVector(pos[0],pos[1])
	close_drones=blockListDict
	#close_drones=find_neighbours_in_radius(current,1000)
	if len(close_drones)==0:
		empty=PVector(0,0)
		#velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		#current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	sx=sum_all_x(uav_name,blockListDict)
	sx=(sx/len(blockListDict))
	sx=sx - pos[0]
	sy=sum_all_y(uav_name,blockListDict)
	sy=(sy/len(blockListDict))
	sy=sy - pos[1]
	cohesion_vec=numpy.array([(sx-pos[0]),(sy-pos[1])])
	cohesion_vec=normalize(cohesion_vec)
	return cohesion_vec

def velavg (uav_name,blockListDict):
	alt_d=8
	position=PVector(current.xyz[0],current.xyz[1])
	close_drones=find_neighbours_in_radius(current,1000)
	if len(close_drones)==0:
		empty=PVector(0,0)
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	velx=sum_all_vel_x(close_drones,current)
	velx=(velx/len(close_drones))
	vely=sum_all_vel_x(close_drones,current)
	vely=(vely/len(close_drones))
	vel_vector=numpy.array([velx,vely])
	vel_vector=normalize(vel_vector)
	return vel_vector

def flocking (uav_name, blockListDict):	
	flocking_vec=separation(uav_name, blockListDict)+cohesion(uav_name, blockListDict)#+velavg(current))
	return flocking_vec

def normalize(vector):
	vector=PVector(vector[0],vector[1])
	vector.normalize()
	return vector.return_as_vector()

