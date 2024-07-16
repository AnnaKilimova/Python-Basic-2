def is_even(number):
    scope = (_ for _ in range(2, 10, 2))

    for element in scope:
        if element == int(str(number)[-1]):
            return True
    return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('ok')