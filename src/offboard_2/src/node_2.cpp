/**
 * @file offb_node.cpp
 * @brief Offboard control example node, written with MAVROS version 0.19.x, PX4 Pro Flight
 * Stack and tested in Gazebo SITL
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/TwistStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include "gazebo_msgs/GetModelState.h"
#include "gazebo_msgs/SetModelState.h"
#include "gazebo_msgs/ModelState.h"
#include <mavros_msgs/State.h>
#include <iostream>
#include "std_msgs/String.h"
 
using namespace std;

mavros_msgs::State current_state;
ros::Publisher local_pos_pub;
ros::Publisher local_vel_pub;
gazebo_msgs::GetModelState getmodelstate;
geometry_msgs::TwistStamped pose;
geometry_msgs::PoseStamped pose1;
ros::ServiceClient gms_c;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}
void move_drone_callback(const std_msgs::String::ConstPtr& msg)
  {
	 gms_c.call(getmodelstate);
	 //ROS_INFO("I heard: [%s]", msg->data.c_str());
	//switch (str2int(msg->data.c_str())) {
        if(string(msg->data.c_str()).compare("right")== 0){
            ROS_INFO("It pressed right");
	    pose1.pose.position.x = getmodelstate.response.pose.position.x+1;
    	    pose1.pose.position.y = getmodelstate.response.pose.position.y;
            pose1.pose.position.z = getmodelstate.response.pose.position.z;
            }
        else if(string(msg->data.c_str()).compare("left")== 0){
            ROS_INFO("It pressed left");
	    pose1.pose.position.x = getmodelstate.response.pose.position.x-1;
    	    pose1.pose.position.y = getmodelstate.response.pose.position.y;
            pose1.pose.position.z = getmodelstate.response.pose.position.z;
           }
        else if(string(msg->data.c_str()).compare("up")== 0){
            ROS_INFO("It pressed up");
            pose1.pose.position.x = getmodelstate.response.pose.position.x;
    	    pose1.pose.position.y = getmodelstate.response.pose.position.y+1;
            pose1.pose.position.z = getmodelstate.response.pose.position.z;
            }
	 else if (string(msg->data.c_str()).compare("down")== 0){
            ROS_INFO("It pressed down");
            pose1.pose.position.x = getmodelstate.response.pose.position.x;
    	    pose1.pose.position.y = getmodelstate.response.pose.position.y-1;
            pose1.pose.position.z = getmodelstate.response.pose.position.z;
          }
         else ROS_INFO("command not implemented");
	 local_pos_pub.publish(pose1);

  }
void move_drone_to_target_callback(const geometry_msgs::TwistStamped::ConstPtr& msg)
{
	pose.twist.linear.x =  msg->twist.linear.x;
    	pose.twist.linear.y =  msg->twist.linear.y;
        pose.twist.linear.z =  msg->twist.linear.z;
	ROS_INFO("setpoint recent: %.1f, %.1f, %.1f", pose.twist.linear.x, pose.twist.linear.y, pose.twist.linear.z);
 
}


int main(int argc, char **argv)
{
    std::cout<<argv[0]<<"passed argument";
    ros::init(argc, argv, "offb2_node");
    ros::NodeHandle nh;
    
    
    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("iris_2/mavros/state", 1000, state_cb);
    local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("iris_2/mavros/setpoint_position/local", 1000);
    local_vel_pub = nh.advertise<geometry_msgs::TwistStamped>
            ("iris_2/mavros/setpoint_velocity/cmd_vel", 1000);
    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>
            ("iris_2/mavros/cmd/arming");
    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>
            ("iris_2/mavros/set_mode");

    gms_c = nh.serviceClient<gazebo_msgs::GetModelState>("/gazebo/get_model_state");
    ros::Subscriber sub = nh.subscribe("/gazebo/iris_2/command", 1000, move_drone_callback);
    ros::Subscriber destination = nh.subscribe("gazebo/iris_2/go_to_destination", 1000, move_drone_to_target_callback);
    getmodelstate.request.model_name="iris_2";
    gms_c.call(getmodelstate);
    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    // wait for FCU connection
    while(ros::ok() && current_state.connected){
        ros::spinOnce();
        rate.sleep();
    }
    //send a message to move to move drone position
    //pose1.pose.position.x = getmodelstate.response.pose.position.x;
    //pose1.pose.position.y = getmodelstate.response.pose.position.y;
    pose1.pose.position.z = 1;
    ROS_INFO("initial setpoint: %.1f, %.1f, %.1f", pose1.pose.position.x, pose1.pose.position.y, pose1.pose.position.z);
    //ROS_INFO("setpoint recent: %.1f, %.1f, %.1f", pose.twist.linear.x, pose.twist.linear.y, pose.twist.linear.z);
 
    //send a few setpoints before starting
    for(int i = 100; ros::ok() && i > 0; --i){
        local_pos_pub.publish(pose1);
        ros::spinOnce();
        rate.sleep();
    }

    mavros_msgs::SetMode offb_set_mode;
    offb_set_mode.request.custom_mode = "OFFBOARD";
   
    mavros_msgs::CommandBool arm_cmd;
    arm_cmd.request.value = true;

    ros::Time last_request = ros::Time::now();

    while(ros::ok()){
        if( current_state.mode != "OFFBOARD" &&
            (ros::Time::now() - last_request > ros::Duration(5.0))){
            if( set_mode_client.call(offb_set_mode) &&
                offb_set_mode.response.mode_sent){
                ROS_INFO("Offboard enabled");
            }
            last_request = ros::Time::now();
        } else {
            if( !current_state.armed &&
                (ros::Time::now() - last_request > ros::Duration(5.0))){
                if( arming_client.call(arm_cmd) &&
                    arm_cmd.response.success){
                    ROS_INFO("Vehicle armed");
                   
                }
                last_request = ros::Time::now();
            }
        }
     	//ROS_INFO("I am here");
	//ROS_INFO("setpoint: %.1f, %.1f, %.1f", pose.pose.position.x, pose.pose.position.y, pose.pose.position.z);
	local_vel_pub.publish(pose);
	//local_pos_pub.publish(pose1);	
	ros::spinOnce();
        rate.sleep();
    }

    return 0;
}
