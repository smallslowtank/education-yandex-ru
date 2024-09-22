# Задача Q Корень зла - 2.2 Условный оператор - 2 Базовые конструкции Python

a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    # Если все аргументы раны нулю, то решений бесконечное количество
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    # Если только а рано нулю, то решаем линейное уравнение
    print(round((-c / b), 2))
elif a == b == 0:
    # Если а и б равны нулю, а с не равно нулю, то решения не существует
    print("No solution")
elif a == c == 0:
    # Если а и с равны нулю, а б не равно нулю, то х равен нулю
    print(0)
else:
    # Решаем уравнение через дискриминант
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        # Если дискриминант больше нуля, то есть два решения
        x1 = (-b + pow(discriminant, 1 / 2)) / (2 * a)
        x2 = (-b - pow(discriminant, 1 / 2)) / (2 * a)
        print(round(min(x1, x2), 2), round(max(x1, x2), 2))
    elif discriminant == 0:
        # Если дискриминант равен нулю, то одно решение
        print(round((-b / (2 * a)), 2))
    else:
        # Если дискриминант меньше нуля, то решения нет
        print("No solution")
