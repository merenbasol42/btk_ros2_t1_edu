import rclpy
from rclpy.node import Node

from benim_arayuzler.msg import SensorVerisi, AcilDurum
from benim_arayuzler.srv import Esik


class MyNode(Node):
    def __init__(self):
        super().__init__("kontrolcu")

        self.sicaklik_esik = 30.0
        self.batarya_esik = 20.0

        self.create_service(Esik, "esik_ayarla", self.esik_ayarla_cb)
        self.create_subscription(SensorVerisi, "sensor", self.sensor_mesac_geldi, 10)
        self.acil_pubber = self.create_publisher(AcilDurum, "acil_durum", 10)

    def sensor_mesac_geldi(self, msg: SensorVerisi):
        acil_msg = AcilDurum()
        
        if msg.sicaklik > self.sicaklik_esik:
            acil_msg.acil_mi = True
            acil_msg.sebep = "sicaklik çok yüksek"
          
        elif msg.batarya < self.batarya_esik:
            acil_msg.acil_mi = True
            acil_msg.sebep = "batarya cok düşük"
        
        else:
            acil_msg.acil_mi = False
            acil_msg.sebep = "herşey düzgün"

        self.acil_pubber.publish(acil_msg)
        

    def esik_ayarla_cb(self, istek: Esik.Request, yanit: Esik.Response) -> Esik.Response:
        self.sicaklik_esik = istek.sicaklik_esik
        self.batarya_esik = istek.batarya_esik

        yanit.success = True

        return yanit




def main():
    rclpy.init()

    n = MyNode()

    rclpy.spin(n)