# Задача Q Корень зла - 2.2 Условный оператор - 2 Базовые конструкции Python

a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    # Если все аргументы раны нулю, то решений бесконечное количество
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    # Если только а рано нулю, то решаем линейное уравнение
    print(-c / b)
elif a != 0 and b == 0 and c != 0:
    # Если только б равно нулю, дополнительно проверяем на наличие решения у уравнения
    if (c / a) < 0:
        # Если б равно нулю, а и с больше нуля, то решений нет
        print("No solutions")
    else:
        # Решаем уравнение
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + pow(discriminant, 1 / 2)) / (2 * a)
            x2 = (-b - pow(discriminant, 1 / 2)) / (2 * a)
            if x1 < x2:  
                print(round(x1, 2), round(x2, 2))
            else:
                print(round(x2, 2), round(x1, 2))
        elif discriminant == 0:
            print(round(-b / (2 * a), 2))
        else:
            print("No solutions")
        
else:
    # Решаем уравнение
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + pow(discriminant, 1 / 2)) / (2 * a)
        x2 = (-b - pow(discriminant, 1 / 2)) / (2 * a)
        if x1 < x2:  
            print(round(x1, 2), round(x2, 2))
        else:
            print(round(x2, 2), round(x1, 2))
    elif discriminant == 0:
        print(round(-b / (2 * a), 2))
    else:
        print("No solutions")