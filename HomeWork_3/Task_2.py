A = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
# 1
B = ["D", "G"]
# 2
C = ["B", "C", "M", "P"]
# 3
D = ["F", "H", "V", "W", "Y"]
# 4
E = ["K"]
# 5
F = ["J", "X"]
# 8
J = ["Q", "Z"]
# 10
A1 = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
# 1
B1 = ["Д", "К", "Л", "М", "П", "У"]
# 2
C1 = ["Б", "Г", "Ё", "Ь", "Я"]
# 3
D1 = ["Й", "Ы"]
# 4
E1 = ["Ж", "З", "Х", "Ц", "Ч"]
# 5
F1 = ["Ш", "Э", "Ю"]
# 8
J1 = ["Ф", "Щ", "Ъ"]
# 10
slovo = str(input("Введите слово заглавными буквами: "))
summ = 0
for i in range(len(slovo)):
    if slovo[i] in A:
        summ += 1
    if slovo[i] in B:
        summ += 2
    if slovo[i] in C:
        summ += 3
    if slovo[i] in D:
        summ += 4
    if slovo[i] in E:
        summ += 5
    if slovo[i] in F:
        summ += 8
    if slovo[i] in J:
        summ += 10
    if slovo[i] in A1:
        summ += 1
    if slovo[i] in B1:
        summ += 2
    if slovo[i] in C1:
        summ += 3
    if slovo[i] in D1:
        summ += 4
    if slovo[i] in E1:
        summ += 5
    if slovo[i] in F1:
        summ += 8
    if slovo[i] in J1:
        summ += 10
print(summ)
