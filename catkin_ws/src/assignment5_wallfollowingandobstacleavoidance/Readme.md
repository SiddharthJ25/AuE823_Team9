

This is the package for the 5th assignment: wall following and obstacle avoidance.

src:
	scripts: contains the scripts for obstacle avoidance (wander.py) and wall following (wall_follower.py)
	launch: launches the world files in gazebo for obstacle avaoidance ((turtlebot3_obstacles.launch) and wall folloing (turtlebot3_wallfollowing.launch)
	videos: contains the videos of the execution of wall follower and obstacle avoidance in simulation and the video for real world obstacle avoidance using the turtlebot3 Burger
	
Running process:
	Wall follower:
		Commamds: roslaunch turtlebot3_gazebo turtlebot3_wallfollowing.launch # launches the gazebo world
			rosrun assignment5_wallfollowingandobstacleavoidance wall_follower.py # Runs the wall followingscript
			
	Obstacle avoidance:
		Commands: roslaunch turtlebot3_gazebo turtlebot3_obstacles.launch # launches the obstacles world
			rosrun assignment5_wallfollowingandobstacleavoidance wander.py # Runs the obstacle avoidance script



