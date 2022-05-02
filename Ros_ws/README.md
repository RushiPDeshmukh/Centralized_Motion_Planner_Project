# How to Run ROS for the project
Clone the git repository, 
check if you are in the folder Ros_ws if not cd Ros_ws

Run catkin_make

source devel/setup.bash

### Start the planner 
$ roslaunch car planner.launch

### Start the simulator 
Open different terminal
$ roslaunch car simulator.launch

### Start the car clients
Open different terminal
To check for one single car : $ roslaunch car car.launch

To Run multiple cars 
cd ~\Centralized_Motion_Planner_Project
bash run_multiple.sh

