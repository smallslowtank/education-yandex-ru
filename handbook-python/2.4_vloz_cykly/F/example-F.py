# Задача F "НОД 2.0" - Вложенные циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 1
n = int(input())
s = 1
a = int(input())

# Главный цикл
for i in range(k, n, s):
    b = int(input())
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    a = a + b

# Вывод результата
print(a)

