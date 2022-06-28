from class_objects.bank_class import SavingsAccount

while True:
    print()
    print("Enter your new account details: ")
    customer1 = SavingsAccount()
    print()
    print("Choose the option required: ")
    print("1. deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. pin change")
    print("5. interest")
    print("6. change account")
    option = int(input("Enter the option number: "))
    if option == 1:
        customer1.deposit()
    elif option == 2:
        customer1.withdraw()
    elif option == 3:
        customer1.checkbalance()
    elif option == 4:
        customer1.pinchange()
    elif option == 5:
        customer1.interest()
    elif option == 6:
        customer1 = SavingsAccount()
    else:
        print("Invalid option")
