import random
import math

print('Задайте число элементов списка')
n = int(input())
print('Задайте границы рандома')
a = int(input())
b = int(input())
l = []

for i in range(n):
    l.append(random.randint(a, b))

print(l)

id_1 = 0
id_2 = 0

for i in range(len(l)):
    if l[i] < 0:
        id_1 = i
        break

for i in range(0, len(l)):
    if l[i] < 0:
        id_2 = i

print('Ответ 1:', sum(l[id_1+1:id_2]))

l_otv = []

for i in l:
    if math.fabs(i) < 4:
        l_otv.append(i)

for n in range(len(l)-len(l_otv)):
    l_otv.append(0)

print('Ответ 2:', l_otv)