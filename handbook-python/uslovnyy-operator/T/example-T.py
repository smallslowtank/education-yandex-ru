# Зачада Зайка-2 - Условный оператор - Базовые функции Python
# Важное слово - лексиграфически
# То есть сравниваем не длинну строк, а побуквенно
# Выбирается строка, которая начинается с буквы с наименьшим кодом символа

a = str(input())
b = str(input())
c = str(input())

z = ""

# Проверяем строку а
if ("зайка" in a):
    z = a

# Проверяем строку б
if ("зайка" in b) and (b <= z or z == ""):
    z = b

# Проверяем строку с
if ("зайка" in c) and (c <= z or z == ""):
    z = c

# Печать результата
print(z, len(z))

