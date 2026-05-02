import rclpy
from rclpy.node import Node

from benim_arayuzler.msg import SensorVerisi


class MyNode(Node):
    def __init__(self):
        super().__init__("gozlemci")
        self.pubber = self.create_publisher(SensorVerisi, "sensor", 10)

        self.create_timer(1.0, self.timer_cb)

    def timer_cb(self):
        msg = SensorVerisi()
        msg.sicaklik = 50.0
        msg.batarya = 50.0

        self.pubber.publish(msg)

def main():
    rclpy.init()

    n = MyNode()

    rclpy.spin(n)