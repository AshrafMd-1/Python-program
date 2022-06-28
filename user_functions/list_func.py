def unique_lst(list1):
    unique_list1 = []
    for i in list1:
        if i not in unique_list1:
            unique_list1.append(i)
    return unique_list1


def list_print(list1, ending_character="\n"):
    for i in list1:
        print(i, end=ending_character)


def linear_search(list1, search_element):
    if search_element in list1:
        return True
    else:
        return False


def linear_search_index(list1, search_element):
    if search_element in list1:
        return list1.index(search_element)
    else:
        return False


def binary_search(list1, search_element):
    list1.sort()
    while len(list1):
        mid = len(list1) // 2
        if search_element > list1[mid]:
            list1 = list1[mid + 1:]
        elif search_element < list1[mid]:
            list1 = list1[0:mid]
        elif search_element == list1[mid]:
            return True
    else:
        return False


def bubble_search(list1, sort="ascending"):
    if sort == "ascending":
        for i in range(list1):
            for j in range(len(list1) - i - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        return list1
    elif sort == "descending":
        for i in range(list1):
            for j in range(len(list1) - i - 1):
                if list1[j] < list1[j + 1]:
                    list1[j + 1], list1[j] = list1[j], list1[j + 1]
        return list1
    else:
        return "wrong value entered"
