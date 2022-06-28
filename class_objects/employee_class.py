class Employee:
    def __init__(self):
        self.name = input("Enter the employee name: ")
        self.id = input("Enter the employee id: ")
        self.age = int(input("Enter the employee age: "))
        self.salary = int(input("Enter the employee salary: "))

    def info(self):
        print("The employee information is: ")
        print("name: ", self.name)
        print("id: ", self.id)
        print("age: ", self.age)
        print("salary: ", self.salary)
