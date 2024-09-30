# Вариант1

num = int(input())

divisor = 2
prime = True

if num <= 1:
    prime = False
else:
    for divider in range(2, int(num**0.5 + 1)):
        if num % divider == 0:
            prime = False
            break

if prime is True:
    print('YES')
else:
    print('NO')


# Вариант 2

num = int(input())

divisor = 2
prime = True

if -1 <= num <= 1:
    prime = False
else:
    while divisor ** 2 <= num and prime is True:
        if num % divisor == 0:
            prime = False
        else:
            divisor = divisor + 1

if prime is True:
    print('YES')
else:
    print('NO')


