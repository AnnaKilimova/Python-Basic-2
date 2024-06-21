while True:
    number_1 = int(input('Enter a number one: '))
    action = input('Add an action: ')
    number_2 = int(input('Enter a number two: '))

    result = None

    if action == '+':
        result = number_1 + number_2

    elif action == '-':
        result = number_1 - number_2

    elif action == '*':
        result = number_1 * number_2

    elif action == '/' and number_2 != 0:
        result = number_1 / number_2

    else:
        print('Use valid data =>', end=' ')

    print(result)

    Question_Answer = input('Do you want to keep going??? Enter \'Yes\' / \'No\': ').lower()
    if Question_Answer == 'yes':
        continue
    else:
        break









