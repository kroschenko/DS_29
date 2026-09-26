class GameBinaryTree:

    def play(self) -> None:
        while True:
            self.__run_game()

            again = self.__get_answer("Do you want to play again")
            if not again:
                break

    def __run_game(self) -> None:
        print("Please guess the number from 1 to 10")
        input("Press Enter to start...")

        low = 1
        high = 10
        attempts = 0

        while low <= high:
            if attempts >= 4:
                print("Dishonest player!")
                break

            attempts += 1
            mid = (low + high) // 2

            check_number = self.__get_answer(f"Your number is {mid}")
            if check_number:
                break

            attempts += 1
            check_mid = self.__get_answer(f"Your number is greater than {mid}")
            if check_mid:
                if mid == high:
                    print(
                        "Dishonest player! Your number is greater than the last number."
                    )
                    break
                low = mid + 1
            else:
                if mid == low:
                    print(
                        "Dishonest player! Your number is less than the first number."
                    )
                    break
                high = mid - 1

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


GameBinaryTree().play()
