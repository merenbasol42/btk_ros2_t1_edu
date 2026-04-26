import random

import rclpy
from rclpy.node import Node
from rclpy.task import Future

from example_interfaces.srv import SetBool



class MyNode(Node):
    def __init__(self):
        super().__init__("benim_node")
        res = SetBool.Response()
        res.success = True
        self.client = self.create_client(AddTwoInts, "carpim")
        
        while not self.client.wait_for_service(0.5):
            print("servisi bekliyorum")

        self.create_timer(1.0, self.ara)

    def ara(self):
        istek = AddTwoInts.Request()
        istek.a = random.randint(1, 5)
        istek.b = random.randint(5, 12)
        gelecek = self.client.call_async(istek)
        gelecek.add_done_callback(self.yanit_geldi)

    def yanit_geldi(self, future: Future):
        yanit: AddTwoInts.Response = future.result()

        print(f"cevap şu: {yanit.sum}")

def main():
    rclpy.init()

    n = MyNode()
    rclpy.spin(n)