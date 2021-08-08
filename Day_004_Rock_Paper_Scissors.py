rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 Scissors. "))
if user_choice >= 3 or user_choice < 0:
  print("You entered an invalid number. You lose")
else:
  print(game_images[user_choice])

  print("Computer chooses: \n")
  com_choice = random.randint(0,2)
  print(game_images[com_choice])

  if (user_choice == 0 and com_choice == 2) or (user_choice == 1 and com_choice == 0) or (user_choice == 2 and com_choice == 1):
    print("You win!")
  elif (com_choice == 0 and user_choice == 2) or (com_choice == 1 and user_choice == 0) or (com_choice == 2 and user_choice == 1):
    print("You lose :(")
  else:
    print("It's a draw.")



