class SquareManager:
    def run(self) -> None:
        while True:
            side_a = self.__get_side("a")
            side_b = self.__get_side("b")
            print(f"The area of the rectangle is {side_a * side_b}")

            if not self.__try_again():
                break

    def __get_side(self, side: str) -> float:
        while True:
            try:
                n = float(input(f"Enter the side {side} of the rectangle: "))
                if n <= 0:
                    raise TypeError
                return n
            except ValueError:
                print("Invalid input. Please enter a number.")
            except TypeError:
                print("Invalid input. Please enter a positive number.")

    def __try_again(self) -> bool:
        print(f"Do you want to try again? (y/n) ")

        while True:
            res = input().lower()
            if res == "y":
                return True
            elif res == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


SquareManager().run()
