# Задача D_Считалочка_2.0 - Циклы - Базовые_конструкции_Python

# Инициализация переменных и ввод данных
str_output = ""
k = int(input())
n = int(input())
s = 1
if k > n:
    s = -1

# Основной цикл
for i in range(k, n, s):
    str_output = str_output + str(i) + " "

# Добавить последнее число в диапазоне и вывод результата
str_output = str_output + str(n)
print(str_output)

