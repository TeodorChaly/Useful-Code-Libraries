# Task from https://pythonist.ru/python-voprosy-sobesedovaniya-chast-ii-middle/

# Correct answers from quizz: 2, 3, 6, 11, 13, 14, 15, 16

import time


def repeater_decorator(function):
    def wrapper(*args, **kwargs):
        try:
            return_value = function(*args, **kwargs)
            print("Everything is ok")
            return return_value
        except:
            print("Error")

    return wrapper


def time_decorator(function):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        return_value = function(*args, **kwargs)
        end = time.time()
        print(f"Time of execution: {end - start}")
        return return_value

    return wrapper


@repeater_decorator
def hello_person(name, surname):
    time.sleep(1)
    return f"Hello, {name} and {surname}!"


print(hello_person("Mike", "Schmidt"))


# Also tasks from https://pythonist.ru/python-voprosy-sobesedovaniya-chast-iii-senior/

# Correct answers from quizz: 1

