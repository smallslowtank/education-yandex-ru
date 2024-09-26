# Задача F "НОД" - Циклы - Базовые конструкции Python

# Получить два числа на входе
a = int(input())
b = int(input())

# Основной цикл
s = 1
k = 1
if a >= b:
    n = b + 1
else:
    n = a + 1
for i in range(k, n, s):
    if ((a / i) == (a // i)) and ((b / i) == (b // i)):
        c = i

# Вывод результата
print(c)

