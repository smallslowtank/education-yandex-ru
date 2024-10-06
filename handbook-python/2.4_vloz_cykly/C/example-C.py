# Задача C "Новогоднее настроение" - Вложенные циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 1
n = int(input())
s = 1
x = 1
y = 1
a = ""

# Главный цикл
for i in range(k, n + 1, s):
    if a == "":
        a = str(i)
    else:
        a = a + " " + str(i)
    if x == y:
        print(a)
        x = 1
        y = y + 1
        a = ""
    else:
        x = x + 1
if a != "":
    print(a)

