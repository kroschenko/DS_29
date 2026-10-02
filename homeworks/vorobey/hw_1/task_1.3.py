class NumberGuesser:
    """Класс для игры 'Угадай число', где компьютер угадывает число пользователя."""

    def __init__(self, min_value: int = 1, max_value: int = 10):
        # Инициализируем стартовые настройки игры
        self.min_value = min_value
        self.max_value = max_value
        self.low = min_value
        self.high = max_value
        self.game_over = False

    def _reset_round(self):
        """Сброс границ перед началом нового раунда."""
        self.low = self.min_value
        self.high = self.max_value
        self.game_over = False

    def _get_valid_answer(self) -> str:
        """Внутренний метод для безопасного ввода подсказки (больше/меньше/равно)."""
        while True:
            answer = input("Ваше число больше, меньше или равно задуманному? ").strip().lower()
            if answer in ['больше', 'меньше', 'равно']:
                return answer
            print("Ошибка! Введите только слово: 'больше', 'меньше' или 'равно'.")

    def _get_valid_again(self) -> str:
        """Внутренний метод для безопасного ответа на продолжение игры (да/нет)."""
        while True:
            answer = input("\nХотите загадать новое число? (да/нет): ").strip().lower()
            if answer in ['да', 'нет']:
                return answer
            print("Пожалуйста, введите строго 'да' или 'нет'.")

    def play_round(self):
        """Логика одного раунда угадывания."""
        self._reset_round()
        print(f"\nЗагадайте число от {self.min_value} до {self.max_value}.")
        input("Загадали? Нажмите Enter, чтобы я начал угадывать...")

        # Цикл бинарного поиска внутри раунда
        while self.low <= self.high and not self.game_over:
            guess = (self.low + self.high) // 2
            print(f"\nДумаю, что это число: {guess}")

            user_answer = self._get_valid_answer()

            if user_answer == 'равно':
                print(f"Ура! Компьютер угадал число {guess}!")
                self.game_over = True

            elif user_answer == 'больше':
                self.low = guess + 1  # Сужаем диапазон снизу

            elif user_answer == 'меньше':
                self.high = guess - 1  # Сужаем диапазон сверху

        # Если границы пересеклись, значит пользователь где-то ошибся
        if self.low > self.high and not self.game_over:
            print("\nКажется, вы где-то ошиблись в ответах. Числа закончились!")

    def start(self):
        """Главный метод для запуска игры и управления перезапуском."""
        print("Добро пожаловать в игру 'Угадай число'!")

        while True:
            self.play_round()

            again = self._get_valid_again()
            if again == 'нет':
                print("Спасибо за игру! До свидания.")
                break


# Запуск игры при прямом вызове файла
if __name__ == "__main__":
    # Создаем объект игры (здесь можно легко поменять диапазон, например на 1-100)
    game = NumberGuesser(min_value=1, max_value=10)
    # Запускаем игровой процесс
    game.start()