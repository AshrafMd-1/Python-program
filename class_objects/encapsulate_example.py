class Employee:
    name = None
    _location = None
    __id = None

    def __init__(self):
        self.name = input("Enter the employee name: ")
        self._location = input("Enter the employee location: ")
        self.__id = input("Enter the employee id: ")

    def emp_info(self):
        print("The employee information is: ")
        print("name: ", self.name)
        print("location: ", self._location)
        print("id: ", self.__id)


class SalesRep(Employee):
    def __init__(self):
        Employee.__init__(self)

    def sales_info(self):
        print("The sales rep information is: ")
        print("name: ", self.name)
        print("location: ", self._location)
