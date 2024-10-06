# Задача D "Суммарная сумма" - Вложенные циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 0
n = int(input())
s = 1
n_sum = 0

# Главный цикл
for i in range(k, n, s):
    a = int(input())
    a_len = len(str(a))
    for x in range(k, a_len, s):
        n_sum = n_sum + (a % 10)
        a = a // 10

# Вывод результата
print(n_sum)

