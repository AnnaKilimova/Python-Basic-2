a = int(input('Enter a 5-digit number: '))

print(f'{str(a % 10) + str(a // 10 % 10) + str(a // 100 % 10) + str(a // 1000 % 10) + str(a // 10000 % 10)}')
