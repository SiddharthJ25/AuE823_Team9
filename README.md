# AuE823_Team9
## File System
   - **Tb3_Sim2Real**
      - 1_sim2real_screenrecording.mp4
      - 1_sim2real_tb3.mp4
      - 2_Screen_Recording.mkv
      - 2_Teleop_tb3.mp4
   - **Tb3_Teleop**
      - 1_Screen_Recording.mkv
      - 1_Teleop_tb3.mp4
      - 2_Screen_Recording.mkv
      - 2_Teleop_tb3.mp4
      
   - **catkin_ws**
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
              - lab4_turtlebot3   # copy to the worlds folder in your gazebo path
              - turtlebot3_wall   # copy to the worlds folder in your gazebo path
              - lab4_turtlebot3.world   # copy to the worlds folder in your gazebo path
              - turtlebot3_wall.world   # copy to the worlds folder in your gazebo path
          
          - videos
            - Turtlebot3_brake.mp4
            - Turtlebot3_circle.mp4
            - Turtlebot3_square.mp4
