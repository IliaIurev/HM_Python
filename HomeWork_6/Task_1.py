A = []
A.append(int(input('Введите первый элемент массива: ')))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))
for i in range(2, n+1):
    A.append(A[0]+(i-1)*d)
print(A)