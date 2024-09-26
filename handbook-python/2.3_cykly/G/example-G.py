# Задача G "НОК" - Циклы - Базовые конструкции Python

# Ввод данных
a = int(input())
b = int(input())

# Главный цикл
k = a * b
n = 0
s = -1
for i in range(k, n, s):
    if ((i / a) == (i // a)) and ((i / b) == (i // b)):
        c = i

# Вывод результата
print(c)
