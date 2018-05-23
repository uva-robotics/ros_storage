cmake_minimum_required(VERSION 2.8.3)
project(ros_storage)

find_package(catkin REQUIRED COMPONENTS
  rospy
# roscpp
#  test_pkg_msg
)

catkin_python_setup()

catkin_package()

install(PROGRAMS
  src/main.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
