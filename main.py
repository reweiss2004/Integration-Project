# Ethan Weiss

# I decided to reformat my original CYOA game into more of a dungeon-crawler.
# The player will be presented with a series of rooms they can walk in and out,
# having to solve puzzles along the way.
# In one of the rooms will be a shop, where they will pretend to buy food
# (it won't really be too consequential).
# Another room will have a puzzle that makes you find the radius of a circle
# to get a key that unlocks the exit door.
# They will escape the dungeon, and that will be the end of it.

# Inspiration comes from www.makeuseof.com/python-text-adventure-game-create/
# I'll try and keep most of the code unique, but the general framework will
# be pretty similar - using def() functions to move between rooms.

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
# This is used in the puzzle to generate a unique answer every time.
import random

# I will use this for navigation. I will exclude invalid inputs if it does not
# align with the map of the dungeon I have created.
validActions = ['1', '2', '3', '4', '5', '6']
#                0    1    2    3    4    5

# Global Variables. These are going to be keys. These will change to True once
# the user solves a puzzle or interacts with something.

jail_key = False
jail_door_unlocked = False
radius_key = False


# There are two options for the jail cell - Either they have obtained the key
# by searching the bed, or they haven't. They cannot go south if they have not
# obtained the jail key.

def jail_cell():
    global jail_door_unlocked
    if jail_door_unlocked:
        still_in_loop = True
        while still_in_loop:
            print("\n>>>You are in the jail cell.")
            print("[It's dark, dreary, and gross in here.]")
            print("[You recognize this room as the place you started. "
                  "There isn't much here other than a bed and bad interior "
                  "design.]")
            print("You can go (south) from here.")
            action = input("\nActions:\n1.) South\n\n>Action: ")
            if action == validActions[0]:
                still_in_loop = False
                center_room()
            else:
                print("Invalid option.")

    else:
        global jail_key
        still_in_loop = True
        print("\n>>>You are in the jail cell.")
        print("[It's dark, dreary, and gross in here.]")
        print("There is a (bed) in the corner, and a (locked door) on the "
              "south wall.")
        while still_in_loop:
            action = input("\nActions:\n1.) Inspect Bed\n2.) Try the Locked "
                           "Door\n\n>Action: ")

            if action == validActions[0]:
                if not jail_key:
                    print("You search for and find the jail key.")
                    jail_key = True
                else:
                    print("This is where you found the jail key. Surprisingly"
                          " enough, it's not there anymore. You picked it up.")

            elif action == validActions[1]:
                if jail_key:
                    print("You unlock the locked door, and continue on into "
                          "the next room.\nCongratulations! You know how to "
                          "open a door.")
                    jail_door_unlocked = True
                    still_in_loop = False
                    center_room()
                elif not jail_key:
                    print("You jiggle the handle, and the door doesn't budge."
                          " Locked. Now, where to find the key..")
            else:
                print("ERROR: Invalid option.\nPlease enter the number"
                      " corresponding to the action you want to perform.")


# This is the center room, between the jail cell and store room.
def center_room():
    still_in_loop = True
    while still_in_loop:
        print("\n>>>You are in the center room.")
        print("[It's calm in here. Nice and quiet. The wooden floorboards"
              " creak slightly as you step on them.]")
        print("You can go (north), (south), or (east) from here.")
        action = input("\nActions:\n1.) North\n2.) South\n3.) East"
                       "\n\n>Action: ")
        if action == validActions[0]:
            still_in_loop = False
            jail_cell()
        elif action == validActions[1]:
            still_in_loop = False
            store_room()
        elif action == validActions[2]:
            still_in_loop = False
            puzzle_room()
        else:
            print("ERROR: Invalid option.\nPlease enter the number "
                  "corresponding to the action you want to perform.")


