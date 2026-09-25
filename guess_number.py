play = "да"
while play == "да":
    print("Задумайте число от 1 до 10.")
    input("Когда будете готовы, нажмите Enter...")

    guess = 1
    answer = "нет"
    while answer != "да":
        print("Я думаю, это", guess)
        answer = input("Я угадала? (да/нет): ")
        guess = guess + 1

    print("Угадала!")
    play = input("Загадаете новое число? (да/нет): ")

print("Спасибо за игру.")
