class Account:
    def __init__(self):
        self._balance = 0

    # instance variable that is somehow protected: cannot be modified from outside the class
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(500)
    print("Balance: ", account.balance)

# self._balance is available to all methods and can be modified through the methods


#
# # This is a global variable and cannot be modified in the main function unless designated to do so using global
# balance = 0
#
#
# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
#
# # Note that even if you input balance, it assumes it is local and cannot change the value of the global variable
# def deposit(n):
#     global balance
#     balance += n
#
# def withdraw(n):
#     global balance
#     balance -= n
#
if __name__ == '__main__':
    main()