def piramida(n):
    counter = 1
    previous = 0
    while True:
        previous += counter
        if previous + (counter + 1) > n:
            break
        counter += 1

    return previous, counter


def checker(input_variable, variable):
    if input_variable - variable > 0:
        return True
    else:
        return False


def loop(input_variable):
    first_variable = 0
    list_of_blocks = []
    while True:
        if checker(input_variable, first_variable):
            second_variable = first_variable
            first_variable, results = piramida(input_variable - first_variable)
            first_variable = first_variable + second_variable
            list_of_blocks.append(results)
        else:
            print(len(list_of_blocks))
            for i in list_of_blocks:
                print(i, end=" ")
            break


user_variable = int(input("Enter number: "))
loop(user_variable)
