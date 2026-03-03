from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class Telnpay(PaymentGateway):
    def pay(self):
        print("Paying using Tell&Pay.....")

class Razorpay(PaymentGateway):
    def pay(self):
        print("Paying using Razorpay...")

class Purchase:

    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checking out....")
        self.gateway.pay()

gateway1 = Razorpay()
gateway2 = Telnpay()
p1 = Purchase(gateway1)

p1.checkout()