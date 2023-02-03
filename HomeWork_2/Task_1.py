n = int(input('Введите количество монет: '))
A = str(input('Введите стороны всех монет в одну строку: '))
summ = 0
for i in range(n):
    if int(A[i]) == 1:
        summ += 1
summ2 = 0
if summ >= n/2:

    for i in range(n):
        if int(A[i]) == 0:
            summ2 += 1
else:
    for i in range(n):
        if int(A[i]) == 1:
            summ2 += 1
print(summ2)