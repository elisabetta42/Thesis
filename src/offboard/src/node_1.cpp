/**
 * @file offb_node.cpp
 * @brief Offboard control example node, written with MAVROS version 0.19.x, PX4 Pro Flight
 * Stack and tested in Gazebo SITL
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include "gazebo_msgs/GetModelState.h"
#include <mavros_msgs/State.h>
#include <iostream>
#include "std_msgs/String.h"
 
using namespace std;

mavros_msgs::State current_state;
ros::Publisher local_pos_pub;
gazebo_msgs::GetModelState getmodelstate;
geometry_msgs::PoseStamped pose;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}
void move_drone_callback(const std_msgs::String::ConstPtr& msg)
  {
	 //ROS_INFO("I heard: [%s]", msg->data.c_str());
	//switch (str2int(msg->data.c_str())) {
        if(string(msg->data.c_str()).compare("right")== 0){
            ROS_INFO("It pressed right");
	    pose.pose.position.x = getmodelstate.response.pose.position.x+1;
    	    pose.pose.position.y = getmodelstate.response.pose.position.y;
            pose.pose.position.z = getmodelstate.response.pose.position.z+1;
            }
        else if(string(msg->data.c_str()).compare("left")== 0){
            ROS_INFO("It pressed left");
	    pose.pose.position.x = getmodelstate.response.pose.position.x-1;
    	    pose.pose.position.y = getmodelstate.response.pose.position.y;
            pose.pose.position.z = getmodelstate.response.pose.position.z+1;
           }
        else if(string(msg->data.c_str()).compare("up")== 0){
            ROS_INFO("It pressed up");
            pose.pose.position.x = getmodelstate.response.pose.position.x;
    	    pose.pose.position.y = getmodelstate.response.pose.position.y+1;
            pose.pose.position.z = getmodelstate.response.pose.position.z+1;
            }
	 else if (string(msg->data.c_str()).compare("down")== 0){
            ROS_INFO("It pressed down");
            pose.pose.position.x = getmodelstate.response.pose.position.x;
    	    pose.pose.position.y = getmodelstate.response.pose.position.y-1;
            pose.pose.position.z = getmodelstate.response.pose.position.z+1;
          }
         else ROS_INFO("command not implemented");

  }
void move_drone_to_target_callback(const geometry_msgs::PoseStamped::ConstPtr& msg)
{
	pose.pose.position.x =  msg->pose.position.x;
    	pose.pose.position.y =  msg->pose.position.y;
        pose.pose.position.z =  msg->pose.position.z;
}


int main(int argc, char **argv)
{
    std::cout<<argv[0]<<"passed argument";
    ros::init(argc, argv, "offb1_node");
    ros::NodeHandle nh;

    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("iris_1/mavros/state", 10, state_cb);
    local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("iris_1/mavros/setpoint_position/local", 10);
    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>
            ("iris_1/mavros/cmd/arming");
    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>
            ("iris_1/mavros/set_mode");
    ros::ServiceClient gms_c = nh.serviceClient<gazebo_msgs::GetModelState>("/gazebo/get_model_state");
    ros::Subscriber sub = nh.subscribe("/gazebo/iris_1/command", 1000, move_drone_callback);
    ros::Subscriber destination = nh.subscribe("gazebo/iris_1/go_to_destination", 1000, move_drone_to_target_callback);
    
    gms_c.call(getmodelstate);

    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    // wait for FCU connection
    while(ros::ok() && current_state.connected){
        ros::spinOnce();
        rate.sleep();
    }
    //send a message to move to move drone position
   
    pose.pose.position.x = getmodelstate.response.pose.position.x;
    pose.pose.position.y = getmodelstate.response.pose.position.y;
    pose.pose.position.z = getmodelstate.response.pose.position.z+1;
    //send a few setpoints before starting
    for(int i = 100; ros::ok() && i > 0; --i){
        local_pos_pub.publish(pose);
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
	local_pos_pub.publish(pose);
        ros::spinOnce();
        rate.sleep();
    }

    return 0;
}
