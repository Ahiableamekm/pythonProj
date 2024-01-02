from art import logo
import random
import os 



def deal_cards():
    """Retruns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from it"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0



    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🤝"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack 😒"
    elif user_score == 0:
        return "Win with a blackjack😊"
    elif user_score > 21:
        return "You wnet over, you lose😒"
    elif computer_score > 21:
        return "Opponent went over, you win😊"
    elif user_score > computer_score:
        return "You win😊"
    else: 
        return "You lose😒"



def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for num in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\tYour cards: {user_cards}, Current Score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_cards == 0 or user_score > 21:
            is_game_over = True
        else:
            another_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if another_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, final Score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final Score {computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls')
    print(logo)
    play_game()

