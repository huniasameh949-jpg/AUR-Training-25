#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class HumPublisher(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.get_logger().info("hum node started")
        self.publisherhum=self.create_publisher(Int32,'test_topic2',10)
        self.timer=self.create_timer(2,self.publisherhum_callback)

    def publisherhum_callback(self):
        hum=Int32()
        hum.data=randint(20,100)
        self.publisherhum.publish(hum)
        self.get_logger().info(f'publishing:{hum.data}')
        
        
    

def main():
    rclpy.init()
    node=HumPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()




