import string
def first_word(text):
    punctuation = string.punctuation[0] + string.punctuation[2:6] + string.punctuation[7:] + ' '

    fist_word = ''

    for i in text.lstrip(string.punctuation).lstrip():
        if i in punctuation:
            break
        fist_word += i

    return fist_word

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')








