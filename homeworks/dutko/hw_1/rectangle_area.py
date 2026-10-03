def calculate_area(length, width):
    """Функция для расчёта площади прямоугольника"""
    return length * width


def get_positive_float(prompt):
    """Функция для безопасного ввода положительного числа"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("⚠ Ошибка: значение должно быть больше нуля! Попробуйте снова.\n")
                continue
            return value
        except ValueError:
            print(
                "⚠ Ошибка: введено не число! Пожалуйста, введите числовое значение.\n"
            )
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            exit()
        except Exception as e:
            print(f"⚠ Неожиданная ошибка: {e}. Попробуйте снова.\n")


def main():
    """Основная функция программы"""
    print("=" * 50)
    print("  Программа для расчёта площади прямоугольника")
    print("=" * 50)
    print()

    try:
        # Ввод сторон с обработкой ошибок
        length = get_positive_float("Введите длину прямоугольника: ")
        width = get_positive_float("Введите ширину прямоугольника: ")

        # Расчёт площади
        area = calculate_area(length, width)

        # Вывод результата
        print()
        print("-" * 50)
        print("📊 Результат:")
        print(f"   Длина:   {length}")
        print(f"   Ширина:  {width}")
        print(f"   Площадь: {area}")
        print("-" * 50)

        # Дополнительная информация
        perimeter = 2 * (length + width)
        print(f"   Периметр: {perimeter}")
        print("-" * 50)

    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем (Ctrl+C).")
    except Exception as e:
        print(f"\n❌ Произошла непредвиденная ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()
