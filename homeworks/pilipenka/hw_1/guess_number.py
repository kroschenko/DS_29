class GuessNumberGame:
    def __init__(self, min_val=1, max_val=10):
        self.min_val = min_val
        self.max_val = max_val
        self.attempts = 0

    def start_new_game(self):
        """Сбрасывает границы поиска для новой игры."""
        self.current_min = self.min_val
        self.current_max = self.max_val
        self.attempts = 0
        print(f"Загадайте число от {self.min_val} до {self.max_val}.")
        print("Отвечайте на мои вопросы: 'больше', 'меньше' или 'да'.")

    def make_guess(self) -> int:
        """Программа делает предположение (середина текущего диапазона)."""
        return (self.current_min + self.current_max) // 2

    def update_bounds(self, user_response: str, guess: int):
        """Обновляет границы поиска на основе ответа пользователя."""
        if user_response == 'меньше':
            self.current_max = guess - 1
        elif user_response == 'больше':
            self.current_min = guess + 1

    def play(self):
        """Основной цикл игры."""
        while True:
            self.start_new_game()
            
            while self.current_min <= self.current_max:
                self.attempts += 1
                guess = self.make_guess()
                
                response = input(f"Это число {guess}? (да/больше/меньше): ").lower().strip()
                
                if response == 'да':
                    print(f"Ура! Я угадал число {guess} за {self.attempts} попыток!")
                    break
                elif response in ['больше', 'меньше']:
                    self.update_bounds(response, guess)
                else:
                    print("Пожалуйста, ответьте 'да', 'больше' или 'меньше'.")
                    self.attempts -= 1 # Не считаем некорректный ввод за попытку
            
            if self.current_min > self.current_max:
                print("Кажется, вы ошиблись в ответах, так как диапазон поиска исчерпан.")
            
            again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
            if again != 'да':
                print("До встречи!")
                break

if __name__ == "__main__":
    game = GuessNumberGame(1, 10)
    game.play()
