# K - natural number

def double_check(list_of_num, iteration=0):
    try:
        list_of_num = sorted(list_of_num, reverse=True)
        new_array = []
        max_val = -1

        for i in range(len(list_of_num)):
            if int(list_of_num[i][iteration]) >= max_val:
                max_val = int(list_of_num[i][iteration])
                new_array.append(list_of_num[i])

        if len(new_array) == 1:
            variable = new_array[0]
            return variable

        iteration += 1
        return double_check(new_array, iteration)

    except Exception as e:
        print(str(list_of_num[0][:list_of_num[0].find(list_of_num[1])])+ str(list_of_num[1])+str(list_of_num[0][list_of_num[0].find(list_of_num[1]):]))
        return list_of_num


color_list = ['592', '265', '3545']
iteration = 0
for i in color_list:
    iteration += len(str(i))

full_num = ""
for i in range(iteration - 1):
    max_num = -1
    id_max = -1
    check = []
    for i2 in color_list:
        first_char = int(str(i2)[0])
        check.append(str(i2)[0])

        # print(first_char, end=" ")

        if first_char > max_num:
            max_num = first_char
            id_max = i2
    # print(f"Max {max_num}")
    if check.count(str(max_num)) > 1:
        delete = double_check(color_list)
        # print(delete, len(delete))
        id_max = color_list[color_list.index(delete)]
        color_list[color_list.index(id_max)] = str(id_max)[len(delete):]

        if color_list[color_list.index(str(id_max)[len(delete):])] == "":
            color_list.remove(str(id_max)[len(delete):])

        full_num += str(delete)
        # print(color_list, 123)
    else:
        color_list[color_list.index(id_max)] = str(id_max)[1:]

        if color_list[color_list.index(str(id_max)[1:])] == "":
            color_list.remove(str(id_max)[1:])

        full_num += str(max_num)
        # print(color_list)

print(color_list, full_num)
