def seven_seg_display(number, symbols="#"):
    con_str = str(number)
    pattern = {
        1: "#  ",
        2: "## ",
        3: "###",
        4: "  #",
        5: " ##",
        6: "# #"
    }
    row_form = {
        "1": [4, 4, 4, 4, 4],
        "2": [3, 4, 3, 1, 3],
        "3": [3, 4, 3, 4, 3],
        "4": [6, 6, 3, 4, 4],
        "5": [3, 1, 3, 4, 3],
        "6": [3, 1, 3, 6, 3],
        "7": [3, 4, 4, 4, 4],
        "8": [3, 6, 3, 6, 3],
        "9": [3, 6, 3, 4, 3],
        "0": [3, 6, 6, 6, 3]
    }
    for i in range(5):
        for j in con_str:
            lst = row_form[j]
            print(pattern[lst[i]].replace("#", symbols), end=" ")
        print("\r")


def cipher_caesar(string, shift_no=1):
    if 1 <= shift_no <= 25:
        cipher = ''
        for char in string:
            if not char.isalpha():
                cipher += char
                continue
            cap = char.upper()
            code = ord(cap) + int(shift_no)
            if code > ord('Z'):
                code = (code - ord("Z")) + ord('A')
            text = chr(code)
            if char.islower():
                text = text.lower()
            cipher += text
        return cipher
    else:
        return "wrong shift value entered"


def decipher_caesar(string, shift_no=1):
    if 1 <= shift_no <= 25:
        decipher = ''
        for char in string:
            if not char.isalpha():
                decipher += char
                continue
            cap = char.upper()
            code = ord(cap) - int(shift_no)
            if code < ord('A'):
                code = (code - ord("Z")) + ord('A')
            text = chr(code)
            if char.islower():
                text = text.lower()
            decipher += text
        return decipher
    else:
        return "wrong shift value entered"
