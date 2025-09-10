#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
#from sensor_msgs.msg import Temperature
from random import randint

class TempPublisher(Node):
    def __init__(self):
        super().__init__('temperature_node')
        self.get_logger().info("temp node started")
        self.publishertemp=self.create_publisher(Int32,'test_topic1',10)
        self.timer=self.create_timer(1,self.publishertemp_callback)

    def publishertemp_callback(self):
        temp=Int32()
        temp.data=randint(15,40)
        self.publishertemp.publish(temp)
        self.get_logger().info(f'publishing:{temp.data}')
        

   
def main():
    rclpy.init()
    node=TempPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
