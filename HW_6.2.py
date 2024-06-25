my_number = int(input('Enter a number from 0 and to 8640000: '))
divider_list = (86400, 3600, 60)
my_list = []
day_dict = {}

if my_number <= 0 or my_number >= 8640000:
    print('You entered the wrong number. Try again')

elif my_number >= 0 and my_number < 8640000:

    for divider in range(3):
        result = divmod(my_number, divider_list[divider])
        my_number = result[1]
        my_list.append(str(result[0]).zfill(2))

    my_list.append(str(my_number).zfill(2))

    conditions_1 = ('11', '12', '13', '14')
    conditions_2 = ('0', '5', '6', '7', '8', '9')
    conditions_3 = ('2', '3', '4')

    if my_list[0] in conditions_1 or my_list[0][1] in conditions_2:
        day_dict[my_list[0]] = 'днів'
    elif my_list[0][1] in conditions_3:
        day_dict[my_list[0]] = 'дні'
    elif my_list[0][1] == '1':
        day_dict[my_list[0]] = 'день'

    for key, value in day_dict.items():
       print(f'{int(key)} {value}, {my_list[1]}:{my_list[2]}:{my_list[3]}')










