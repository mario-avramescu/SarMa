install the robot:
- sudo apt install ros-noetic-husky-desktop ros-noetic-husky-simulator ros-noetic-husky-navigation

topics_quiz:
....

services_quiz:
....
- Start robot: roslaunch husky_gazebo husky_playpen.launch
- Launch server: roslaunch services_quiz services_server.launch
- Launch client: roslaunch services_quiz services_client.launch

actions_quiz:
....
- Start drone: roslaunch ardrone_gazebo single_ardrone.launch
- Launch server: roslaunch actions_quiz server_drone.launch
- Launch client: rostopic pub /drone_action/goal actions_quiz/SarmaActionGoal [TAB][TAB] (set goal: 'TAKEOFF'" or 'LAND'")
