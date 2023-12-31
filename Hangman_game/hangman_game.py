import random
import hangman_art
import hangman_words
import os

# List of words to select from.
word_list = hangman_words.word_list

# randomly select a word
chosen_word = random.choice(word_list)

print(f'{hangman_art.logo}')
# print(f'psst! the chosen word is {chosen_word}')

# Generate as many "-" as there are letters in the chosen_word
display = ["_" for letter in chosen_word]


lives = 6
end_of_game = False



while not end_of_game:
    users_guess = input('Guess a letter: ').lower()
    os.system('cls')

    if users_guess in display:
        print(f"You've already guessed {users_guess}")
        
    for position, letter in enumerate(chosen_word):
        if users_guess == letter:
            display[position]=users_guess

    print(" ".join(display))
    if '_' not in display:
        end_of_game = True
        print('You Won!')

    if users_guess not in chosen_word:
        print(f"you guessed letter {users_guess}, That's not in the word. You lose a life")
        lives -= 1
    
        if lives == 0:
            end_of_game = True
            print('\n\nGame Over')

    print(f'{hangman_art.stages[lives]}')