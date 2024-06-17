my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
# my_list = []

my_sum = 0

for element in range(0, len(my_list), 2):

    my_sum += my_list[element]

if len(my_list) > 0:
    my_sum *= my_list[len(my_list) - 1]

print(my_sum)

