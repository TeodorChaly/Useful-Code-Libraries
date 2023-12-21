import random
import time

from matplotlib import pyplot as plt


def decorator(function):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        return_value = function(*args, **kwargs)
        time_end = time.time()
        print(time_start - time_end, "seconds")
        return return_value

    return wrapper


@decorator
def bool_massive(massive, element):
    if element in massive:
        return True
    else:
        return False


@decorator
def count_element_in_massive(massive, element):
    if massive.count(element) > 0:
        return True
    else:
        return False


@decorator
def count_element_in_index(massive, element):
    try:
        if massive.index(element):
            return True
    except:
        return False


@decorator
def massive_splitter(massive, element):
    counter = None

    while True:
        if len(massive) == 0:
            break
        elif len(massive) % 2 == 0:
            if massive[len(massive) // 2:][0] <= element:
                if massive[len(massive) // 2:][0] == element:
                    counter = massive[len(massive) // 2:][0]
                    break
                else:
                    massive = massive[len(massive) // 2:]
            else:
                massive = massive[:len(massive) // 2]
        else:
            if massive[len(massive) // 2] == element:
                counter = massive[len(massive) // 2]
                break
            elif massive[len(massive) // 2] < element:
                massive = massive[len(massive) // 2 + 1:]
            else:
                massive = massive[:len(massive) // 2]

    if counter is None:
        return False
    else:
        return True


massive_small = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
element_small = 7

random_list = [random.randint(-10000, 100000) for _ in range(1000000)]
big_list = sorted(random_list)
k_big = 6446

print(bool_massive(big_list, k_big))  # "Bool type function:"
print(count_element_in_massive(big_list, k_big))  # "Counter type function:"
print(count_element_in_index(big_list, k_big))  # "Index type function:"
print(massive_splitter(big_list, k_big))  # "Splitter type function:"
