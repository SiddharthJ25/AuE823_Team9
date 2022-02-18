# AuE823_Team9
## File System
  **catkin_ws**
      - build
      - devel
      - src
        - assignment3_turtlebot3
          - src
            - scripts
              - circle.py
              - move_brake.py
              - square.py
            - launch
              - move.launch :- launch file to move the turtlebot3 with scritps circle.py or square.py
              - move_brake.launch :- launch file to move the turtlebot3 in a straight line until it detects an obstacle
          - worlds
              lab4_turtlebot3   # copy to the worlds folder in your gazebo path
              turtlebot3_wall   # copy to the worlds folder in your gazebo path
              lab4_turtlebot3.world   # copy to the worlds folder in your gazebo path
              turtlebot3_wall.world   # copy to the worlds folder in your gazebo path
          
          - videos
            - Turtlebot3_brake
            - Turtlebot3_circle
            - Turtlebot3_square
