import rclpy
from rclpy.node import Node

from benim_arayuzler.msg import MotorBilgileri



class MyNode(Node):
    def __init__(self):
        super().__init__("benim_node")
        self.pubber = self.create_publisher(MotorBilgileri, "motor_stats", 10)
        self.create_timer(1.0, self.timer_cb)

    def timer_cb(self):
        msg = MotorBilgileri()
        msg.sicaklik = 1.0
        msg.acik_mi = True
        self.pubber.publish(msg)


def main():
    rclpy.init()
        
    n = MyNode()

    rclpy.spin(n)
