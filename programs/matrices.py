from user_functions.matrix_func import *

while True:

    row_1 = int(input("how many rows of first matrix: "))
    column_1 = int(input("how many column of first matrix: "))

    print()

    row_2 = int(input("how many rows of second matrix: "))
    column_2 = int(input("how many column of second matrix: "))

    print()

    mat1 = matrix_entry(row_1, column_1, 1)

    print()

    mat2 = matrix_entry(row_2, column_2, 2)

    print()

    print("matrix A is:")
    matrix_print(mat1)
    print()

    print("matrix B is:")
    matrix_print(mat2)
    print()

    while True:

        print()
        task1 = input("enter addition or multiplication : ")
        print()

        if task1 == "addition":

            print("result of addition of matrices are: ")
            mat_add = matrix_add(mat1, mat2, row_1, column_1)
            matrix_print(mat_add)
            break

        elif task1 == "multiplication":

            print("result of multiplication of matrices are: ")
            mat_product = matrix_multiply(mat1, mat2, row_1)
            matrix_print(mat_product)
            break

        else:

            print()
            print("error")
            print("enter a valid task")

    print()
    end_task = input("type end to exit : ")
    print()

    if end_task == "end":
        break
