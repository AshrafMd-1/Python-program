from class_objects.encapsulate_example import *

a1 = SalesRep()
print()
print("SalesRep class is a derived class from Employee class which is a base class.")
print("-The location attributes is protected so is available in the SalesRep class.")
print("-The id attributes is private so is not available in the SalesRep class.")
print("-The name attribute is public so can be called even outside the class.")
print()
a1.sales_info()
print()
a1.emp_info()
print()
print("The name attribute value: ", a1.name)
