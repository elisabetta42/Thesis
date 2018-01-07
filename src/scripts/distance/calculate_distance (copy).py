#! /usr/bin/env python
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int32

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
    	while not rospy.is_shutdown():
        	try:
            		model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	    		input_drone_coordinates = model_coordinates("iris_1", "base_link")
            		print '\n'
            		print 'Status.success = ', input_drone_coordinates.success
            		print("iris_1")
            		print("Cube " + str("iris_1"))
            		print("Position of X : " + str(input_drone_coordinates.pose.position.x))
	    		print("Position of Y : " + str(input_drone_coordinates.pose.position.y))
	    		print("Position of Z : " + str(input_drone_coordinates.pose.position.z))
            		print("Orientation of X : " + str(input_drone_coordinates.pose.orientation.x))
	    		print("Orientation of Y : " + str(input_drone_coordinates.pose.orientation.y))
	    		print("Orientation of Z : " + str(input_drone_coordinates.pose.orientation.z)) 	
            	
			for block in self._blockListDict.itervalues():
                		blockName = str(block._name)
				if blockName!="iris_1" :
					arm_pub = rospy.Publisher("gazebo/iris_1/distances", Int32, queue_size=10)
					print "current model"
                			resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
                			print '\n'
                			print 'Status.success = ', resp_coordinates.success
                			print(blockName)
                			print("Cube " + str(block._name))
                			print("Position of X : " + str(resp_coordinates.pose.position.x))
					print("Position of Y : " + str(resp_coordinates.pose.position.y))
					print("Position of Z : " + str(resp_coordinates.pose.position.z))
                			print("Orientation of X : " + str(resp_coordinates.pose.orientation.x))
					print("Orientation of Y : " + str(resp_coordinates.pose.orientation.y))
					print("Orientation of Z : " + str(resp_coordinates.pose.orientation.z))
					#distance = PoseStamped()
					#distance.header.frame_id = blockname+"/base_link"
					#distance.header.stamp = rospy.Time.now()
					#distance.pose.position.x = distance.euclidean(resp_coordinates.pose.position.x,input_drone_coordinates.x)
					#distance.pose.position.y = distance.euclidean(resp_coordinates.pose.position.y,input_drone_coordinates.y)
					#distance.pose.position.z = distance.euclidean(resp_coordinates.pose.position.z,input_drone_coordinates.z)
					arm_pub.publish(1)
					rospy.sleep(2)

    except rospy.ServiceException as e:
	rospy.loginfo("Get Model State service call failed:  {0}".format(e))
	
		


if __name__ == '__main__':
    tuto = Tutorial()
    tuto.show_gazebo_models()

