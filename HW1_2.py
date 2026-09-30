import random


def play_game ():
    print ('Привет, начинаем игру! Угадай число от 1 до 10.')

    secret_number = random.randint (1,10)

    user_input = input ('Введите Ваше число: ')

    guess = int (user_input)

    if guess < secret_number:
        print ('Попробуйте еще раз, мое число больше.')
    elif guess > secret_number:
        print ('Попробуйте еще раз, мое число меньше.')
    else:
        print (f'Поздравляю, Вы угадали число {secret_number}!')
    