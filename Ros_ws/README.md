# How to Run ROS for the project

# TODO : Make a roslaunch

1. roscore
2. To run car / generate car nodes :
    rosrun car car_client.py 
3. To run the planenr server node to get path plans for car:
    rosrun car planner_server.py
4. To start simulation node :
    rosrun car simulator_ros.py