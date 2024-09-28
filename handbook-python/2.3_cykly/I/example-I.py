# Задача I "Факториал" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
n = int(input())
f = 1

# Главный цикл
if n == 0:
    print(f)
else:
    for i in range(1, n + 1, 1):
        f = f * i
    print(f)

