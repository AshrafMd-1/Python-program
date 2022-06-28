def count_up_low(string1):
    dict1 = {"upper": 0, "lower": 0}
    for i in string1:
        if i.isupper():
            dict1["upper"] += 1
        if i.islower():
            dict1["lower"] += 1
    return dict1["upper"], dict1["lower"]


def count_letter(string1):
    dict1 = {}
    for i in string1:
        dict1[i] = string1.count(i)
    return dict1


def add_dict(dictionary1, dictionary2):
    for keys, value in dictionary2.items():
        dictionary1[keys] = value
    return dictionary1
