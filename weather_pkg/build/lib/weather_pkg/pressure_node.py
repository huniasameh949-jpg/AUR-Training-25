#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class PressPublisher(Node):
    def __init__(self,):
        super().__init__('pressure_node')
        self.get_logger().info("press node started")
        self.presspublisher=self.create_publisher(Int32,'test_topic3',10)
        self.timer=self.create_timer(3,self.presspublisher_callback)

    def presspublisher_callback(self):
        press=Int32()
        press.data=randint(900,1100)
        self.presspublisher.publish(press)
        self.get_logger().info(f'publishing:{press.data}')
        

def main():
    rclpy.init()
    node=PressPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()