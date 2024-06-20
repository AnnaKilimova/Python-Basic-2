import keyword
import string

my_str = input('Enter the variable name: ')
str_pun = string.punctuation[0:26] + string.punctuation[27:]

condition_1 = condition_2 = 'True'

for symbol in my_str:
    if str_pun.find(symbol) != -1:
        condition_1 = 'False'
        break
    elif symbol.isalpha():
        if not symbol.islower():
            condition_1 = 'False'
            break

if (my_str[0].isdigit() or my_str in keyword.kwlist or \
        my_str.find('__') != -1 or my_str.find(' ') != -1):
     condition_2 = 'False'

if (condition_1 == 'True' and condition_2 == 'True'):
    print('True')
else:
    print('False')

