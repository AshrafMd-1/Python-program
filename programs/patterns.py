from user_functions.pattern_func import *

task = input("do you want to cipher or decipher: ")
if task == "cipher":
    string = input("enter the text you want to cipher: ")
    shift = int(input("enter the shift number: "))
    print(f"{cipher_caesar(string, shift)}")
else:
    string = input("enter the text you want to decipher: ")
    shift = int(input("enter the shift number: "))
    print(f"{decipher_caesar(string, shift)}")