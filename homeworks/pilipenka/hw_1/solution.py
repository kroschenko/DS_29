def calculate_rectangle_area(a: float, b: float) -> float:
    """
    Рассчитывает площадь прямоугольника по двум сторонам.
    
    Args:
        a: Длина первой стороны
        b: Длина второй стороны
        
    Returns:
        Площадь прямоугольника
    """
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть положительными числами")
    return a * b


if __name__ == "__main__":
    try:
        side_a = float(input("Введите длину первой стороны: "))
        side_b = float(input("Введите длину второй стороны: "))
        
        area = calculate_rectangle_area(side_a, side_b)
        print(f"Площадь прямоугольника: {area}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
