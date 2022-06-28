def compute_lcm(number1, number2, gcd):
    lcm = (number1 * number2) // gcd
    return lcm


def compute_gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def group_square(start_value, end_value):
    square_lst = []
    for i in range(start_value, end_value + 1):
        i = i ** 2
        square_lst.append(i)
    return square_lst


def fibonacci_last(end_value):
    number1 = 1
    number2 = 1
    for i in range(end_value):
        sum1 = number1 + number2
        number1 = number2
        number2 = sum1
    return number2 - number1


def fibonacci_series(end_value):
    fibonacci_lst = []
    number1 = 1
    number2 = 1
    for i in range(end_value):
        sum1 = number1 + number2
        fibonacci_lst.append(number1)
        number1 = number2
        number2 = sum1
    return fibonacci_lst


def compute_factorial(number1):
    fact = 1
    for i in range(1, number1 + 1):
        fact = fact * i
    return fact


def check_even(number):
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False
    else:
        return "wrong input"


def check_odd(number):
    if number % 2 != 0:
        return True
    elif number % 2 == 0:
        return False
    else:
        return "wrong input"
