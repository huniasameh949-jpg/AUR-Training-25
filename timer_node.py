#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

class TimerNode(Node):
    def __init__(self):
        super().__init__('timer_node')
        self.counter=10
        self.timer=self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f"{self.counter}")
        if(self.counter==0):
            self.get_logger().info("Time is up!")
            rclpy.shutdown()
        else:
            self.counter-=1

def main():
    rclpy.init()
    node=TimerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
        