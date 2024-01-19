import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def genrate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, Only letters in the alpabet please")
        genrate_phonetic()
    else:
        print(phonetic_list)
        
genrate_phonetic()