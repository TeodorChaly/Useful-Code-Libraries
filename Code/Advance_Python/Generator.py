import sys


def generator(n):
    result = 1
    for x in range(n):
        result = x + result
        yield result  # Wait for next yeild


values = generator(8)

for i in values:
    print(i)

massive_one = ["one", "two"]
massive_second = ["one", "two", "three", "four", "five"]
variable = "I want to code"

print("value (yield) size: ", sys.getsizeof(values))  # Memory economy
print("massive_one (array) size: ", sys.getsizeof(massive_one))  # No memory economy
print("massive_second (array) size: ", sys.getsizeof(massive_second))  # No memory economy
print("variable (variable) size: ", sys.getsizeof(variable))  # No memory economy
