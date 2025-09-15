#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Turtle2(Node):
    def __init__(self):
        super().__init__('turtle_node')
        self.publisher=self.create_publisher(Twist,'/turtle2/cmd_vel',10)


    def move(self,key):
        msg=Twist()
        if key=='w':
            msg.linear.x=1.5
        elif key=='s':
            msg.linear.x=-1.5
        elif key=='a':
            msg.angular.z=1.5
        elif key=='d':
            msg.angular.z=-1.5
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node=Turtle2()
    print("enter moves from keyboard")
    try:
        while True:
            key=input().lower()
            if key=='q':
                break
            node.move(key)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()