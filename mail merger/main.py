with open("./Input/Letters/starting_letter.txt") as letter:
    message = letter.read()


with open("./Input/Names/invited_names.txt") as name_file:
    name_lists = name_file.readlines()
    for name in name_lists:
        name = name.strip("\n")

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as Output:
            personalised = message.replace("[name]", name)
            Output.write(personalised)