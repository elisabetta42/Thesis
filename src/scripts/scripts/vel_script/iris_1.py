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
import quadrotor as quad
import numpy as np
from std_msgs.msg import Float64
from geometry_msgs.msg import TwistStamped
class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name
class Tutorial:
    x_off=1.0
    y_off=1.0
    count=0
    x_f=0
    y_f=0
    x=0
    y=0
    # Setting quads
    m = 0.65 # Kg
    l = 0.23 # m
    Jxx = 7.5e-3 # Kg/m^2
    Jyy = Jxx
    Jzz = 1.3e-2
    Jxy = 0
    Jxz = 0
    Jyz = 0
    J = np.array([[Jxx, Jxy, Jxz], \
              [Jxy, Jyy, Jyz], \
              [Jxz, Jyz, Jzz]])
    CDl = 9e-3
    CDr = 9e-4
    kt = 3.13e-5  # Ns^2
    km = 7.5e-7   # Ns^2
    kw = 1/0.18   # rad/s

# Initial conditions
    att_0 = np.array([0.0, 0.0, 0.0])
    pqr_0 = np.array([0.0, 0.0, 0.0])
    xyz1_0 = np.array([1.0, 1.2, 0.0])

    v_ned_0 = np.array([0.0, 0.0, 0.0])
    w_0 = np.array([0.0, 0.0, 0.0, 0.0])

    q1 = quad.quadrotor(1, m, l, J, CDl, CDr, kt, km, kw, \
        att_0, pqr_0, xyz1_0, v_ned_0, w_0)
    count_back=0
    vres=numpy.array([0.0,0.0,0.0])
    blockListDict = {
        'block_a': Block('iris_1', ""),
	'block_b': Block('iris_2', ""),
        'block_c': Block('iris_3', "")
    }
    
    def swarm(self,uav_name, blockListDict):
	#separation=rules.separation("iris_1",self.blockListDict)
	#cohesion=rules.cohesion("iris_1",self.blockListDict)
	self.vres[0]=rules.flocking(uav_name, blockListDict)[0] #+ self.x_off
	self.vres[1]=0.4*rules.flocking(uav_name, blockListDict)[1] #+ self.y_off
	#self.vres[2]=self.q1.set_v_2D_alt_lya(self.vres[0:1],-1)[2]
	return self.vres
    
	
if __name__ == '__main__':
	 rospy.init_node('iris_1')
	 drone_list=Tutorial()
	 arm_pub=rospy.Publisher("gazebo/iris_1/go_to_destination", TwistStamped,queue_size=1000)	 
   	
	 while True:	
		vres=drone_list.swarm("iris_1", drone_list.blockListDict)		
		#goal = PoseStamped()
		goal=TwistStamped()
		goal.header.frame_id = "/base_link"
		goal.header.stamp = rospy.Time.now()
		goal.twist.linear.x = vres[0] #+ drone_list.x_off
		goal.twist.linear.y = vres[1] #+ drone_list.y_off              
		goal.twist.linear.z = 0.01
		arm_pub.publish(goal)
		print vres
		
               
