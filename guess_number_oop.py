class NumberGuessingGame:
    def __init__(self):
        # Границы диапазона хранятся в самом объекте.
        self.low = 1
        self.high = 10

    def play(self):
        play_again = "да"
        while play_again == "да":
            print(f"Задумайте число от {self.low} до {self.high}.")
            input("Когда будете готовы, нажмите Enter...")

            guess = self.low
            answer = "нет"
            while answer != "да":
                print("Я думаю, это", guess)
                answer = input("Я угадала? (да/нет): ")
                guess = guess + 1

            print("Угадала!")
            play_again = input("Загадаете новое число? (да/нет): ")

        print("Спасибо за игру.")


game = NumberGuessingGame()
game.play()
