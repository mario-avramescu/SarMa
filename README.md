install the robot:
- sudo apt install ros-noetic-husky-desktop ros-noetic-husky-simulator ros-noetic-husky-navigation

topics_quiz:
....

services_quiz:
....
- Start robot: roslaunch husky_gazebo husky_playpen.launch
- Launch server: roslaunch services_quiz services_server.launch
- Launch client: roslaunch services_quiz services_client.launch
