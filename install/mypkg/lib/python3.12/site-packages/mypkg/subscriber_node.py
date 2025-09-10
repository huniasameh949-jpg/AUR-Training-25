#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32,Int64
from std_msgs.msg import Float32
from random import randint

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.get_logger().info("subscriber node started")
        self.subscribetemp=self.create_subscription(Int32,'test_topic1',self.sub_callbackspeed,10 )
        self.subscriberhum=self.create_subscription(Int64,'test_topic2',self.sub_callbackdistance,10 )
       
    def sub_callbackspeed(self,msg):
        self.get_logger().info(f"{msg.data} ")
    

    def sub_callbackdistance(self,msg):
        self.get_logger().info(f"{msg.data} ")
       
    
def main():
    rclpy.init()
    node=Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

