from art import logo
import os
print(f'{logo}')
print('Welcome to secret auction program')


bidders_registry = {}
auction_ongoing = True

while auction_ongoing:   
    auction_bidder = input('What is your name?: ')
    bidders_amount = int(input("What's your bid?: $"))
    bidders_registry[auction_bidder]=bidders_amount
    other_bidders = input("Are there any other bidders? Type 'yes' or no ").lower()
    if other_bidders =='no':
        auction_ongoing = False
    os.system('cls')

winner = ''
winners_bid = 0
for key in bidders_registry:
    if bidders_registry[key] > winners_bid:
        winner = key
        winners_bid = bidders_registry[key]
print(f'The winner is {winner}, with a bid of ${winners_bid}')  