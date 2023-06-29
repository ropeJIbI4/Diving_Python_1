#Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

from random import randint

def guess_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 100
    COUNT_TRY = 2
    RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
    is_win = True
    for _ in range(COUNT_TRY + 1):
        number = int(input('Введи число от 0 до 1000: '))
        if number > RAND_NUMBER:
            print('Ваше число БОЛЬШЕ загаданного')
            is_win = False
        elif number < RAND_NUMBER:
            print('Ваше число МЕНЬШЕ загаданного')
            is_win = False
        else:
            print('Вы выиграли!')
            is_win = True
    if not is_win:
        print('К сожалению вы проиграли')

guess_number()