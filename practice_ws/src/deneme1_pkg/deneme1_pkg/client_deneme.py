import rclpy
from rclpy.node import Node
from rclpy.task import Future

from example_interfaces.srv import AddTwoInts



class MyNode(Node):
    def __init__(self):
        super().__init__("benim_node")
        self.client = self.create_client(AddTwoInts, "carpim")
        
        while not self.client.wait_for_service(0.5):
            print("servisi bekliyorum")
            
        self.create_timer(1.0, self.ara)

    def ara(self):
        istek = AddTwoInts.Request()
        istek.a = 7
        istek.b = 6
        gelecek = self.client.call_async(istek)
        gelecek.add_done_callback(self.yanit_geldi)

    def yanit_geldi(self, future: Future):
        yanit: AddTwoInts.Response = future.result()

        print(f"cevap şu: {yanit.sum}")

def main():
    rclpy.init()

    n = MyNode()
    rclpy.spin(n)