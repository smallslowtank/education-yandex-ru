# Задача R "Простая задача 2.0" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
a = int(input())
rezultat = ""
k = 2
n = a
s = 1

# Главный цикл
for i in range(k, n, s):
    while (a / i == a // i) and (a >= i):
        if rezultat == "":
            rezultat = str(i)
        else:
            rezultat = rezultat + " * " + str(i)
        a = a / i

# Вывод результата
print(rezultat)

