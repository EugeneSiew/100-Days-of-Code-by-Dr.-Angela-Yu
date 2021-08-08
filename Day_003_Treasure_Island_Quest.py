print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_choice = input("You have stumbled upon a path. Which path do you take? Type 'left' or 'right'?")
first_choice_lower = first_choice.lower()
if first_choice_lower == 'left':
  second_choice = input("Congratulations! You venture on safely and found a lake. Will you swim across or wait for a boat? Type 'swim' to swim across or 'wait' to wait for a boat.")
  second_choice_lower = second_choice.lower()

  if second_choice_lower == 'wait':
    third_choice = input("You have now entered the boat and reached the treasure house. The house has 3 doors: red, yellow and blue. Which door would you choose? Type 'red' for red door, 'yellow' for yellow door or 'blue' for blue door.") 
    third_choice_lower = third_choice.lower()

    if third_choice_lower == 'yellow':
      print("Congratulations, You have found the treasure!")
    elif third_choice_lower == 'red':
      print("You have been burnt by fire. Game over :(")
    elif third_choice_lower == 'blue':
      print("You were found and eaten by beasts. Game over :(")  

  else:
     print("A few piranhas had a scent of you and chomped you. Game over :(")
else: 
  print("You have been caught by a pack of lions. Game over :(")
