# Centralized_Motion_Planner_Project
Localized motion planning on-board an Autonomous Vehicle (AV) using SLAM (Simultaneous Localization and Mapping) has been implemented. This individual motion planning of the route by AVs does not account for other AVs' routes, urgency, other such parameters and can lead to deadlock situations. A centralized computation unit that provides the registered AVs with a optimal motion plan is proposed by this project. A central planner will find a optimal motion plan for all the AVs in its control area. This central planner will consider the fuel constraint, priorities, speed constraint, etc while planning. This project proposes the use of Particle Swarm Optimization algorithm for meta-heuristic centralized decoupled motion planning. A classic decoupled centralized motion planning algorithm will be implemented for baseline comparison. Advanced algorithm like Grey Wolf Optimization will be studied and explored in the project.

__Simple APlanning Working__:                                                                                                             
<img width="504" alt="image" src="https://user-images.githubusercontent.com/98420717/191346375-0e4a4c9b-e24c-496e-a2a2-69d6da4a3c8b.png">

__Simulation Environment Designed in Pygame__:
![image](https://user-images.githubusercontent.com/98420717/191346472-04637c81-29c3-48f4-b8d8-687777a7669e.png)

__Results__:

1. __Naive A* Planner__: 

https://user-images.githubusercontent.com/98420717/191366767-d91d5675-a8e0-4b5d-9974-764040422812.mov

2. __Priotize Safe Interval based Planner__:

https://user-images.githubusercontent.com/98420717/191366912-0ce801f0-f7e5-4e99-99fa-3136cc73e4cd.mov

3. __Combinational Planner__:

https://user-images.githubusercontent.com/98420717/191367500-de3362df-e3b4-4dd6-8b0c-a30845d855cb.mov

Performance Graph

![image](https://user-images.githubusercontent.com/98420717/191367593-990f36b1-6d85-499d-9139-5ce5ac899bf3.png)







/src/Simulator/  Folder contains:

    simulatorv0.py: used to create city maps of class BLOCKS stored in map.pkl using pickle.
    
    map.pkl: contains a city map can be open and edited to change the roads and orientations of roads. 
    
    grid.py: contains a class function of GRID. This will be used to represent the city map in 150x150 grid.
    
    grid_tile.py: contains a class function of GRIDTILE. This will be used to represent the singel tile on the grid.
    
    map_grid.npy: file contains a numpy array of size (150,150). This will be used to initialize the grid object for now.
    
### Requirements
The version is tested on ubuntu 20.04 using python 3.8.10

* pygame 2.1.2
* ROS noetic

### Instructions to run the REPO

git clone https://github.com/wokeengineer/Centralized_Motion_Planner_Project.git

cd Ros_ws

For further instructions follow the README in the Ros_ws folder.
