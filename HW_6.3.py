number_int = int(input('Enter the integer number: '))
my_list = []

while True:
  result = 1
  for _ in range(len(str(number_int))):
    my_list.append(number_int % 10)
    number_int = number_int // 10
  my_list.reverse()

  for element in range(len(my_list)):
    result *= my_list[element]

  my_list.clear()
  number_int = result

  if result < 10:
    break

print(result)