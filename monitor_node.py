#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.get_logger().info("subscriber node started")
        self.subscribetemp=self.create_subscription(Int32,'test_topic1',self.subtemp_callback,10 )
        self.subscriberhum=self.create_subscription(Int32,'test_topic2',self.subhum_callback,10 )
        self.subscriberpress=self.create_subscription(Int32,'test_topic3',self.subpress_callback,10 )

        self.file=open("weather_reading.txt","w")

    def subtemp_callback(self,temp):
        self.get_logger().info(f"{temp.data} C")
        self.file.write(f"{temp.data} C\n")

    def subhum_callback(self,hum):
        self.get_logger().info(f"{hum.data} %")
        self.file.write(f"{hum.data} %\n")

    def subpress_callback(self,press):
        self.get_logger().info(f"{press.data} hPa")
        self.file.write(f"{press.data} hPa\n")

    def destroy_node(self):
        self.file.close()
        super().destroy_node()

def main():
    rclpy.init()
    node=WeatherSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

