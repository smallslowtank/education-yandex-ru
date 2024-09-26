# Три варианта решения из Решебника

a, b = a1, b1 = int(input()), int(input())

while a != 0:
    a, b = b % a, a

print(a1 * b1 // (a + b))


a, b = int(input()), int(input())

product = a * b

while b != 0:
    a, b = b, a % b

print(product // a)


# нестандартный алгоритм нахождения НОК

a, b = int(input()), int(input())

lcm = maximum = max(a, b)
minimum = min(a, b)

while lcm % minimum != 0:
    lcm += maximum

print(lcm)

