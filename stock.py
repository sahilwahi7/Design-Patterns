from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

# Interface for payment methods
class PaymentMethod(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# Concrete implementations of payment methods
class CheckPayment(PaymentMethod):
    def deposit(self, amount):
        print(f"Depositing ${amount} via check")

    def withdraw(self, amount):
        print(f"Withdrawing ${amount} via check")

class WirePayment(PaymentMethod):
    def deposit(self, amount):
        print(f"Depositing ${amount} via wire transfer")

    def withdraw(self, amount):
        print(f"Withdrawing ${amount} via wire transfer")

class ElectronicTransferPayment(PaymentMethod):
    def deposit(self, amount):
        print(f"Depositing ${amount} via electronic transfer")

    def withdraw(self, amount):
        print(f"Withdrawing ${amount} via electronic transfer")

# Interface for trade orders
class TradeOrder(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete implementations of trade orders
class MarketOrder(TradeOrder):
    def execute(self):
        print("Executing market order")

class LimitOrder(TradeOrder):
    def execute(self):
        print("Executing limit order")

class StopLossOrder(TradeOrder):
    def execute(self):
        print("Executing stop loss order")

class StopLimitOrder(TradeOrder):
    def execute(self):
        print("Executing stop limit order")

# Factory for creating trade orders
class TradeOrderFactory:
    @staticmethod
    def create_order(order_type):
        if order_type == OrderType.MARKET:
            return MarketOrder()
        elif order_type == OrderType.LIMIT:
            return LimitOrder()
        elif order_type == OrderType.STOP_LOSS:
            return StopLossOrder()
        elif order_type == OrderType.STOP_LIMIT:
            return StopLimitOrder()
        else:
            raise ValueError("Invalid order type")

# Enum for trade order types
class OrderType(Enum):
    MARKET = 1
    LIMIT = 2
    STOP_LOSS = 3
    STOP_LIMIT = 4

# Observer interface for trade order notifications
class TradeOrderObserver(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# Concrete implementation of trade order observer
class UserNotification(TradeOrderObserver):
    def __init__(self, user):
        self.user = user

    def notify(self, message):
        print(f"Notification for {self.user.username}: {message}")

# User class
class User:
    def __init__(self, username, payment_method):
        self.username = username
        self.payment_method = payment_method
        self.notifications = []

    def deposit_funds(self, amount):
        self.payment_method.deposit(amount)

    def withdraw_funds(self, amount):
        self.payment_method.withdraw(amount)

    def place_order(self, order_type):
        order = TradeOrderFactory.create_order(order_type)
        order.execute()
        self.notify_observers(f"Order executed: {order_type.name}")

    def attach_observer(self, observer):
        self.notifications.append(observer)

    def detach_observer(self, observer):
        self.notifications.remove(observer)

    def notify_observers(self, message):
        for observer in self.notifications:
            observer.notify(message)

# Main function for testing
def main():
    # Create users with different payment methods
    user1 = User("Alice", CheckPayment())
    user2 = User("Bob", WirePayment())
    user3 = User("Charlie", ElectronicTransferPayment())

    # Attach observers (notifications)
    user1.attach_observer(UserNotification(user1))
    user2.attach_observer(UserNotification(user2))
    user3.attach_observer(UserNotification(user3))

    # Deposit funds for users
    user1.deposit_funds(1000)
    user2.deposit_funds(1500)
    user3.deposit_funds(2000)

    # Withdraw funds for users
    user1.withdraw_funds(500)
    user2.withdraw_funds(1000)
    user3.withdraw_funds(1500)

    # Place trade orders for users
    user1.place_order(OrderType.MARKET)
    user2.place_order(OrderType.LIMIT)
    user3.place_order(OrderType.STOP_LOSS)

if __name__ == "__main__":
    main()
