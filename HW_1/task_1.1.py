def square(side_a, side_b)->float:
    print(f"Площадь прямоугольника со сторонами {side_a} и {side_b} равна {side_a*side_b}")

#для проверка стороны А
while True:
    try:
        a = float(input("Введите сторону А: "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число.")

#для проверки стороны В
while True:
    try:
        b = float(input("Введите сторону В: "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число.")

square(a,b)
