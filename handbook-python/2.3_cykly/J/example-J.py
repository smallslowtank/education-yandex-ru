# Задача J "Маршрут построен" - Циклы - Базовые конструкции Python

# Инициализация переменных - начальная точка маршрута
x = 0
y = 0

# Главный цикл
while (course := str(input())) != "СТОП":
    step = int(input())
    if course == "СЕВЕР":
        y = y + step
    elif course == "ЮГ":
        y = y - step
    elif course == "ЗАПАД":
        x = x - step
    else:
        x = x + step

# Конец маршрута, странно, но для решения задачи нужно выводить сначала у, а потом х
print(y)
print(x)

