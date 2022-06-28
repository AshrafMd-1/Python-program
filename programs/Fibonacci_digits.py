from user_functions.math_func import *
from user_functions.list_func import *

end_no = int(input("enter the number of digits u want: "))
generation = input("enter if you want series or last digit: ")
print()
if generation == "series":
    fib_lst = fibonacci_series(end_no)
    print("the fibonacci series is: ")
    list_print(fib_lst, " ")
else:
    fib_num = fibonacci_last(end_no)
    print(f"the fibonacci series last digit is {fib_num}")
