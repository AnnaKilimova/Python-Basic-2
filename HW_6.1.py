import string

my_str = input('Enter two letters hyphenated: ').split('-')
first_letter = string.ascii_letters.find(my_str[0])
last_letter = string.ascii_letters.find(my_str[-1])

print(string.ascii_letters[first_letter : last_letter + 1])

