def common_elements():
    my_range = range(0, 100)
    my_list1 = []
    my_list2 = []

    for element in my_range:
        if element % 3 == 0:
            my_list1.append(element)

        if element % 5 == 0:
            my_list2.append(element)

    return set(list(my_list1)) & set(list(my_list2))

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


# Option 2 without list creation

# def common_elements():
#     my_range = range(0, 100)
#     my_set1 = set()
#     my_set2 = set()
#
#     for element in my_range:
#         if element % 3 == 0:
#             my_set1.add(element)
#
#         if element % 5 == 0:
#             my_set2.add(element)
#
#     return my_set1 & my_set2
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}





