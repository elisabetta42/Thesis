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
def find_neighbours_in_radius(uav_name,blockListDict,radius):
	#agents=current.group.all_drones
	neibourgh={}
	#model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	#input_drone_coordinates = model_coordinates(uav_name, "")	
	#c_y=input_drone_coordinates.pose.position.y
 	#c_x=input_drone_coordinates.twist.linear.x
	a=get_position(uav_name,blockListDict)
	for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       b=get_position(blockName,blockListDict)
               distance=euclidean_distance(a,b)
	       #print block, "block.................................................................."
	       if distance < radius:
		  neibourgh[blockName]=block
	#print neibourgh, "neisdfkjsdfhskh"
	#print blockListDict, "blockkkkk"
	return neibourgh	
def euclidean_distance(a,b):
	distance=math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2))
	return distance
def sum_all_vel_x(uav_name,blockListDict):
	dx=0
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "")	
	#c_x=input_drone_coordinates.pose.position.y
 	c_x=input_drone_coordinates.twist.linear.x
	for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	       x1=resp_coordinates.twist.linear.x
	       dx+=x1-c_x
	#for other in close_drones:
	#	dx+=current.v_ned_d[0]-other.v_ned_d[0]
	return dx
						
def sum_all_vel_y(uav_name,blockListDict):
	dy=0
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "")	
	#c_x=input_drone_coordinates.pose.position.y
 	c_y=input_drone_coordinates.twist.linear.y
	for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    if blockName!=uav_name:
	       resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	       y1=resp_coordinates.twist.linear.y
	       dy+=y1-c_y
	#for other in close_drones:
	#	dx+=current.v_ned_d[0]-other.v_ned_d[0]
	return dy

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
	       dx+=x1-c_x	
	#for other in close_drones:
	#	dx+=current.xyz[0]-other.xyz[0]
	dx=(-1.5)*dx
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
	       dy+=y1-c_y	
	#for other in close_drones:
	#	dx+=current.xyz[0]-other.xyz[0]
	dy=(-1.5)*dy
	return dy	
def sum_all_x(uav_name,blockListDict):
	dx=0
        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    #if blockName!=uav_name:
	    resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
	    x1=resp_coordinates.pose.position.x
	    dx+=x1
	return dx
						
def sum_all_y(uav_name,blockListDict):
	dy=0
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        for block in blockListDict.itervalues():
    	    blockName = str(block._name)
    	    #if blockName!=uav_name:
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
def getaltitude(uav_name):
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "")	
	c_z=input_drone_coordinates.pose.position.z
	return c_z
	
def separation (uav_name,blockListDict):
	#alt_d=8
        pos=get_position(uav_name,blockListDict)
        close_drones=find_neighbours_in_radius(uav_name,blockListDict,1.5)
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
	close_drones=find_neighbours_in_radius(uav_name,blockListDict,20)
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
	position=get_position(uav_name,blockListDict)
	close_drones=find_neighbours_in_radius(uav_name,blockListDict,20)
	if len(close_drones)==0:
		empty=PVector(0,0)
		#velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		#current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	velx=sum_all_vel_x(uav_name, blockListDict)
	velx=(velx/len(close_drones))
	vely=sum_all_vel_x(uav_name, blockListDict)
	vely=(vely/len(blockListDict))
	vel_vector=numpy.array([velx,vely])
	vel_vector=normalize(vel_vector)
	return vel_vector

def flocking (uav_name, blockListDict):	
        print blockListDict
	flocking_vec=1.5*separation(uav_name, blockListDict)+cohesion(uav_name, blockListDict)+velavg(uav_name, blockListDict)#+(-0.4)*cohesion(uav_name, blockListDict)
	return flocking_vec

def normalize(vector):
	vector=PVector(vector[0],vector[1])
	vector.normalize()
	return vector.return_as_vector()

