class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name  # public attribute -> can be accessed inside and outside of a class
        # protected -> can be accessed inside of a class and subclasses
        self._account_number = account_number
        self.__balance = balance  # private -> can only accessed inside the class

    # getter function -> help to access private data outside of a class
    def get_balance(self):
        print(f"{self.name} has {self.__balance} dollars in his account")

    # setter function -> update value of a private attribute
    def set_new_balance(self, new_balance):
        self.__balance = new_balance


account1 = BankAccount("shazzad_hosen", "a157918350104828", "999M")

# we can access a protected attribute outside of a class, but we should not do that
print(f"account number of {account1.name} is {account1._account_number} ")

# accessing private attribute thrugh a getter function
account1.get_balance()


account1.set_new_balance("1298M")
account1.get_balance()
