# Задача S "Игра в Угадайку" - Циклы - Базовые конструкции Python

# Инициализация переменных
b = 500
start = 0
end = 1001

print(b)

# Главный цикл
while (a := str(input())) != "Угадал!":
    if a == "Больше":
        start = b
        b = b + ((end - start) // 2)
    elif a == "Меньше":
        end = b
        b = b - ((end - start) // 2)
    print(b)

