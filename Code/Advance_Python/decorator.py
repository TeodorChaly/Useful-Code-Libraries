def decorator(function):
    def wrapper(*args, **kwargs):  # Wrap function
        print("Decorating function start.")  # executing moment
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper


@decorator  # Calling decorator
def hello_person(name, surname):
    return f"Hello, {name} and {surname}!"


print(hello_person("Mike", "Schmidt"))