# Here is the store room. Inside of it is a shop.
def store_room():
    still_in_loop = True
    while still_in_loop:
        print("\n>>>You are in the Store Room.")
        print("You can go (north) from here.\nHere, you can see a (shop).")
        action = input("\nActions:\n1.) North\n2.) Enter the Shop"
                       "\n\n>Action: ")
        if action == validActions[0]:
            still_in_loop = False
            center_room()
        elif action == validActions[1]:
            still_in_loop = False
            shop()
        else:
            print("ERROR: Invalid option.\nPlease enter the number "
                  "corresponding to the action you want to perform.")


def shop():
    print("You enter the shop. It more closely resembles a bar than a shop."
          " There is a menu on the table. It reads:\n")
    print("(1).   Bread  - $2.50 per loaf")
    print("(2).   Wine   - $4.00 per bottle")
    print("(3).   Cookie - $1.25 each")
    print("(4).   Back away from the counter.\n")

    bread = 0
    wine = 0
    cookie = 0

    still_in_loop = True
    while still_in_loop:
        action = (input("Menu Option: "))

        # Here are the menu options - 1 for bread, 2 for wine, 3 for cookie.
        # I assume that the user is going to input an invalid number - a float
        # or negative integer every time they enter an action.
        # I combat this by using try/except to force their answer to change to
        # an integer, then use abs() to force it to be positive.

        if action == validActions[0]:
            invalid_number = True
            while invalid_number:
                try:
                    bread = abs(int(input("How many loaves of bread? ")))
                except ValueError:
                    print("- Unfortunately, you have to buy "
                          "the loaves in full.\n(Please enter a positive"
                          " integer.)")
                else:
                    invalid_number = False
            print()

        elif action == validActions[1]:
            invalid_number = True
            while invalid_number:
                try:
                    wine = abs(int(input("How many bottles of wine? ")))
                except ValueError:
                    print(
                        "- Unfortunately, you have to buy the bottles in "
                        "full.\n(Please enter a positive integer.)")
                else:
                    invalid_number = False
            print()

        elif action == validActions[2]:
            invalid_number = True
            while invalid_number:
                try:
                    cookie = abs(int(input("How many cookies? ")))
                except ValueError:
                    print(
                        "- Unfortunately, you have to buy the cookies in "
                        "full. Why wouldn't you buy a full cookie?!\n(Please"
                        "enter a positive integer.)")
                else:
                    invalid_number = False
            print()

        # When the user is done and types 'back', a small message appears that
        # calculates what would be the total of these items all added together.
        # If the total is 0, there is no message besides 'Ehh, never-mind.' If
        # the total is greater than 0, it prints the calculated message,
        # breaks the loop, and returns to the store room that the shop is in.
        elif action == validActions[3]:
            total_price = float(bread * 2.50 + wine * 4.00 + cookie * 1.25)
            if total_price > 0:
                print("With your", bread, "loaves of bread,", end=' ')
                print(wine, "bottles of wine, and", end=' ')
                print(cookie,
                      "cookies, you begin to do the math in your head.")
                print("You figure it would cost $" +
                      str(format(total_price, '.2f')) +
                      " where you come from. Somewhere else, it may have "
                      "costed something closer to $" +
                      str(format(total_price ** 2, '.2f')) + ".")
                print("With nothing stopping you from just taking it off the "
                      "shelf, you have a fine snack.")
            elif total_price == 0:
                print("Ehh, never-mind.")
            print("Finished with your business, you return to the store room.")
            still_in_loop = False
            store_room()

        # If the input is anything other than '1', '2', '3', or 'back', this
        # error message is displayed until a valid value is entered.
        else:
            print("ERROR: Invalid option.\nPlease enter the number "
                  "corresponding to the action you want to perform.\n")


