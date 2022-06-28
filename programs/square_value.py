from user_functions.list_func import *
from user_functions.math_func import *

start1 = int(input("enter the starting number: "))
end1 = int(input("enter the ending number: "))

lst_num = group_square(start1, end1)

print("the squares of numbers are:- ")
list_print(lst_num)
