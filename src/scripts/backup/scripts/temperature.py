#!/usr/bin/env python
import rospy
import math
import numpy 
from std_msgs.msg    import Float64
from gazebo_msgs.srv import GetModelState
class Temperature:
	
   def temperature_sensor(self,uav_name):
	value=[]
	a=600
	b=4
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    	input_drone_coordinates = model_coordinates(uav_name, "base_link")	
	c_x=input_drone_coordinates.pose.position.x
 	c_y=input_drone_coordinates.pose.position.y
	fire_x=0.0
	fire_y=0.0
	distance=math.sqrt(pow((c_x - fire_x), 2) + pow((c_y - fire_y), 2))
	print "distance:"
	print distance
	temperature=a/(distance+b)
	print "temperature"
	print temperature
	value.append(temperature)
	value.append(distance)
	return value
	
def main():
	 rospy.init_node('temperature')
	 temp=Temperature()
	 while True:
		 uav_name="iris_1"
		 temp_publisher_1 = rospy.Publisher("/gazebo/"+uav_name+"/temperature", Float64,queue_size=1000)
		 dist_publisher_1 = rospy.Publisher("/gazebo/"+uav_name+"/fire_dist", Float64,queue_size=1000)
		 result=temp.temperature_sensor(uav_name)
		 temp_publisher_1.publish(result[0])
	         #dist_publisher_1.publish(result[1])		
	         
		 uav_name="iris_2"
		 temp_publisher_2 = rospy.Publisher("/gazebo/"+uav_name+"/temperature", Float64,queue_size=1000)
	         dist_publisher_2 = rospy.Publisher("/gazebo/"+uav_name+"/fire_dist", Float64,queue_size=1000)
		 iris_2_temp,iris_2_distance=temp.temperature_sensor(uav_name)
		 result=temp.temperature_sensor(uav_name)
		 temp_publisher_2.publish(result[0])
	         #dist_publisher_2.publish(result[1])

		 uav_name="iris_3"
		 temp_publisher_3 = rospy.Publisher("/gazebo/"+uav_name+"/temperature", Float64,queue_size=1000)
		 dist_publisher_3 = rospy.Publisher("/gazebo/"+uav_name+"/fire_dist", Float64,queue_size=1000)
		 result=temp.temperature_sensor(uav_name)
		 temp_publisher_3.publish(result[0])
	         #dist_publisher_3.publish(result[1])
		
		
		
if __name__ == '__main__':
    main()


