from user_functions.list_func import *

print("enter the elements of the list: ")
dup_lst = [i for i in input().split()]
unique_lst = unique_lst(dup_lst)
print("the unique list is:- ")
print(unique_lst)
