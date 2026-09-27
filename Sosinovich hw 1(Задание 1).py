class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        return self.side_a * self.side_b
__name__ == "__main__"
a = float(input("Введите длину: "))
b = float(input("Введите ширину: "))
rect = Rectangle(a,b)
print(f"Площадь прямоугольника равна: {rect.calculate_area()}")