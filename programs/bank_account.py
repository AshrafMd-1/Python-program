from class_objects.bank_class import BankAccount, menus

print("Enter your new account details:- ")
customer1 = BankAccount()
while True:
    print()
    option = menus()
    if option == 1:
        customer1.deposit()
    elif option == 2:
        customer1.withdraw()
    elif option == 3:
        customer1.checkbalance()
    elif option == 4:
        customer1.pinchange()
    elif option == 5:
        print()
        print("Enter your new account details:- ")
        customer1 = BankAccount()
    else:
        print("Invalid option")
