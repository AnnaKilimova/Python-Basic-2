def second_index(text, some_str):

    index = 0
    sum = 0

    for _ in text:
        if text.find(some_str) != -1:
            index += text.find(some_str)
            text = text[text.find(some_str) + 1 :]
            sum += 1

            if sum == 2:
                return index + 1

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

