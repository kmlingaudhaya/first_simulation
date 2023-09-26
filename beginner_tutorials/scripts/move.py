#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

PI = 3.1415926535897

class Movement:

    def __init__(self):
        rospy.init_node('move_robot_node', anonymous=False)
        self.pub_move = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.move = Twist()

    def publish_vel(self):
        self.pub_move.publish(self.move)

    def move_forward(self):
        self.move.linear.x = 1
        self.move.angular.z = 0.0

    def move_backward(self):
        self.move.linear.x = -1
        self.move.angular.z = 0.0

    def stop(self):
        self.move.linear.x = 0
        self.move.angular.z = 0.0

if __name__ == "__main":
    print("Before input prompt")
    rospy.init_node('rc_control', anonymous=True)
    print("Before input prompt")

    mov = Movement()
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        print("Before input prompt")
        movement = input('Enter desired movement: ')

        if movement == 'f':
            mov.move_forward()
        elif movement == 'b':
            mov.move_backward()
        elif movement == 's':
            mov.stop()
        else:
            print("Invalid movement command. Valid commands: 'f', 'b', 's'")

        mov.publish_vel()
        rate.sleep()
