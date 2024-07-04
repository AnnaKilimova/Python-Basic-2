def popular_words (text, words):

    words_info = {}

    for search_word in words:
        for word in text.lower().split():
            if word == search_word and search_word in words_info:
                words_info[search_word] += 1
            elif word == search_word and search_word not in words_info:
                    words_info[search_word] = 1
            elif word != search_word and search_word not in words_info:
                words_info[search_word] = 0

    return words_info

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

