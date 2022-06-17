number_first = input('Введите ряд чисел с раздилителями "/" или "," или ";"')
number_second = input('Введите ряд чисел с раздилителями "/" или "," или ";"')
number_first = number_first.replace(';', ',').replace('/', ',').split(',')
number_second = number_second.replace(';', ',').replace('/', ',').split(',')
print(type(number_first))
print(type(number_second))
number_three = []
# с применением цикла c удалением всех вхождений
for i in number_first:
    if i not in number_second:
        number_three.append(i)
print(number_three)
# с применением set уникальные значения и удаления 2-го списка
print(list(set(number_first)-set(number_second)))