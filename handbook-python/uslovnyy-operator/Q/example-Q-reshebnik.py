# Вариант из Решебника
# https://reshebnik.mumuproject.com/frontpage/yandex-python-handbook/yandex-python-2-2-uslovniy-operator/yandex-handbook-koren-zla/

a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c != 0:
    print(f'{-(c / b):.2f}')
elif a == b == 0:
    print('No solution')
elif a == c == 0:
    print(0)
else:
    disc = (b ** 2) - (4 * a * c)
    if disc == 0:
        print(f'{(-b) / (2 * a):.2f}')
    elif disc > 0:
        x1 = (-b - (disc ** 0.5)) / (2 * a)
        x2 = (-b + (disc ** 0.5)) / (2 * a)
        print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')
    else:
        print('No solution')
