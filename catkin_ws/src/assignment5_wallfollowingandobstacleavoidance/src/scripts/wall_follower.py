#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pow, atan2, sqrt, inf, cos, sin
from numpy import mean, radians

class TurtleBot:

	def __init__(self):
		rospy.init_node('turtlebot_wall_following', anonymous=True)
		self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		self.scan_subscriber = rospy.Subscriber('/scan', LaserScan, self.scan_subs)
		self.rate1 = rospy.Rate(10)
		self.rate2 = rospy.Rate(10)
		self.scan_data = LaserScan()
		self.vel_msg = Twist()
		
		self.right = 3.5
		self.left = 3.5
		self.base_vel = 0.6
		
		self.kp = 0.75
		self.kd = 0
		self.angular_vel = 0

	

	def scan_subs(self, data):
		print ("left distance is:", data.ranges[90])
		print ("right distance is:", data.ranges[270])
		x = data.ranges[90]
		y = data.ranges[270]
		deviation = round(x-y,4)
		print("Deviation from center line",deviation)
		self.left = data.ranges[20:90]
		self.right = data.ranges[-90:-20]
		self.right = [3.5 if x >= 3.5 else x for x in self.right]
		self.right = mean(self.right)
		self.left = [3.5 if x >= 3.5 else x for x in self.left]
		self.left = mean(self.left)
		#print("Left = ", self.left,"Right = ", self.right)
		self.rate2.sleep()

	def pid(self):
		error = self.left-self.right
		#print("error= ", error)
		self.rate2.sleep()
		return self.kp*error

		
	#def angular_vel(self, steer_angle, constant=1):
		"""See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
		#return constant * (steer_angle)


	def wall_follow(self):
		
		while not rospy.is_shutdown():

			
			self.vel_msg.linear.x = self.base_vel
			self.angular_vel = self.pid()
			self.vel_msg.angular.z = self.angular_vel
			#print("The angular velocity is: ",self.angular_vel)
			self.vel_pub.publish(self.vel_msg)
			self.rate1.sleep()

		rospy.spin()


if __name__ == '__main__':
	try:
		x = TurtleBot()
		x.wall_follow()
	except rospy.ROSInterruptException:
		pass
