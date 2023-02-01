chislo = str(input("Введите число: "))
len_chisla = int(len(chislo))
summ = 0
for i in range(len_chisla):
    summ += int(chislo[i])
print("Сумма цифр числа: ", summ)