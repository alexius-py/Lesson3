# str_numbers = ""
str_numbers = input('Введите числа через запятую')
print(type(str_numbers))
str_numbers = str_numbers.replace(';', ',').replace('/', ',').split(',')
str_numbers = list(set(str_numbers))
print(str_numbers)
