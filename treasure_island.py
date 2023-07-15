# This beginner level project to test undestanding on conditional logic.


print("""
      
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
      
""")

# dsiplay a welcome message and mission of the game
print("Welcome to Treasure Island\nYour mission is to find the treasure.")

# Ask the user for their cross road decision. between moving right or left
cross_road_direction = input("You are at a cross road. Where do you want to go? Type 'Right' or 'Left': ").lower()

# check for the users cross road decision
if cross_road_direction =="left":

    # Ask the user for the action performed at the river.  between swimming or waiting
    river_action = input("You have arrive at a river. What do you want to do? Type 'Swim' or 'Wait': ").lower()

    # check the user river action.
    if river_action == 'wait':

        # Ask the user for their door choice. between red, blue and yellow
        door_choice = input("Three doors appeared. Which door do you want to choose? Type 'Red', 'Blue' or 'Yellow': ").lower()

        # check their door choice
        if door_choice =='yellow':
            print("You found it 🪙")
        elif door_choice =="red":
            print("Burn by fire. Game Over 💀")
        elif door_choice =="blue":
            print("Eaten by a beast. Game Over 💀")
        else:
            print("Wrong entry. Game Over 💀")
        

    else:
        print("Attacked by trout. Game Over 💀")

        
else:
    print("You fell into a hole. Game Over 💀")