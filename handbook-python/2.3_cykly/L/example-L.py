# Задача L "Сильная цифра" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
a = int(input())
k = 0
n = len(str(a))
s = 1
a_max = 0

# Глаыный цикл
for i in range(k, n, s):
    if a_max < (a % 10):
        a_max = a % 10
    a = a // 10

# Вывод результата
print(a_max)

