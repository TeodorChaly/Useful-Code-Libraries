# Task: Sorted massive of numbers. Find two numbers, which sum is equal to given number.
# Examples: massive = [-1, 2, 5, 8] K = 7 -> 2, 5
import random

import numpy as np
import time


def decorator(function):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        return_value = function(*args, **kwargs)
        time_end = time.time()
        print(time_start - time_end, "seconds")
        return return_value

    return wrapper


@decorator
def function_two_way_compression(massive_local, k_local):
    result_list_local = []
    new_massive = massive_local.copy()
    for element_id in range(len(massive_local)):
        new_massive.pop(0)
        for sub_element_id in range(len(new_massive)):
            if massive_local[element_id] + new_massive[sub_element_id] == k_local:
                result_list_local.append(str(massive_local[element_id]) + " " + str(new_massive[sub_element_id]))
            if massive_local[element_id] + new_massive[sub_element_id] > k_local:
                break
    return result_list_local


@decorator
def function_element_finder(massive_local, k_local):
    result_list_local = []
    for element in massive_local:
        if k_local - element in massive_local and element <= 0:
            result_list_local.append(str(element) + " " + str(k_local - element))

    return result_list_local


random_list = [random.randint(-10000, 100000) for _ in range(10000)]
big_list = sorted(random_list)
k_big = 6446

massive = [-1, 2, 5, 8]
k_small = 7

result_list_one = function_two_way_compression(big_list, k_big)
result_list_two = function_element_finder(big_list, k_big)

# for i in result_list_one:
#     print(i)
#
# for i2 in result_list_two:
#     print(i2)
