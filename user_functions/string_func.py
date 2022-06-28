def reverse_str(string1):
    rev = ""
    for i in string1:
        rev = i + rev
    return rev


def substring_str(string1, string2):
    if string2 in string1:
        return True
    else:
        return False
