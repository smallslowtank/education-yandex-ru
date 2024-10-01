# Задача Q "Чётная чистота" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
a = int(input())
len_a = len(str(a))
k = 0
n = len_a
s = 1
b = ""

# Главный цикл
for i in range(k, n, s):
    c = a % 10
    if (c / 2) != (c // 2):
        b = str(c) + b
    a = a // 10

# Вывод результата
print(int(b))

