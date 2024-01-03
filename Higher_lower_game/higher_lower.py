from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Format account data into printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country  = account['country']
    return f"{account_name}, a {account_description} from {account_country}"


def check_answer(answer, follower_acc_a, follower_acc_b):
    """Take user answer, follow accounts and return if they got it right"""
    if follower_acc_a > follower_acc_b:
        return answer == 'A'
    else:
        return  answer == 'B'
    
print(logo)

game_score = 0
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
  
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    follower_account_a = account_a['follower_count']
    follower_account_b = account_b['follower_count']

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    os.system('cls')
    print(logo)
    is_correct = check_answer(answer, follower_account_a, follower_account_b)
    if is_correct:
        game_score += 1
        print(f"You are correct. Current Score: {game_score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {game_score}")




# display arts

# pick random accounts

# format and display account data


# ask user for answer

# check if user is correct

# Get the account follower counts

# make the game repeatable

# make account at position a  move to position b
    
#  clear output between rounds