#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as num
from std_msgs.msg import String
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
from Tkinter import *
import time

def callback(data):
    if(data == True):
	    pub = rospy.Publisher('tp', PoseStamped, queue_size=10)
	    rospy.init_node('talker', anonymous=True)
	    rate = rospy.Rate(10) # 10hz
	    message = PoseStamped()
	    message.pose.position.x=-num.pi
	    b = True
	    while not rospy.is_shutdown():
		#hello_str = "hello world %s" % rospy.get_time()
		#rospy.loginfo(hello_str)
		#x = message.pose.position.x 

		if(b):
			if(message.pose.position.x < num.pi):

				message.pose.position.x = message.pose.position.x + 0.1
				message.pose.position.y = num.sin(message.pose.position.x)
				message.header.frame_id = "map"
				pub.publish(message)
				print(message)
				rate.sleep()
				if(message.pose.position.x >= num.pi):
					b = False
		else:
			if(message.pose.position >= num.pi):

				message.pose.position.x = message.pose.position.x - 0.1
				message.pose.position.y = -(num.sin(message.pose.position.x))
				message.header.frame_id = "map"
			      	pub.publish(message)
				print(message)
			       	rate.sleep()	
				if(message.pose.position.x < -num.pi):
					b = True


    else:
	time.sleep(2)

def talker():
   rospy.init_node('listener', anonymous=True)

   rospy.Subscriber("button_state", Bool, callback)

     
   rospy.spin()
if __name__ == '__main__':
   
    talker()
    

