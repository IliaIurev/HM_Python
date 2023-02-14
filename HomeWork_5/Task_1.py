def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

base = int(input('Введите число: '))
exp = int(input('Введите степень: '))
print(power(base, exp))
