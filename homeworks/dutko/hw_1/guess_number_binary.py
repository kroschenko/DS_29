"""
Игра "Угадай число" с бинарным поиском.
Программа угадывает число пользователя за минимальное количество попыток.
"""


def get_yes_no_answer(prompt):
    """
    Запрашивает у пользователя ответ 'да' или 'нет'.
    Возвращает True, False или None (если нажат Ctrl+C).
    """
    while True:
        try:
            answer = input(prompt).strip().lower()
            if answer in ["да", "д", "yes", "y"]:
                return True
            if answer in ["нет", "н", "no", "n"]:
                return False
            print("⚠ Пожалуйста, введите 'да' или 'нет'")
        except KeyboardInterrupt:
            print("\n\n👋 Игра прервана пользователем.")
            return None


def get_comparison_answer():
    """
    Запрашивает у пользователя, больше или меньше загаданное число.
    Возвращает 'больше', 'меньше' или None (если нажат Ctrl+C).
    """
    while True:
        try:
            answer = (
                input("Ваше число больше или меньше? (больше/меньше): ").strip().lower()
            )
            if answer in ["больше", "б"]:
                return "больше"
            if answer in ["меньше", "м"]:
                return "меньше"
            print("⚠ Пожалуйста, введите 'больше' или 'меньше'")
        except KeyboardInterrupt:
            print("\n\n👋 Игра прервана пользователем.")
            return None


def format_attempts(n):
    """Возвращает правильное склонение слова 'попытка' для числа n."""
    if n == 1:
        return "1 попытку"
    elif 2 <= n <= 4:
        return f"{n} попытки"
    else:
        return f"{n} попыток"


def play_round():
    """
    Один раунд игры. Программа угадывает число от 1 до 10.
    Возвращает количество попыток или None (если игра прервана).
    """
    low = 1
    high = 10
    attempts = 0

    print("\nЗагадайте число от 1 до 10 (включительно)")
    try:
        input("Нажмите Enter, когда будете готовы...")
    except KeyboardInterrupt:
        print("\n\n👋 Игра прервана пользователем.")
        return None
    print()

    while low <= high:
        attempts += 1
        guess = (low + high) // 2

        print(f"Попытка #{attempts}: Ваше число — {guess}?")

        result = get_yes_no_answer("Угадал? (да/нет): ")
        if result is None:
            return None  # Прерывание по Ctrl+C
        if result:
            return attempts

        comparison = get_comparison_answer()
        if comparison is None:
            return None  # Прерывание по Ctrl+C

        if comparison == "больше":
            low = guess + 1
        else:
            high = guess - 1

        print()

    return -1  # Пользователь обманул


def show_stats(attempts):
    """Выводит статистику после раунда."""
    if attempts == -1:
        print("😅 Похоже, вы меня обманули! Число должно быть в диапазоне 1-10.")
    else:
        print(f"🎉 Угадал ваше число за {format_attempts(attempts)}!")

    print("📊 Максимум попыток для диапазона 1-10: 4")


def main():
    """Главная функция программы."""
    print("=" * 50)
    print("  Игра 'Угадай число'")
    print("  (с бинарным поиском)")
    print("=" * 50)

    total_rounds = 0
    total_attempts = 0

    try:
        while True:
            attempts = play_round()

            # Если play_round вернул None, значит был Ctrl+C
            if attempts is None:
                break

            show_stats(attempts)

            total_rounds += 1
            if attempts > 0:
                total_attempts += attempts

            print()
            result = get_yes_no_answer("Хотите загадать новое число? (да/нет): ")
            if result is None or not result:
                break
            print()

    except KeyboardInterrupt:
        print("\n\n👋 Игра прервана пользователем.")
    finally:
        print()
        print("=" * 50)
        if total_rounds > 0:
            avg = total_attempts / total_rounds
            print(
                f"📈 Итоговая статистика: {total_rounds} раундов, "
                f"среднее кол-во попыток: {avg:.1f}"
            )
        print("=" * 50)
        print("Спасибо за игру! До свидания! 👋")


if __name__ == "__main__":
    main()
