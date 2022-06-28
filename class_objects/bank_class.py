class BankAccount:
    chkpin = None
    dep = None
    wtd = None
    newpin = None

    def __init__(self):
        self.name = input("Enter your name: ")
        while True:
            self.pin = int(input("Enter a 4 digit account pin: "))
            if len(str(self.pin)) == 4:
                break
            else:
                print("Enter a 4 digit pin")
        self.balance = int(input("Enter your balance: "))

    def checkpin(self):
        self.chkpin = int(input("Enter your current pin: "))
        if self.chkpin == self.pin:
            return True
        else:
            return False

    def deposit(self):
        while True:
            if BankAccount.checkpin(self):
                self.dep = int(input("Enter the money you want to deposit: "))
                if self.dep > -1:
                    self.balance = self.balance + self.dep
                    print("The current balance is: ", self.balance)
                    break
                else:
                    print("Enter a valid amount to deposit.")
            else:
                print("Wrong pin")

    def withdraw(self):
        while True:

            if BankAccount.checkpin(self):
                self.wtd = int(input("Enter the money you want to withdraw: "))
                if self.balance >= self.wtd > -1:
                    self.balance = self.balance - self.wtd
                    print("The current balance is: ", self.balance)

                else:
                    print("deposit more money before withdrawing")
                break
            else:
                print("Wrong pin")

    def checkbalance(self):
        while True:
            if BankAccount.checkpin(self):
                print("Hello", self.name)
                print("Your current balance is: ", self.balance)
                break
            else:
                print("Wrong pin")

    def pinchange(self):
        while True:
            if BankAccount.checkpin(self):
                while True:
                    self.newpin = int(input("Enter the new 4 digit pin: "))
                    if len(str(self.newpin)) == 4:
                        self.pin = self.newpin
                        print("The pin has been changed")
                        break
                    else:
                        print("Enter a valid 4 digit pin")
                break
            else:
                print("Wrong pin")


class SavingsAccount(BankAccount):
    rate = None

    def __init__(self):
        BankAccount.__init__(self)

    def interest(self):
        while True:
            if BankAccount.checkpin(self):
                self.rate = int(input("Enter the current interest rate: "))
                self.balance = self.balance + (self.balance * (self.rate / 100))
                print("The interest is: ", self.balance * (self.rate / 100))
                print("The current bank balance is: ", self.balance)
                break
            else:
                print("Wrong pin")


def menus():
    print("Choose the option required: ")
    print("1. deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. pin change")
    print("5. new account")
    option = int(input("Enter the option number: "))
    return option