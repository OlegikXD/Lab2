def factorial(N):
    counter = 1
    for n in range(1, N+1):
        counter = counter * n
    return counter

def operation(X, N):
    otvet = 1
    for n in range(N + 1):
        otvet += (X ** n) / factorial(n)
    print(otvet)

print('Введите вещественное число X')
X = float(input())

print('Введите целое число N > 0')
N = int(input())

if N <= 0:
    while N <= 0:
        print('Вы ввели неправильное число')
        N = int(input())
        operation(X, N)
else:
    operation(X, N)

print('мой гитхаб https://github.com/OlegikXD/Lab2')