import time

class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.lock = False

    def get_balance(self) -> int:
        if self.lock is False:
            raise ValueError("Cannot retrieve balance, account was already closed.")
        return self.balance

    def open(self):
        while self.lock:
            time.sleep(.5)
        self.lock = True    

    def deposit(self, amount: int):
        if self.lock is False:
            raise ValueError("Cannot deposist, account was already closed.")
        elif amount < 0:
            raise ValueError("Cannot deposist a negative amount.")
        self.balance = self.balance + amount

    def withdraw(self, amount: int):
        if self.lock is False:
            raise ValueError("Cannot withdraw, account was already closed.")
        elif amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        elif amount <= self.balance:
            self.balance = self.balance - amount
        else:
            raise ValueError("Cannot withdraw more than account balance.")

    def close(self):
        self.lock = False
