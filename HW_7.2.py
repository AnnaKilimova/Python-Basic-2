def correct_sentence(text):
    text_container = []

    for word in text.replace('.', ',').split(', '):

        if word[-1] == ',':
            text_container.append(word.replace(',', '.').capitalize())

        else:
            text_container.append(word.capitalize() + '.')
    return ' '.join(text_container)

# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')