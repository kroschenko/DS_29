print("Добро пожаловать в игру 'Угадай число'!")

#Главный цикл, который отвечает за предложение "сыграть еще раз"
while True:
    print("\nЗагадайте число от 1 до 10.")
    input("Нажмите Enter, чтобы я начал угадывать...")

    low = 1
    high = 10
    game_over = False

    #Цикл угадывания внутри одного раунда
    while low <= high and not game_over:
        guess = (low + high) // 2
        print(f"\nДумаю, что это число: {guess}")

        #Цикл проверки ввода
        while True:
            user_answer = input("Ваше число больше, меньше или равно задуманному? ").strip().lower()
            if user_answer in ['больше', 'меньше', 'равно']:
                break
            print("Ошибка! Введите только слово: 'больше', 'меньше' или 'равно'.")

        #Меняем границы в зависимости от ответа
        if user_answer == 'равно':
            print(f"Ура! Я угадал число {guess}!")
            game_over = True

        elif user_answer == 'больше':
            low = guess + 1

        elif user_answer == 'меньше':
            high = guess - 1

    #Если вдруг границы пересеклись
    if low > high and not game_over:
        print("\nКажется, вы где-то ошиблись в ответах. Числа закончились!")

    #Цикл проверки ответа для новой игры
    while True:
        again = input("\nХотите загадать новое число? (да/нет): ").strip().lower()
        if again in ['да', 'нет']:
            break
        print("Пожалуйста, введите строго 'да' или 'нет'.")

    #Выходим из главного цикла
    if again == 'нет':
        print("Спасибо за игру! До свидания.")
        break