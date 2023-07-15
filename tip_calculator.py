# This is a beginner level project that calculate the tips for amount spent during after a meal

# print a welcome message to the user
print("Welcome to the tip calculator!")

# Request the total till
bill = float(input("What is your total bill?: $"))

# Ask the tip percentage
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15: "))

# Get the number of people at the meal
number_people = int(input("How many people to split the bill?: "))

# calculate the tip amout
tip_amount = bill * (tip_percent /100)

# calculate the total bill with percentage tip
total_bill = bill + tip_amount


# share the bill to the number of people at the meal and round to two decimal places
bill_per_person = round(total_bill / number_people, 2)

# display the bill per person
print(f"Each person should pay: ${bill_per_person}")