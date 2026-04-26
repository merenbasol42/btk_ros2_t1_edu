import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from example_interfaces.srv import SetBool

class MyNode(Node):
    def __init__(self):
        super().__init__("motor")
        self.create_subscription(Int32, "sicaklik", self.sicaklik_geldi, 10)
        self.client = self.create_client(SetBool, "on_off")

        while not self.client.wait_for_service(0.5):
            print("servisi bekliyorum")

    def sicaklik_geldi(self, msg: Int32):
        if msg.data > 30:
            istek = SetBool.Request()
            istek.data = False
            self.client.call_async(istek)
        elif msg.data < 15:
            istek = SetBool.Request()
            istek.data = True
            self.client.call_async(istek)

def main():
    rclpy.init()

    n = MyNode()

    rclpy.spin(n)