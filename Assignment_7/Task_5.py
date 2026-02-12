from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Processing credit card payment of", amount)


class UPIPayment(Payment):
    def process_payment(self, amount):
        print("Processing UPI payment of", amount)


cc = CreditCardPayment()
upi = UPIPayment()

cc.process_payment(5000)
upi.process_payment(3000)
