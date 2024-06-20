user_text = input('Enter text: ')

new_hashtag = '#'

for symbol in user_text.title():
    if len(new_hashtag) <= 140 and symbol.isalnum():
        new_hashtag += symbol

print(new_hashtag)
