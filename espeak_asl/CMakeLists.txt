cmake_minimum_required(VERSION 2.8.3)
project(espeak_asl)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs std_srvs message_generation)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(CATKIN_DEPENDS rospy std_msgs std_srvs message_runtime
#  DEPENDS system_lib
)
