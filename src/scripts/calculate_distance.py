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
			distances = list()
    					
    			for block in self._blockListDict.itervalues():
    				blockName = str(block._name)
    				if blockName!="iris_1" :
					distances_pub = rospy.Publisher('gazebo/iris_1/distances', Floats,queue_size=10)
    					resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
					x1=resp_coordinates.pose.position.x
					x2=input_drone_coordinates.pose.position.x
					y1=resp_coordinates.pose.position.y
					y2=input_drone_coordinates.pose.position.y
					distance=math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
					distances.append(distance)
				
				else :
					distances.append(float(-1))		 

		except rospy.ServiceException as e:
    		       rospy.loginfo("Get Model State service call failed:  {0}".format(e))
		numpy.set_printoptions(precision=2)
		drone_distances = numpy.array(distances)						
		distances_pub.publish(drone_distances)
    		rospy.sleep(10)
	
		

if __name__ == '__main__':
		tuto = Tutorial()
        	tuto.show_gazebo_models()

