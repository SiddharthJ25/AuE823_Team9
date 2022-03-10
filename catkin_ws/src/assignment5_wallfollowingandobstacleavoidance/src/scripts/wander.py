#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pow, atan2, sqrt, inf 
from numpy import mean
import time

class Turtlebot3_wallfollowing:

	def __init__(self):
		rospy.init_node('turtlebot_wall_following', anonymous=True)
		self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		self.scanner = rospy.Subscriber('/scan', LaserScan, self.warn_me)
		self.rate1 = rospy.Rate(10)
		self.rate2 = rospy.Rate(10)
		self.scan_data = LaserScan()
		#self.warn = [0, 0, 0]
		self.vel_msg = Twist()
		self.front = 3.5
		self.front_min = 0.12
		self.lf = 3.5
		self.right = 3.5
		self.rf = 3.5
		self.left = 3.5
		self.skip = 0
		

	def warn_me(self,data):
		self.scan_data = data
		self.front = self.scan_data.ranges[0:20] + self.scan_data.ranges[-20:]
		self.front = [x if x < 3.5 else 3.5 for x in self.front]
		dummy = sorted(self.scan_data.ranges[-85:]+self.scan_data.ranges[0:85])[:5]
		if mean(dummy) < 0.3:
			#self.front_min = mean(dummy)
			self.skip = 1
			#print("skip")
			#self.front_min = mean(self.front_min)
		else:
			self.skip = 0
		
		self.front_min = sorted(self.front)[:5]
		self.front_min = mean(self.front_min)

		self.front = mean(self.front)
		print("Front = ", self.front)
		print("Front Minimum = ", self.front_min)

		self.left = self.scan_data.ranges[45:90]
		self.left = [3.5 if x >= 3.5 else x for x in self.left]
		self.left = mean(self.left)
		print("Left = ", self.left)
		
		self.right = self.scan_data.ranges[-90:-45]
		self.right = [3.5 if x >= 3.5 else x for x in self.right]
		self.right = mean(self.right)
		print("	right = ", self.right)

		self.rf = self.scan_data.ranges[-45:-15]
		self.rf = [3.5 if x >= 3.5 else x for x in self.rf]
		self.rf = mean(self.rf)
		print("	right front = ", self.rf)

		self.lf = self.scan_data.ranges[15:45]
		self.lf = [3.5 if x >= 3.5 else x for x in self.lf]
		self.lf = mean(self.lf)
		print("	left front = ", self.lf)

		self.rate2.sleep()


	def wander(self):

		while not rospy.is_shutdown():

			#if max(self.front,self.right,self.left,self.rf,self.lf)==self.front:
			#if self.front > 1:
			if self.front_min<0.5 and self.skip != 1 :#and self.rf<1 and self.lf<1:
				
				#flag = 0
				self.vel_msg.linear.x = 0
				self.vel_msg.angular.z = 0
				self.vel_pub.publish(self.vel_msg)

				while max(self.front,self.right,self.left,self.rf,self.lf)==self.front:
					self.vel_msg.linear.x = 0.2
					self.vel_msg.angular.z = 0
					self.vel_pub.publish(self.vel_msg)

				while max(self.front,self.right,self.left,self.rf,self.lf)==self.lf or max(self.front,self.right,self.left,self.rf,self.lf)==self.rf:
					if max(self.front,self.right,self.left,self.rf,self.lf)==self.lf:
						self.vel_msg.linear.x = 0
						self.vel_msg.angular.z = 0.2
						self.vel_pub.publish(self.vel_msg)
						#flag = 1
						#time.sleep(2)


					else:
						#if flag == 0:
						
						self.vel_msg.linear.x = 0
						self.vel_msg.angular.z = -0.3
						self.vel_pub.publish(self.vel_msg)

				flag = 0
				while max(self.front,self.right,self.left,self.rf,self.lf)==self.left or max(self.front,self.right,self.left,self.rf,self.lf)==self.right:
					if max(self.front,self.right,self.left,self.rf,self.lf)==self.left:
						if self.skip == 1:
							self.vel_msg.linear.x = -0.1
							self.vel_msg.angular.z = -0.3
						else:
							self.vel_msg.linear.x = 0
							self.vel_msg.angular.z = 0.3

						
						self.vel_pub.publish(self.vel_msg)
						flag = 1
						#time.sleep(2)

					else:
						if self.skip == 1:
							self.vel_msg.linear.x = -0.1
							self.vel_msg.angular.z = 0.3
						else:
							self.vel_msg.linear.x = 0
							self.vel_msg.angular.z = -0.3
						#if flag == 0:
						
						self.vel_pub.publish(self.vel_msg)

			else:
				self.vel_msg.linear.x = 0.2
				self.vel_msg.angular.z = 0
				self.vel_pub.publish(self.vel_msg)

			#while self.right<self.left:
				#self.vel_msg.linear.x = 0
				#self.vel_msg.angular.z = 0.2
				#self.vel_pub.publish(self.vel_msg)

			self.rate1.sleep()

		rospy.spin()


if __name__ == '__main__':
	try:
		x = Turtlebot3_wallfollowing()
		x.wander()
	except rospy.ROSInterruptException:
		pass