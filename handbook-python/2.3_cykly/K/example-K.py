# Задача K "Цифровая сумма" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
a = int(input())
a_sum = 0
k = 0
n = len(str(a))
s = 1

# Главный цикл
for i in range(k, n, s):
    a_sum = a_sum + a % 10
    a = a // 10
    
# Вывод резельтата
print(a_sum)

