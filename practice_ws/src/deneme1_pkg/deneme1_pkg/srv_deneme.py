import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts



class MyNode(Node):
    def __init__(self):
        super().__init__("benim_node")
        self.create_service(AddTwoInts, "carpim", self.srv_arandi)

    def srv_arandi(self, istek: AddTwoInts.Request, yanit: AddTwoInts.Response) -> AddTwoInts.Response:
        yanit.sum = istek.a * istek.b
        return yanit
    

def main():
    rclpy.init()

    n = MyNode()
    rclpy.spin(n)