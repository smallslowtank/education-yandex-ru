# Задача B "Не таблица умножения" - Вложенные циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 1
n = int(input())
s = 1

# Главный цикл
for x in range(k, n + 1, s):
    for y in range(k, n + 1, s):
        print(str(y) + " * " + str(x) + " = " + str(x * y))

