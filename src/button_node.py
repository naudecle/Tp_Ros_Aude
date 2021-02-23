#!/usr/bin/env python
from std_msgs.msg import Bool
from Tkinter import *
import rospy



class RosButton:
	def __init__(self):
		self.master=Tk()
		self.master.geometry("100x100")
		rospy.init_node("button_gui")
		self.pub=rospy.Publisher("button_state",Bool,queue_size=1)
		self.state=True
		self.pub.publish(self.state)
		b=Button(self.master, text="Toggle", command=self.callback)
		b.pack()
		mainloop()
	
	def callback(self):
		self.state= not self.state
		self.pub.publish(self.state)
	
	def exit(self):
		self.master.destroy()
		print("EXITING")

if __name__ == "__main__":
	
	button=RosButton()
		
