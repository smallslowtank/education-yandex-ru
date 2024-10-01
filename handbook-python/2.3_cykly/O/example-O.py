# Задача O "Зайка-4" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 0
n = int(input())
s = 1
line_z = 0
z = "зайка"

# Главный цикл
for i in range(k, n, s):
    line = str(input())
    if z in line:
        line_z = line_z + 1

# Вывод результата
print(line_z)

