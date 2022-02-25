# Centralized_Motion_Planner_Project
Localized motion planning on-board an Autonomous Vehicle (AV) using SLAM (Simultaneous Localization and Mapping) has been implemented. This individual motion planning of the route by AVs does not account for other AVs' routes, urgency, other such parameters and can lead to deadlock situations. A centralized computation unit that provides the registered AVs with a optimal motion plan is proposed by this project. A central planner will find a optimal motion plan for all the AVs in its control area. This central planner will consider the fuel constraint, priorities, speed constraint, etc while planning. This project proposes the use of Particle Swarm Optimization algorithm for meta-heuristic centralized decoupled motion planning. A classic decoupled centralized motion planning algorithm will be implemented for baseline comparison. Advanced algorithm like Grey Wolf Optimization will be studied and explored in the project.



/src/Simulator/  Folder contains:
     simulatorv0.py which is used to create city maps of class BLOCKS stored in map.pkl using pickle.
    map.pkl contains a city map can be open and edited to change the roads and orientations of roads. 
    grid.py contains a class function of GRID. This will be used to represent the city map in 150x150 grid.
    grid_tile.py contains a class function of GRIDTILE. This will be used to represent the singel tile on the grid.
    map_grid.npy file contains a numpy array of size (150,150). This will be used to initialize the grid object for now.
    
