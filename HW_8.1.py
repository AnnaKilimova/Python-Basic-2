def add_one(some_list, sum = ''):

    for element in some_list:
        sum += str(element)

    for number in range(len(some_list)):
        if len(some_list) < len(str(int(sum) + 1)):
            some_list.append(0)

        some_list[number] = int((str(int(sum) + 1))[number])

    return some_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")