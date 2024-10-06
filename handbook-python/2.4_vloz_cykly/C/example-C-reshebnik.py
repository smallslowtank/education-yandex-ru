# Решение с вложенными циклами

dim = int(input())

count = 1
num = 1

while num <= dim:
    for i in range(count):
        if num > dim:
            break
        print(num, end=' ')
        num += 1
    print()
    count += 1


# Решение с одни циклом

finish = int(input())

limit = 1
current = 0

for pos in range(finish):
    current += 1
    print(pos + 1, end=' ')
    if current == limit:
        print()
        limit += 1
        current = 0

