import random
secret_number = random.randint(1, 10)
print("Игра 'Угадай число!' Я загадал число от 1 до 10.")

while True:
    try:
        user_guess = int(input("Попробуйте угадать число: "))

        if user_guess == secret_number :
            print("Поздравляю.Вы угадали число!")

            play_again = input(("Хотите сыграть ещё раз? (да/нет): ")).strip().lower()
            if play_again.startswith(("д", "y")):
                secret_number = random.randint(1, 10)
                print("Я загадал новое число от 1 до 10.Угадывайте!")
                continue
            else:
                print("Спасибо за игру! До свидания.")
                break
        elif user_guess < secret_number:
            print("Загаданное число больше. Попробуйте ещё раз.")
        else:
            print("Загаданое число меньше. Попрбуйте ещё раз.")

            
    except ValueError:
        print("Пожалуйста, введите целое число.")

                   