def puzzle_room():
    still_in_loop = True
    while still_in_loop:
        print("\n>>>You are in the Puzzle room.")
        print("You can go (west) back to the center room or (south) to"
              " a locked door from here.")
        print("On the northern (wall), there is a small hole you could easily"
              " fit your hand into. There seems to be a slip of paper inside.")
        print("You also see a (squirrel) here.")
        action = input("\nActions:\n1.) South\n2.) West\n3.) Inspect the "
                       "wall\n4.) Talk to the Squirrel\n\n>Action: ")
        # south
        if action == validActions[0]:
            if radius_key is True and jail_key is True:
                exit()
            else:
                print("You check the door. There are two keyholes, and you "
                      "only have one!\nMaybe that squirrel has what you need.")

        # west
        elif action == validActions[1]:
            still_in_loop = False
            center_room()

        # wall
        elif action == validActions[2]:
            print("You find a note! On it reads the following:\n")
            print("~~~!!!~~~")
            print("Area = Pi * Radius squared!\nDiameter = 2 * Radius!")
            print("~~~!!!~~~")
            print("Ugh, Pi?! I hate math!")


        # I'm probably just going to make this elif into its own separate
        # 'squirrel_dialogue()', but I feel like that would make it even more
        # of a mess than it already is.
        elif action == validActions[3]:
            if not radius_key:
                print("\"" + "Hey, " * 3, "Human!\", says the squirrel.")
                print("\"I've got a question for ya! Get it right in under "
                      "three tries and I'll give you this sick key! "
                      "Whaddya say?\"\n")
                squirrelanswer = input("How do you respond?\nType (y) to "
                                       "take him up on his challenge, or "
                                       "anything else to deny him: ")
                if squirrelanswer == 'y' or squirrelanswer == 'Y':
                    still_in_loop = False
                    squirrel_game()
                else:
                    print("\"Fiiine..\", he says. \"But I've got a shiny key, "
                          "and you dont!\"")
            else:
                print("\"I already gave you your key! scram!\"")
        else:
            print("Invalid option.")


# Here, the random number is running through a calculation and assigned a
# value that the player has to match.
def calculate_diameter(radius_info):
    diameter = 2 * radius_info
    return diameter


def squirrel_game():
    radius = random.randint(1, 5)

    global radius_key

    for tries in range(2, -1, -1):
        answer = int(input("\"If the radius is " + str(radius) +
                           ", what is the diameter of a circle?\"\n"))

        # Here is where I'd reward the player with the radius key.
        if answer == calculate_diameter(radius):
            print("\"Correct! Here's your prize!\"\nThe squirrel hands you the"
                  " Radius Key. It looks like it would fit in the door to"
                  " the south!")
            radius_key = True
            puzzle_room()

        else:
            print("\"Wrong! Tries remaining:", tries)

        if tries == 0:
            print("\"Took too long, I got bored! Try again!\"")
            puzzle_room()


# This displays when you access the south room after acquiring the radius key.
def exit():
    print("Freedom! You made it to the end of the program!")
    print("Thank you for playing!")
    quit()


def main():
    print("\n>>>Welcome to my Integration project!")
    print("Anything you see in the 'Actions' list you can do by typing the "
          "number next to the action you wish to execute.")
    print("For example: when you're ready, type '1' to Start the game.")
    still_in_loop = True
    while still_in_loop:
        action = input("\nActions:\n1.) Start Game\n\n>Action: ")
        if action == validActions[0]:
            still_in_loop = False
            print("\n|  |  |  |  |  |  G A M E   S T A R T  |  |  |  |  |  |")
            jail_cell()
        else:
            print("Oops! Be sure to enter the number corresponding to the "
                  "action you want to take.\nFor example, typing '1' will "
                  "start the game.")


# Call to main
main()

# HERE ARE THE REST OF THE REQUIREMENTS #

# - means to subtract two numbers. 3 - 2 = 1.

# Month-Date-Year: 1 9 23
# sep='-' yields 1-9-23

# %, or Modulus, finds the remainder. You can use this to see if something is
# even or odd by doing:
# x = int(input("Enter a number, and I'll tell you if it's even or odd: "))
# if x % 2 == 0:
#     print("Even.")
# else:
#     print("Odd.")

# / is simple division
# // is floor division, it rounds down no matter what the tenth's place.
# 10/2.1 = 4.76
# 10//2.1 = 4

# != means 'not equal to'

# 'or': One of the two variables or both of the variables must be true in
# order to return 'True'.

# Shortcut operators, like += and -=, iterate. They add one to itself.
# total += 1 is the same as total = total + 1, the same with a minus.
