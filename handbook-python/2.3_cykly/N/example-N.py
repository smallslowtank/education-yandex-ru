# Задача N "Простая задача" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 2
n = int(input())
s = 1
flag = 'YES'

# Главный цикл
if n == 1:
    flag = 'NO'
elif n == 2:
    flag = 'YES'
else:
    for i in range(k, n, s):
        if n / i == n // i:
            flag = 'NO'
print(flag)
# Превышен лимит времени

