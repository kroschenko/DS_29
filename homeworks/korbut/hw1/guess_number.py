def playGame():
    print("Задумай число от 1 до 10, я попробую его угадать!")
    input("Нажми Enter, когда будешь готов...")

    low = 1
    high = 10
    attempt = 1

    while True:
        guess = (low + high) // 2
        print(f"Попытка {attempt}: моё число — {guess}")

        answer = input("Угадал, больше или меньше? (угадал/больше/меньше): ").strip().lower()

        if answer == "угадал":
            print(f"Отлично! Угадал за {attempt} попыток(ку)!")
            break
        elif answer == "больше":
            low = guess + 1
        elif answer == "меньше":
            high = guess - 1
        else:
            print("Не поняла ответ, попробуй ввести: угадал / больше / меньше")
            continue

        attempt += 1

def main():
    while True:
        playGame()
        again = input("\nХочешь загадать новое число? (да/нет): ").strip().lower()
        if again != "да":
            print("Спасибо за игру!")
            break
        print()

main()
