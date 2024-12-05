cmake_minimum_required(VERSION 3.0.2)
project(gazebosensorplugins)

# set(CMAKE_AUTOMOC ON)
# set(CMAKE_AUTOUIC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -std=c++11")


# add_definitions(-std=c++11)


## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roscpp
  std_msgs
  gtec_msgs
  tf
)

# Depend on system install of Gazebo
find_package(gazebo REQUIRED)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})

add_library(gtec_uwb_plugin src/UwbPlugin.cpp)
target_link_libraries(gtec_uwb_plugin ${catkin_LIBRARIES} ${GAZEBO_LIBRARIES} ${Boost_LIBRARIES})
add_dependencies(gtec_uwb_plugin ${catkin_EXPORTED_TARGETS})

catkin_package(
  DEPENDS 
    roscpp 
    gazebo_ros
    gtec_msgs
)
##add_dependencies(${PROJECT_NAME} gtec_generate_messages_cpp)

# set(CUSTOM_INSTALL_DIR "/opt/ros/noetic/lib")
# install(TARGETS gtec_uwb_plugin
#   LIBRARY DESTINATION ${CUSTOM_INSTALL_DIR}
# )

# # Install the library to a custom folder
# set(CUSTOM_INSTALL_DIR "/home/cyy/PX4_Firmware/build/px4_sitl_default/build_gazebo")
# install(TARGETS gtec_uwb_plugin
#   LIBRARY DESTINATION ${CUSTOM_INSTALL_DIR}
# )
