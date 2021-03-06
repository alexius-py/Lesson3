import random

name_user = input('Введите Ваше имя:')
print('Добро пожаловать в игру,', name_user)
print('Правила игры: ответы необходимо вводить в формате "ДД.ММ.ГГГГ"')
# словарь преобразования дня даты
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тренадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'дватцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцпть седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'дридцать первое'
}
# слвоарь предбровазания номера месяца
months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}
# список словарей с вопросами и ответами
quetions = [{'q': 'Дата рождения Антон Чехов', 'a': '29.01.1860'},
            {'q': 'Дата рождения Владимир Набоков', 'a': '22.04.1899'},
            {'q': 'Дата рождения Федор Достоевский', 'a': '11.11.1821'},
            {'q': 'Дата рождения Александр Солженицын', 'a': '11.12.1918'},
            {'q': 'Дата рождения Иван Бунин', 'a': '22.10.1870'},
            {'q': 'Дата рождения Иван Тургенев', 'a': '09.11.1818'},
            {'q': 'Дата рождения Николай Гоголь', 'a': '01.04.1809'},
            {'q': 'Дата рождения Михаил Булгаков', 'a': '15.05.1891 '},
            {'q': 'Дата рождения Лев Толстой', 'a': '09.09.1910'},
            {'q': 'Дата рождения Александр Пушкин', 'a': '26.05.1799'}]
quetions_random = random.sample(quetions, len(quetions))

new_game = "д"
while True:
    if new_game == "н":
        print("До скорой встречи", name_user)
        break
    elif new_game == "д":
        wow = 0
        loss = 0
        new_game = "None"
        for i in quetions_random:
            print(i['q'])
            answer_user = input('Введите ответ: ')
            answer = i['a']
            day, month, year = answer.split('.')
            if answer_user == answer:
                print(days[day], months[month], year, 'года')
                wow += 1
            else:
                print('Ответ не верен')
                loss += 1
        print("Правельных ответов:", wow)
        print("Неправельных ответов:", loss)
        print("Процент правельных ответов", (wow * 100) / 5)
        print("Процент неправельных ответов", (loss * 100) / 5)
        if wow == 0:
            print(name_user, "твоя оценка НЕУТ!!! (СРОЧНО В ШКОЛУ)")
        elif 1 <= wow <= 2:
            print(name_user, "твоя оценка ПЛОХО, (нужно больше читать)")
        elif wow == 3:
            print(name_user, "твоя оценка УДОВЛЕТВОРИТЕЛЬНО")
        elif wow == 4:
            print(name_user, "твоя оценка ХОРОШО!!")
        else:
            print(name_user, "твоя оценка ОТЛИЧНО!!!")
    else:
        new_game = input("Повторим д (да)/н (нет):")
