# This a biginner project that simulate the game of rock paper scissors.

# import the random mudule for generating computers choice in the game.
import random

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
# create a list of game art to be selected
game_basket = [rock, paper, scissors]

# Ask the user of their choices. represent the game choice rock with 0, paper with 1 and scissors with 2
users_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

computer_choice = random.randint(0, 2)

# check users choice against computers choice. using game display the winner
if users_choice >=3 or users_choice <= 0:
    print("Invalid number You lose.")
else:
        # display the art that corresponds to users choice
    print(f"You chose\n{game_basket[users_choice]}\n")

    # display the art that corresponds to computers choice
    print(f"computer chose\n{game_basket[computer_choice]}")

    if users_choice == 0 and computer_choice == 2:
        print("You won!")
    elif computer_choice == 0 and users_choice == 2:
        print("You lose!")
    elif users_choice > computer_choice:
        print("You win!")
    elif computer_choice > users_choice:
        print("You lose!")
    else:
        print("It's a draw!")

 
