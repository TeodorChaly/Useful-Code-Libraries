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


@decorator
def function_zero_point(massive_local, k_local):
    plus_list = []
    minus_list = []
    result_list_local = []

    for element in massive_local:
        if element == 0:
            if k_local - element in massive_local:
                result_list_local.append(str(element) + " " + str(k_local - element))
        elif element > 0:
            plus_list.append(element)
        elif element < 0:
            minus_list.append(element)

    for positive in plus_list:
        for negative in minus_list[::-1]:
            if positive + negative < k_local:
                break
            elif positive + negative == k_local:
                result_list_local.append(str(positive) + " " + str(negative))

    if k_local > 0:
        for positive in plus_list:
            if k_local - positive in plus_list:
                result_list_local.append(str(positive) + " " + str(k_local - positive))
    elif k_local < 0:
        for negative in minus_list:
            if k_local - negative in minus_list:
                result_list_local.append(str(negative) + " " + str(k_local - negative))

    return result_list_local


random_list = [random.randint(-10000, 100000) for _ in range(10000)]
big_list = sorted(random_list)
k_big = 6446

massive = [-4, -2, 0, 1, 3, 4, 8, 9]
k_small = -4

result_list_one = function_two_way_compression(big_list, k_big)  # Count each once (Best)
result_list_two = function_element_finder(big_list, k_big)  # Count only once
result_list_three = function_zero_point(big_list, k_big)  # Count each once

print("________________________")
for i in result_list_one:
    print(i)
print("________________________")
for i2 in result_list_two:
    print(i2)
print("________________________")
for i3 in result_list_three:
    print(i3)
