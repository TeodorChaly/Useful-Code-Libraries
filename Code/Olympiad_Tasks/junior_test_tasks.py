# Tasks from https://pythonist.ru/python-voprosy-sobesedovaniya-chast-i-junior/

# Correct answers from quizz: All except 21, 22, 28

# Task is to create a list with all prime numbers from 0 to 100
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...]

def all_prime_numbers():
    prime_numbers = []
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


# Task is to create a list with unique elements
# [1, 2, 3, 3, 3, 3, 4, 5] -> [1, 2, 3, 4, 5]

def unique_list_converter(list_with_duplicates):
    new_list = []
    for i in list_with_duplicates:
        if i not in new_list:
            new_list.append(i)
    return new_list


# Task is to create a string from 0 to 100
# 123...100
def zero_to_hundred(string):
    for i in range(100):
        string += str(i)
    return string


# Task is to delete empty strings from list
# ["", "Hello", "", "world", ""] -> ["Hello", "world"]

def delete_empty_strings(string_list):
    new_list = []
    for string in string_list:
        if string != "":
            new_list.append(string)
    return new_list


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
    print("Task 1:")
    print(binary_converter("00001001"))
    print(binary_converter("11111111"))
    print("Task 2:")

    a = (1, 2, 3)
    b = (3, 2, 6)
    print(tuple_checker(a, b))
    print("Task 3:")

    print(string_to_ascii("Hello world!"))
    print("Task 4:")

    string_list = ["", "Hello", "", "world", ""]
    print(delete_empty_strings(string_list))
    print("Task 5:")

    string_from_zero_to_hundred = ""
    print(zero_to_hundred(string_from_zero_to_hundred))
    print("Task 6:")

    list_with_duplicates = [1, 2, 3, 3, 3, 3, 4, 5]
    print(unique_list_converter(list_with_duplicates))

    print(all_prime_numbers())


if __name__ == "__main__":
    main()
