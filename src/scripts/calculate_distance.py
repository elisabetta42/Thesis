#! /usr/bin/env python
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy

import math

import rospy

class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name

class Tutorial:
    rospy.init_node("moveit")
    _blockListDict = {
        'block_a': Block('iris_1', 'base_link'),
	'block_b': Block('iris_2', 'base_link'),
        'block_c': Block('iris_3', 'base_link')
    }

    def show_gazebo_models(self):
	while True:  
    		try:
    			model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    			input_drone_coordinates = model_coordinates("iris_1", "base_link")
    			#print '\n'
    			#print 'Status.success = ', input_drone_coordinates.success
    			#print("iris_1")
   			#print("Cube " + str("iris_1"))
    			#print("Position of X : " + str(input_drone_coordinates.pose.position.x))
   			#print("Position of Y : " + str(input_drone_coordinates.pose.position.y))
   			#print("Position of Z : " + str(input_drone_coordinates.pose.position.z))
    			#print("Orientation of X : " + str(input_drone_coordinates.pose.orientation.x))
    			#print("Orientation of Y : " + str(input_drone_coordinates.pose.orientation.y))
    			#print("Orientation of Z : " + str(input_drone_coordinates.pose.orientation.z)) 	
			distances = list()
    					
    			for block in self._blockListDict.itervalues():
    				blockName = str(block._name)
    				if blockName!="iris_1" :
					#arm_pub = rospy.Publisher("gazebo/iris_1/distances", Float64, queue_size=10)
					distances_pub = rospy.Publisher('gazebo/iris_1/distances', Floats,queue_size=10)
					#print "current model"
    					resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
					x1=resp_coordinates.pose.position.x
					x2=input_drone_coordinates.pose.position.x
					y1=resp_coordinates.pose.position.y
					y2=input_drone_coordinates.pose.position.y
					distance=math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
					#math.sqrt(((x1-x2)**2)+((y1-y2)**2))
					distances.append(distance)
					print "distance"
					print blockName
					print distance
    					#print '\n'
    					#print 'Status.success = ', resp_coordinates.success
    					#print("Cube " + str(block._name))
    					#print("Position of X : " + str(resp_coordinates.pose.position.x))
    					#print("Position of Y : " + str(resp_coordinates.pose.position.y))
    					#print("Position of Z : " + str(resp_coordinates.pose.position.z))
    					#print("Orientation of X : " + str(resp_coordinates.pose.orientation.x))
    					#print("Orientation of Y : " + str(resp_coordinates.pose.orientation.y))
    					#print("Orientation of Z : " + str(resp_coordinates.pose.orientation.z))
				else :
					distances.append(float(-1))		 

		except rospy.ServiceException as e:
    		       rospy.loginfo("Get Model State service call failed:  {0}".format(e))
		numpy.set_printoptions(precision=2)
		drone_distances = numpy.array(distances)	
		#print "list"
		print drone_distances						
		distances_pub.publish(drone_distances)
    		rospy.sleep(10)
		

if __name__ == '__main__':
		tuto = Tutorial()
        	tuto.show_gazebo_models()

