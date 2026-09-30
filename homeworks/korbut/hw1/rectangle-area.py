def isPositive(value, wordForError):
    if value <= 0:
        print(f"Ошибка: {wordForError} не может быть отрицательной или равной нулю!")
        return False
    return True

def getPositiveNumber(wordForInput, wordForError):
    while True:
        value = float(input(f"Введите {wordForInput} прямоугольника: "))
        if isPositive(value, wordForError):
            return value

length = getPositiveNumber("длину", "длина")
width = getPositiveNumber("ширину", "ширина")

area = length * width
print("Площадь прямоугольника:", area)
print("Рада помочь, но помни, лучше считать в уме!")
