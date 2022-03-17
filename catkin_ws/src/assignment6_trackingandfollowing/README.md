# Tracking and following
This is the submission for assignment 6 "Tracking and following"

## Package: **assignment6_trackingandfollowing**

### Files and folders:
**src:**
	- **launch:**
		- *turtlebot3_follow_line.launch*: Used to launch the gazebo world to run line following simulation
	- **scripts:**
		- *follow_line_step_hsv.py*: main script for line following which reads the video stream and applies a PD controller to follow the line
		- *move_robot.py*: Creates a "MoveTurtlebot3()" object and has the "move_robot()" function
		- *line_follower_basics.py*: to test if the camera simulation is working
	- **videos:**
		- *sim_linefollowing-2022-03-17_08.25.41.mkv*: Shows the execution of the line follower simulation

### Execution:
**Line follower simulation:**
- Launching the gazebo environment:
	>roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch

	![github image](https://github.com/sid25j/AuE823_Team9/blob/main/catkin_ws/src/assignment6_trackingandfollowing/src/videos/images/roslaunch_gazebo.PNG)

- Running the line following script:
	>rosrun assignment6_trackingandfollowing follow_line_step_hsv.py

	![github image](https://github.com/sid25j/AuE823_Team9/blob/main/catkin_ws/src/assignment6_trackingandfollowing/src/videos/images/sim_execution.PNG)
