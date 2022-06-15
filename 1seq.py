list_items = int(input('Введите количество: '))
list_user = []
for i in range(list_items):
    user_nubers = input('Введите число: ')
    list_user.append(user_nubers)
list_user.sort()
print(list_user)
