import copy

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def perms(lon):
    all_perms = []
    for digit in digits:
        digits.remove(digit)
        app_perms.append(concat_all(digit, digits))


def concat_all(char, char_list):
    perms = []
    for el in char_list:
        perms.append(char+el)

    temp_list = copy.copy(char_list)
    for el in char_list:
        temp_list.remove(el)
        perms.extend(concat_all(char+el, temp_list))

    return perms


print concat_all("0", ["1", "2"])
