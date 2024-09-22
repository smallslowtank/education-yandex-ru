# Задача R Территория зла - 2.2 Условный оператор - 2 Базовые конструкции Python

# Вводим стороны треугольника
a = int(input())
b = int(input())
c = int(input())

# Вычисляем косинус угла, противоположного наибольшей стороне.
# Косинус меньше нуля, то треуголник тупой
# Косинус больше нуля - острый
# Равен нулю - прямоугольный

if b < a > c:
    # Если сторона а наибольшая
    cos_a = (((b ** 2) + (c ** 2)) - (a ** 2)) / (2 * b * c)
    if cos_a == 0:
        print('100%')
    elif cos_a < 0:
        print('велика')
    else:
        print('крайне мала')
elif a < b > c:
    # Если сторона б наибольшая
    cos_b = (((a ** 2) + (c ** 2)) - (b ** 2)) / (2 * a * c)
    if cos_b == 0:
        print('100%')
    elif cos_b < 0:
        print('велика')
    else:
        print('крайне мала')
elif a < c > b:
    # Если сторона с наибольшая
    cos_c = (((b ** 2) + (a ** 2)) - (c ** 2)) / (2 * b * a)
    if cos_c == 0:
        print('100%')
    elif cos_c < 0:
        print('велика')
    else:
        print('крайне мала')
else:
    # Если стороны равны
    print('крайне мала')

