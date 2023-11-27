# Python is dynamically typed language.
# It means that we can assign any type of data to any variable.

def myfunction(unknown_type: int) -> str:
    return str(unknown_type)


print(myfunction(5))

# You can check if entered data is correct only if you use mypy type_hinting.py in cmd.
