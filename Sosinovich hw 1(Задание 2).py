import random


class GuessNumberGame:
    def __init__(self):
        self.low = 1
        self.high = 10
        self.attempts = 0

    def start(self):
        while True:
            print("\n Новая Игра")    
            print(f"Загадайте число от {self.low} до  {self.high} в уме.")
            input("Как будете готовы,нажмите Enter...")
            
            self.play_round()

            play_again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower() #Предложение задумать новое число
            if play_again not in ["да","д", "yes","y"]:
               print("Спасибо за игру.Отличная игра!")
               break

    def play_round(self): #Сброс счетчика для нового раунда
        current_low = self.low
        current_high = self.high
        self.attempts = 0

        while current_low <= current_high:
              #использование алгоритма бинар поиска
              guess = (current_low + current_high)//2
              self.attempts += 1

              print(f"\nПопытка №{self.attempts}. Компьютер думает что это {guess}")
              answer = (
                  input("Я угадал? (да/ меньше/ больше): ").strip().lower()
              )

              if answer in ["да", "угадал", "y"]:
                  print(
                      f"Бинго! Компьютер угадал число {guess} за {self.attempts} ходов."
                  )
                  return
              elif answer == "меньше":          #если число меньше названного
                  current_high = guess - 1
              elif answer == "больше":          #если число больше названного
                  current_low = guess + 1
              else:
                   print(
                       "Неверный ввод. Ответьте: 'да', 'меньше' или 'больше'."
                    ) 
                   self.attempts -= 1 #не считается ошибкой

        print(
            "\nПроизошла ошибка в ответах. Границы поиска сошлись." 
        )   

#запуск проги
if __name__ == "__main__":
    game = GuessNumberGame()
    game.start()          