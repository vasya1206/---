import random
min_number = 0
max_number = 900
def start_game():
  global attempt, input_number
  attempt = 0
  print(f"Здорово брат!Я загадала число от {min_number} до {max_number}")

def game_loop():
  global attempt,input_number
  input_number=0
  case=random.randint(min_number,max_number)
  while input_number != case:
     input_number=int(input("Угадай число брат!:"))
     attempt += 1
     if input_number < case:
       print("Эщ!Число побольше бери!")
     elif input_number > case:
       print("Вай!Число поменьше бери!")
     else:
       print("Шома брат ты угадал!")
       
def end_game():
  print(f"Ты угадал число за {attempt} попыток")
start_game()
game_loop()
end_game()
      
