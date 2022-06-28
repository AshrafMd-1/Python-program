from user_functions.string_func import *

string1 = input("enter the string: ")
string2 = reverse_str(string1)

if string1 == string2:
    print("yes, its a palindrome")
else:
    print("no, it's not a palindrome")
