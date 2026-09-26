import random


class GameSimple:

    def play(self) -> None:
        while True:
            self.__run_game()

            again = self.__get_answer("Do you want to play again")
            if not again:
                break

    def __run_game(self) -> None:
        print("Please guess the number from 1 to 10")
        input("Press Enter to start...")

        state = [i for i in range(1, 11)]
        random.shuffle(state)

        check = False
        attempts = 0

        while check == False:
            if len(state) == 0:
                print("Dishonest player!")
                break

            attempts += 1
            number = state.pop()
            label = f"Your number is {number}"
            check = self.__get_answer(label)

        print(f"Game over, guessed the number in {attempts} attempts")

    def __get_answer(self, label: str) -> bool:
        print(f"{label}? (y/n) ")

        while True:
            res = input().lower()
            if res == "y":
                return True
            elif res == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


GameSimple().play()
