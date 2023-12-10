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
    print(binary_converter("00001001"))
    print(binary_converter("11111111"))


if __name__ == "__main__":
    main()
