# Решение без сортировки

nature1 = input()
nature2 = input()
nature3 = input()

nature = ''

if 'зайка' in nature1:
    nature = nature1
if 'зайка' in nature2:
    if nature == '' or nature > nature2:
        nature = nature2
if 'зайка' in nature3:
    if nature == '' or nature > nature3:
        nature = nature3

print(nature, len(nature))
