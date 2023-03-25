# Ethan Weiss

# I decided to reformat my original CYOA game into more of a dungeon-crawler.
# The player will be presented with a series of rooms they can walk in and out.
# In one of the rooms will be a shop, where they will buy a key and health pot
# if they want to progress further. Another room will have a puzzle that makes
# you find the radius of a circle.
# Eventually they will escape the dungeon, and that will be the end of it.

# Inspiration comes from www.makeuseof.com/python-text-adventure-game-create/
# I'll try and keep most of the code unique, but the general framework will
# be pretty similar - using def() functions to move between rooms.

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
import random

# I will use this for navigation. I will exclude invalid inputs if it does not
# align with the map of the dungeon I have created.
validDirections = ['north', 'south', 'east', 'west', 'up', 'down']
#                    0        1        2       3      4       5

# Global Variables. These are going to be keys. These will change to True once
# the user solves a puzzle or interacts with something.

jail_key = False
jail_door_unlocked = False
radius_key = False


# There are two options for the jail cell - Either they have obtained the key
# by searching the bed, or they haven't. They cannot go south if they have not
# obtained the jail key.

def jail_cell():
    print("\n>>>You are in the jail cell.")
    global jail_door_unlocked

    if jail_door_unlocked:
        print("You can go (south) from here.")
        still_in_loop = True
        while still_in_loop:
            action = input("\nAction: ")
            if action == validDirections[1]:
                still_in_loop = False
                center_room()
            else:
                print("Invalid option.")

    else:
        print("There is a (bed) in the corner, and a (locked door) on the "
              "south wall.")
        global jail_key

        still_in_loop = True
        while still_in_loop:
            action = input("\nAction: ")
            if action == 'bed':
                print("You search for and find the jail key.")
                jail_key = True
            elif action == 'locked door':
                if jail_key:
                    print("You unlock the locked door, and continue on into "
                          "the next room.\nCongratulations! You know how to "
                          "open a door.")
                    jail_door_unlocked = True
                    still_in_loop = False
                    center_room()
                elif not jail_key:
                    print("Wow! That door sure looks locked to me. Good thing "
                          "there's a keyhole! Now, where to find the key..")
            else:
                print("Oops! Remember, only the words in parentheses () "
                      "can be typed.")


# This is the center room, between the jail cell and store room.
def center_room():
    print("\n>>>You are in the center room.")
    print("You can go (north), (south), or (east) from here.")
    still_in_loop = True
    while still_in_loop:
        action = input("\nAction: ")
        if action == validDirections[0]:
            still_in_loop = False
            jail_cell()
        elif action == validDirections[1]:
            still_in_loop = False
            store_room()
        elif action == validDirections[2]:
            still_in_loop = False
            puzzle_room()
        else:
            print("Invalid option.")


# Here is the store room. Inside of it is a shop.
def store_room():
    still_in_loop = True
    print("\n>>>You are in the Store Room.")
    print("You can go (north) from here.\nHere, you can see a (shop).")
    while still_in_loop:
        action = input("Action: ")
        if action == validDirections[0]:
            still_in_loop = False
            center_room()
        elif action == 'shop':
            still_in_loop = False
            shop()
        else:
            print("Invalid option.")


def shop():
    print("You enter the shop. It more closely resembles a bar than a shop."
          " There is a menu on the table. It reads:\n")
    print("(1).   Bread  - $0.50 per loaf")
    print("(2).   Wine   - $3.00 per bottle")
    print("(3).   Cookie - $1.25 each\n\nAnything strike your fancy? When "
          "you're done, you may (back) away from the counter.")

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

        if action == '1':
            invalid_number = True
            while invalid_number:
                try:
                    bread = abs(int(input("How many loaves of bread? ")))
                except ValueError:
                    print("- Unfortunately, you have to buy "
                          "the loaves in full.")
                else:
                    invalid_number = False
            print()

        elif action == '2':
            invalid_number = True
            while invalid_number:
                try:
                    wine = abs(int(input("How many bottles of wine? ")))
                except ValueError:
                    print(
                        "- Unfortunately, you have to buy the bottles in "
                        "full.")
                else:
                    invalid_number = False
            print()

        elif action == '3':
            invalid_number = True
            while invalid_number:
                try:
                    cookie = abs(int(input("How many cookies? ")))
                except ValueError:
                    print(
                        "- Unfortunately, you have to buy the cookies in "
                        "full. Why wouldn't you buy a full cookie?!")
                else:
                    invalid_number = False
            print()

        # When the user is done and types 'back', a small message appears that
        # calculates what would be the total of these items all added together.
        # If the total is 0, there is no message besides 'Ehh, never-mind.' If
        # the total is greater than 0, it prints the calculated message,
        # breaks the loop, and returns to the store room that the shop is in.
        elif action == 'back':
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
            print("Sorry, we don't have those here! (Please enter a number, or"
                  " 'back' if you're done.)")


