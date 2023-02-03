S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))
for i in range(0, 1001):
    for j in range(0, 1001):
        if i+j == S and i*j == P:
            print(i, '  ', j)
            break
    if i + j == S and i * j == P:
        break
