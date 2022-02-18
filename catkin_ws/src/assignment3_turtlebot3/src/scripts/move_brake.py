#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Turtlebot3_brake:
    def __init__(self):
        rospy.init_node('turtlebot_brake', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.scanner = rospy.Subscriber('/scan', LaserScan, self.warn_me)
        self.rate = rospy.Rate(10)
        self.scan_data = LaserScan()
        self.warn = 0
    
    def warn_me(self, data):
        self.scan_data = data
        if self.scan_data.ranges[0] <= 1.5: 
            self.warn = 1
    
    def move_brake(self):
        """ Moves the turtlebot in constant twist velocity, with emergency braking functionality"""
        vel_msg = Twist()
        while not rospy.is_shutdown():
            while self.warn ==0:
                # Linear velocity along the robots x axis
                vel_msg.linear.x = 0.3
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()
                
            vel_msg.linear.x = 0
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            
        rospy.spin()


if __name__ == '__main__':
    try:
        x = Turtlebot3_brake()
        x.move_brake()
    except rospy.ROSInterruptException:
        pass

