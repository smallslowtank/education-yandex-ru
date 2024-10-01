# Задача P "А роза упала на лапу Азора 2.0" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
a = int(input())
len_a = len(str(a))
flag = 'YES'

# Главный цикл
if len_a > 1:                 
    while (flag == 'YES') and (len_a >= 2):
        left = a // (10 ** (len_a - 1))
        rigth = a % 10
        if left != rigth:
            flag = 'NO'
        else:
            a = (a - (left * (10 ** (len_a - 1)))) // 10
            len_a = len_a - 2

# Вывод данных
print(flag)

