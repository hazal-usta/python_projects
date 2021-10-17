# --- MASTERMIND --- #
# @author: Hazal Usta

import random

print(" --- MASTERMIND --- \n")
print("Guess the secret color code in as few tries as possible.\n")
print("Please, enter your color code.\nYou can use (R)ed, (G)reen, (B)lue, M(agenta), (C)yan, and (Y)ellow")

colors = ["R", "G", "B", "M", "C", "Y", "R", "G", "B", "M", "C", "Y"]
attempts = 0
game = True

# computer randomly picks four-color code
color_code = random.sample(colors, 4)
#print(color_code)

# player guesses the number
while game:
    correct_color = ""
    guessed_color = ""
    attempts += 1
    player_guess = input("Mastermind " + str(attempts) + " ->").upper()

    # checking if player's input is correct
    wrong_char = False
    if len(player_guess) != len(color_code):
        print("\nError! Only 4 characters allowed")
        attempts += -1
        continue
    for i in range(4):
        if player_guess[i] not in colors:
            print("\nError! Only letters (R)ed, (G)reen, (B)lue, M(agenta), (C)yan, and (Y)ellow allowed ")
            wrong_char = True
            break

    if wrong_char:
        attempts += -1
        continue

    black_colors = 0
    white_colors = 0
    # comparison between player's input and secret code
    for i in range(4):
        if player_guess[i] == color_code[i]:
            black_colors += 1

        if player_guess[i] != color_code[i] and player_guess[i] in color_code:
            white_colors += 1

    correct_color += "s: " + str(black_colors) + " "
    guessed_color += "b: " + str(white_colors) + " "
    print(correct_color + guessed_color + "\n")

    if black_colors == 4:
        if attempts == 1:
            print("Wow! You guessed at the first attempt!")
        else:
            print("You win... You used " + str(attempts) + " attempts to guess.")
        game = False
    else:
        if attempts >= 13:
            print("You didn't guess! The secret color code was: " + str(color_code))
            break

