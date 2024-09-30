# Задача M "Первому игроку приготовиться 2.0" - Циклы - Базовые конструкции Python

# Ввод данных и инициализация переменных
k = 0
n = int(input())
s = 1
gamer_1 = ""

for i in range(k, n, s):
    gamer = str(input())
    if gamer_1 == "":
        gamer_1 = gamer
    elif gamer_1 > gamer:
        gamer_1 = gamer

# Вывод данных
print(gamer_1)

