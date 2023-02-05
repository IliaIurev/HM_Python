import random

n = int(input('Введите длинну списка: '))
X = int(input('Введите число Х: '))

my_list = []

for i in range(n):
    my_list.append(random.randint(0, 100))
print(my_list)

summ = 0

for i in range(n):
    if my_list[i] == X:
        summ += 1
print(summ)