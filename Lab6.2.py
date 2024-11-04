print('Введите строку')

stroka = input()
id_1 = stroka.find('(')
id_2 = stroka.rfind(')')
res_stroka = ''
st = ''
for i in range(id_1+1, id_2):
    if stroka[i] == '(' or stroka[i] == ')':
        st += stroka[i]

new_st = stroka[:id_1+1] + st + stroka[id_2:]

print('Результат')
print(new_st)