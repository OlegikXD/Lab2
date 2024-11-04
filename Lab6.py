# Задание1
print('Введите текст через пробел без символов')

symbols = [',', '.', '!', '?', ':', ';']
text = input()
i = 0
flag = False
while flag == False:
    for i in symbols:
        if i in text:
            flag = False
            break
        flag = True
    if flag == False:
        print('Не выполнены условия')
        text = str(input())
text = text.split(' ')

listik = dict()

for num_word in range(len(text)):
    if text[num_word] not in listik.keys():
        listik[text[num_word]] = 1
    else:
        listik[text[num_word]] += 1

data = [['Слово', 'Количество'], listik]

def tabliza(data):

    elem_col1 = [data[0][0]] + list(data[1].keys())

    elem_col2 = [data[0][1]] + list(map(str, list(data[1].values())))

    col_width = [len(max(elem_col1, key=len)),
                 len(max(elem_col2, key=len))]
    print(data[0][0],'|', data[0][1])
    for i in data[1].keys():
        separator = '-+-'.join('-'*n for n in col_width)
        print(separator)
        result = [i.ljust(col_width[0]),
                  str(data[1][i]).rjust(col_width[1], ' ')]

        print(result[0],'|', result[1])

tabliza(data)