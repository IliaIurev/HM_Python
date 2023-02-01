Num_Tick = str(input("Введите шестизначный номер билета: "))
first = int(Num_Tick[0]) + int(Num_Tick[1]) + int(Num_Tick[2])
second = int(Num_Tick[3]) + int(Num_Tick[4]) + int(Num_Tick[5])
if second == first:
    print("Это счастливый билет!")
else:
    print("Это обычный билет.")