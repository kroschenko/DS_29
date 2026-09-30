MIN  = 1
MAX = 10
def game():
    """
    Игра угадывает числа от MIN до MAX, задавая наводящие вопросы.
    Формат ответа: y или n
    Валидация ответа не производится
    """
    print(f"Загадайте число от {MIN} до {MAX}")
    print("Отвечать на вопросы можно только y или n")
    found = False
    left = MIN
    right = MAX
    while not found:
        print(left,"  ", right)
        print(f"Число больше {(right+left)//2}?")
        if input() == "y":
            left = (right+left)//2
            if (right - left) == 1:
                found = True
                print(f"Загаданное число {right}")
                print("Играем еще?")
                if input()  == "n":
                    print("Игра завершена")
                else:
                    print("Новый раунд")
                    found = False
                    left = MIN
                    right = MAX
        else:
            right = (right+left)//2

game()