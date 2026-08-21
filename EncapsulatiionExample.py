class BankAccount:

    def __init__(self, account_holder, opening_balance):
        self.account_holder = account_holder  # Public
        self.__balance = opening_balance       # Private encapsulation as balance is hidden by declaring as private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"£{amount} deposited")
        else:
            print("Deposit must be greater than zero")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"£{amount} withdrawn")

    def get_balance(self):
        return self.__balance
        
account=BankAccount("Rajeeve",1000) 
       
deposit_amount=float(input("Enter amount to deposit "))
account.deposit(deposit_amount)
print(f"Current balance: £{account.get_balance():.2f}")
       