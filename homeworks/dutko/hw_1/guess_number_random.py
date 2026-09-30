"""
Игра "Угадай число" - простой вариант
Программа случайным образом угадывает число, загаданное пользователем.
"""

import random


def get_yes_no(prompt):
    """
    Запрашивает у пользователя ответ 'да' или 'нет'.
    Поддерживает: "да", "д", "yes", "y" и "нет", "н", "no", "n".

    Возвращает:
        bool: True если 'да', False если 'нет'
        None: если пользователь нажал Ctrl+C
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


def guess_number():
    """
    Функция для угадывания числа от 1 до 10.
    Программа делает случайные попытки до тех пор, пока не угадает.
    """
    print("=" * 50)
    print("  Игра 'Угадай число'")
    print("=" * 50)
    print()

    while True:
        print("Загадайте число от 1 до 10")

        try:
            input("Нажмите Enter, когда будете готовы...")
        except KeyboardInterrupt:
            print("\n\n👋 Игра прервана пользователем.")
            return

        print()

        possible_numbers = list(range(1, 11))
        attempts = 0

        while possible_numbers:
            attempts += 1
            guess = random.choice(possible_numbers)

            print(f"Попытка #{attempts}: Ваше число - {guess}?")

            result = get_yes_no("Угадал? (да/нет): ")

            if result is None:
                return

            if result:
                print(f"\n🎉 Ура! Я угадал ваше число с {attempts} попытки!")
                break
            else:
                possible_numbers.remove(guess)
                print(f"Не угадал, осталось вариантов: {len(possible_numbers)}\n")

        if not possible_numbers:
            print("😅 Похоже, вы меня обманули! Число должно было быть в списке.")

        print()
        result = get_yes_no("Хотите загадать новое число? (да/нет): ")

        if result is None:
            return

        if not result:
            print("\nСпасибо за игру! До свидания!")
            break
        print()


# Запуск игры
if __name__ == "__main__":
    try:
        guess_number()
    except KeyboardInterrupt:
        print("\n\n👋 Игра прервана пользователем.")
    finally:
        print("До свидания!")
