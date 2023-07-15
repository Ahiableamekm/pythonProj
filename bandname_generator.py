# This project is a beginners project that generate band name base on the city one grows in and their favorite pet name


# print a welcome message for the project
print("Welcome band name generator!")



# Take the city from which player grew in.
city = input("Enter the name of the city you grew in:\n")

# Take the favorite pet name of the player
pet = input("Enter the name of your favorite pet: ")

# combine the city name and pet name to create bandname
bandname = f'{city} {pet}'

# Display bandname generated to the user.
print("Your Band name would  be: "+bandname)