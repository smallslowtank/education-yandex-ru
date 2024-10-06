# Задача E "Зайка-5" - Вложенные циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 0
n = int(input())
s = 1
z = 0
flag = 0

# Главный цикл
for i in range(k, n, s):
    while (m := str(input())) != "ВСЁ":
        if m == "зайка":
            flag = 1
    if flag == 1:
        z = z + 1
        flag = 0

# Вывод результата
print(z)

