n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
print('Введите элементы первого множества\n')
N = []
M = []
for i in range(n):
    N.append(int(input()))
print('Введите элементы второго множества\n')
for i in range(m):
    M.append(int(input()))

Otvet = []
for i in range(n):
    if N[i] in M:
        Otvet.append(N[i])
print(Otvet)

