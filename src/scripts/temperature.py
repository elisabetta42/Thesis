#!/usr/bin/env python
import rospy
import math
import numpy 
from std_msgs.msg    import Float64
from gazebo_msgs.srv import GetModelState
class Temperature:
	
   def temperature_sensor(self,uav_name):
	a=600
	b=4
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "base_link")	
	c_x=input_drone_coordinates.pose.position.x
 	c_y=input_drone_coordinates.pose.position.y
	fire_x=0.0
	fire_y=0.0
	distance=math.sqrt(pow((c_x - fire_x), 2) + pow((c_y - fire_y), 2))
	print distance
	temperature=a/(distance+b)
	print temperature
	return temperature
def main():
	 rospy.init_node('temperature')
	 temp=Temperature()
	 while True:
		 uav_name="iris_1"
		 temp_publisher = rospy.Publisher("/gazebo/"+uav_name+"/temperature", Float64,queue_size=1000)
		 iris_1_temp=temp.temperature_sensor(uav_name)
		 temp_publisher.publish(iris_1_temp)		
	         
		 uav_name="iris_2"
		 temp_publisher = rospy.Publisher("/gazebo/"+uav_name+"/temperature", Float64,queue_size=1000)
		 iris_2_temp=temp.temperature_sensor(uav_name)
		 temp_publisher.publish(iris_2_temp)

		 uav_name="iris_3"
		 temp_publisher = rospy.Publisher("/gazebo/"+uav_name+"/temperature", Float64,queue_size=1000)
		 iris_3_temp=temp.temperature_sensor(uav_name)
		 temp_publisher.publish(iris_3_temp)
		
		
		
if __name__ == '__main__':
    main()


