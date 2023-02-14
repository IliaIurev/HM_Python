n = int(input('Введите количество кустов: '))
print('Введите урожайность кустов: ')
N = []
for i in range(n):
    N.append(int(input()))
summ = 0
Koord = [0,0,0]
for i in range(1, n-1):
    m = i
    if N[i]+N[i-1]+N[i+1]>summ:
        summ = N[i]+N[i-1]+N[i+1]
        Koord[0] = m-1
        Koord[1] = m
        Koord[2] = m+1
print(Koord)
print(summ)