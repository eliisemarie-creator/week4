from colorama import Fore
# TASK: Favourite Color Personality Test
#
# Create a simple program that asks the user for their favourite color.
#
# Requirements:
# 1. Ask the user to enter their favourite color.
# 2. Convert the input to lowercase.
# 3. For each color provided by the user, print a short personality description.
#
# Example:
# red   ->  "You are energetic and confident."
# blue  ->  "You are calm and thoughtful."
# green ->  "You are balanced and patient."
# yellow -> "You are optimistic and creative."
# any other option -> "You are a magic unicorn."

#elif

""" color = input("What is your favourite color? ").lower()

if color == "red":
    print("You are energetic and confident.")
elif color == "blue":
    print("You are calm and thoughtful.")
elif color == "green":
    print("You are balanced and patient.")
elif color == "yellow":
    print("You are optimistic and creative.")
else:
    print("You are a magical unicorn.") """

color = input("What is your favourite color? ").lower()

match color:
    case "red":
        print(Fore.RED + "You are energetic and confident.")
    case "blue":
        print(Fore.BLUE + "You are calm and thoughtful.")
    case "green":
        print(Fore.GREEN + "You are balanced and patient.")
    case "yellow":
        print(Fore.YELLOW + "You are optimistic and creative.")
    case _:
        print(Fore.CYAN + "You are a magical unicorn.")