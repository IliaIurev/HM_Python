from random import randint
A = []
minn = 10
maxx = 15
B = []
for i in range(20):
    A.append(randint(0,21))
print(A)
for i in range(20):
    if A[i] >= minn and A[i] <= maxx:
        B.append(i)
print(B)