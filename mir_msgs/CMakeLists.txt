cmake_minimum_required(VERSION 2.8.3)
project(mir_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  geometry_msgs
)

################################################
## Declare ROS messages, services and actions ##
################################################

# Generate messages in the 'msg' folder
add_message_files(
  FILES
    Encoders.msg
    Error.msg
    ExternalRobot.msg
    ExternalRobots.msg
    HookStatus.msg
    LocalMapStat.msg
    MirExtra.msg
    MissionCtrlCommand.msg
    MissionCtrlState.msg
    Path.msg
    Pose2D.msg
    RobotMode.msg
    RobotState.msg
    RobotStatus.msg
    Serial.msg
    StampedEncoders.msg
    Trolley.msg
    Twist2D.msg
    UserPrompt.msg
    WebPath.msg
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
    geometry_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS
    message_runtime
    geometry_msgs
)
