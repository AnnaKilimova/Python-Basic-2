from inspect import isgenerator
def prime_generator(end):
    for dividend in range(2, end + 1):
        result = 0
        for divider in range(1, dividend + 1):
            if dividend % divider == 0:
                result += 1
        if result == 2:
            yield dividend

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')