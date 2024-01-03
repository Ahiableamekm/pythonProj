from art import logo
import random


EASY_LIVE = 10
HARD_LIVE = 5

def check_answer(user_guess, computer_guess, lives):
    if user_guess > computer_guess:
        print('Too high!')
        return lives - 1
    elif user_guess < computer_guess:
        print('Too low')
        return lives - 1
    else:
        print(f"You go it. The answer is {computer_guess}")
        
def game_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level =='easy':
        return EASY_LIVE
    else:
        return HARD_LIVE
    

def game():

    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of number between 1 and 100. ")
    computer_guess = random.randint(0, 100)
    game_lives = game_level()
    player_guess = 0

    while player_guess != computer_guess:

        print(f"You have {game_lives} remaining to guess the number")
        player_guess = int(input('Make a guess: '))
        game_lives = check_answer(player_guess, computer_guess, game_lives)

        if game_lives == 0:
            print('You run out of lives')
            return
        elif player_guess != computer_guess:
            print('Guess again')
    
game()

