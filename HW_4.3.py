my_list = [1, 2, 3, 4, 5, 6, 7, 9]
# my_list = [1, 1, 2, 1]
# my_list = [6, 3, 7]

my_new_list = []

for element in range(0, len(my_list), 2):
    if element < 3:
        my_new_list.append(my_list[element])

my_new_list.append(my_list[len(my_list) - 2])

print(my_new_list)