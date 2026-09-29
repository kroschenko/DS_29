print("Игра отгадай число от 1 до 10")
print("Вводите <,>,= в зависимости от вашего загаданного числа и заданного вопроса")
print("Если хотите выйти, введите q")
min=1
max=10
attempt=0


while min<=max:
        attempt+=1
        middle=(max+min)//2
        answer=input(f"Попытка {attempt}:\nВаше число {middle}?")
        
         # Проверка на продолжение цикла или прерывание  
        if answer.lower() in ['q']:
            print("Програма завершена.")
            break
        
        
        # Проверяем на попадание
        if answer.lower() in ['=']:
            print(f"Я отгадал число {middle} за {attempt} попыток. Давайте снова сыграем!")
            attempt=0


        if answer.lower() in ['<']:
            max=middle-1
       
       
        if answer.lower() in ['>']:
            min=middle+1        

    
    