def main():
    print("\n>>>Welcome to my Integration project!")
    print("Anything you see in parentheses, you can do.")
    print("For example: when you're ready, press (start).")
    still_in_loop = True
    while still_in_loop:
        action = input("\nAction: ")
        if action == 'start':
            still_in_loop = False
            print("\n|  |  |  |  |  |  G A M E   S T A R T  |  |  |  |  |  |")
            jail_cell()
        else:
            print("Not ready? All good! Relax, and (start) when you're ready.")


def puzzle_room():
    print("\n>>>You are in the Puzzle room.")
    print("You can go (west) from here.")
    print("On the northern (wall), there is a small hole in the wall.")
    print("You also see a (squirrel) here.")

    still_in_loop = True
    while still_in_loop:
        action = input("\nAction: ")
        if action == validDirections[3]:
            still_in_loop = False
            center_room()

        elif action == validDirections[1]:
            exit()

        elif action == 'wall':
            print("You find a note! On it reads the following:\n")
            print("Area = Pi * Radius squared!\nDiameter = 2 * Radius!\n")
            print("Ugh, Pi?! I hate math!")

        # I'm probably just going to make this elif into its own separate
        # 'squirrel_dialogue()', but I feel like that would make it even more
        # of a mess than it already is.
        elif action == 'squirrel':
            if not radius_key:
                print("\"" + "Hey, " * 3, "Human!\", says the squirrel.")
                print("\"I've got a question for ya! Get it right in under "
                      "three tries and I'll give you this sick key! "
                      "Whaddya say?\"\n")
                squirrelanswer = input("How do you respond?\nType (yes) to "
                                       "take him up on his challenge, or "
                                       "anything else to deny him: ")
                if squirrelanswer == 'yes':
                    still_in_loop = False
                    squirrelgame()
                else:
                    print("\"Fiiine..\", he says. \"But I've got a shiny key, "
                          "and you dont!\"")
            else:
                print("\"I already gave you your key! scram!\"")
        else:
            print("Invalid option.")


# I want to give the player the Radius Key if they get the answers right,
# but I'm at a loss at how to do this. I'm just going to submit what I have
# and hope to amend my grade later on.

def squirrelgame():
    radius = random.randint(1, 5)

    # Here, the random number is running through a calculation and assigned a
    # value that the player has to match.
    def calculate_diameter(radius_info):
        diameter = 2 * radius_info
        return diameter

    for tries in range(2, -1, -1):

        answer = int(input("\"If the radius is " + str(radius) +
                           ", what is the diameter of a circle?\"\n"))

        # Here is where I'd reward the player with the radius key.
        if answer == calculate_diameter(radius):
            print("\"Correct! Here's your prize!\"")
            puzzle_room()
            break

        else:
            print("\"Wrong! Tries remaining:", tries)

        if tries == 0:
            print("\"Took too long, I got bored! Try again!\"")
            puzzle_room()


def exit():
    print("You made it to the end of the program!")
    print("There's still a lot more I want to add, but for now this is it.")
    print("Thank you for playing!")


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

# 'and' is self explanatory, used in logical 'if' or 'while' statements.
# if A and B, then C. Both must be 'true'.

# 'or': One, or the other, or both must be true.

# Shortcut operators, like += and -=, iterate. They add one to itself.
# total += 1 is the same as total = total + 1, the same with a minus.

