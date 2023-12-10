# Tasks from https://pythonist.ru/python-voprosy-sobesedovaniya-chast-i-junior/

# Task is to convert string to ASCII
# "Hello world!" -> [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]

def string_to_ascii(string):
    string_list = []
    for char in string:
        string_list.append(ord(char))
    return string_list


# Task is to check if two tuples have same elements
# (1, 2, 3) and (3, 2, 6) -> (2, 3)

def tuple_checker(a_tuple, b_tuple):
    same_element = []
    for i in a_tuple:
        if i in b_tuple:
            same_element.append(i)
    return same_element


# Task is to convert from binary string to real number
# 00000000 -> 0
# 00000001 -> 1
# 00000010 -> 2
# 00000011 -> 3

# 255 -> 11111111
# 256 -> 100000000
def binary_converter(binary_string):
    binary_string = binary_string[::-1]
    counter = 1
    number = 0
    for i in binary_string:
        if i == "1":
            number += counter
        counter += counter
    return number


def main():
    pass

    # print(binary_converter("00001001"))
    # print(binary_converter("11111111"))

    # a = (1, 2, 3)
    # b = (3, 2, 6)
    # print(tuple_checker(a, b))

    # print(string_to_ascii("Hello world!"))
if __name__ == "__main__":
    main()
