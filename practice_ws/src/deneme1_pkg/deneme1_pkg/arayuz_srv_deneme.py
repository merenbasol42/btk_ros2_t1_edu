import rclpy
from rclpy.node import Node

from benim_arayuzler.srv import ToplamaUc



class MyNode(Node):
    def __init__(self):
        super().__init__("benim_node")
        self.create_service(ToplamaUc, "toplama", self.srv_arandi)

    def srv_arandi(self, istek: ToplamaUc.Request, yanit: ToplamaUc.Response) -> ToplamaUc.Response:

        yanit.sonuc = float( istek.a + istek.b + istek.c )

        return yanit
    

def main():
    rclpy.init()

    n = MyNode()
    rclpy.spin(n)