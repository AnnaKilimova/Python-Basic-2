import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file1:
        html = file1.read()

    list1 = [element for element in range(len(html)) if html[element].find('<') != -1]
    list2 = [element for element in range(len(html)) if html[element].find('>') != -1]

    txt = ''
    for element in range(len(list1) - 1):
        txt += html[list2[element] + 1: list1[element + 1]]

    with codecs.open(result_file, 'w', 'utf-8') as file2:
        file2.write(txt)

    with codecs.open(result_file, 'r', 'utf-8') as file3:
        new_txt = ''

        for str in file3:
            if str.isspace():
                continue
            new_txt += str.strip() +'\n'
        print(new_txt)

    with codecs.open(result_file, 'w', 'utf-8') as file4:
        file4.write(new_txt)
        return result_file

delete_html_tags('draft.html', 'cleaned.txt')