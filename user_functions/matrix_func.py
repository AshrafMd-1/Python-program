def matrix_entry(row, column, matrix_number):
    matrix_list = []
    for a in range(row):
        elements = []
        for b in range(column):
            item = int(input(f"enter the {a + 1}th row {b + 1}th column value of matrix {matrix_number} : "))
            elements.append(item)
        print()
        matrix_list.append(elements)
    return matrix_list


def matrix_multiply(matrix1, matrix2, row1):
    final_matrix_list = []
    for a in matrix1:
        row_sum = []
        for b in range(row1):
            index_val = 0
            sum1 = 0
            for c in matrix2:
                item_1 = a[index_val]
                item_2 = c[b]
                index_val += 1
                sum1 = (item_1 * item_2) + sum1
            row_sum.append(sum1)
        final_matrix_list.append(row_sum)
    return final_matrix_list


def matrix_add(matrix1, matrix2, row, column):
    final_matrix_list = []
    for a in range(row):
        sum1 = []
        for b in range(column):
            item_1 = matrix1[a][b]
            item_2 = matrix2[b][a]
            add_item = item_1 + item_2
            sum1.append(add_item)
        final_matrix_list.append(sum1)
    return final_matrix_list


def matrix_print(matrix, ending_character=" ", row_wise=True):
    for a in matrix:
        for b in a:
            print(b, end=ending_character)
        if row_wise:
            print()
