# Задача A "Таблица умножения" - Вложенные циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 1
n = int(input())
s = 1
stroka = ""

# Главный цикл
for y in range(k, (n + 1), s):
    for x in range(k, (n + 1), s):
        if stroka == "":
            stroka = str(x * y)
        else:
            stroka = stroka + " " + str(x * y)
    print(stroka)
    stroka = ""

