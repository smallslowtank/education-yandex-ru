# Три варианта решения из Решебника

# Простое решение с вычитанием

a, b = int(input()), int(input())

while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a

print(a + b)


# Ускоренное решение с имспользованием остатка от деления

a, b = int(input()), int(input())

while a != 0 and b != 0:
    if a >= b:
        a %= b
    else:
        b %= a

print(a + b)


# Продвинутое решение с имспользованием остатка от деления

a, b = int(input()), int(input())

while a != 0:
    a, b = b % a, a

print(b)

