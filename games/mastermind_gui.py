

from tkinter import *
from tkinter import messagebox
import random



print(" --- MASTERMIND --- \n")
print("Guess the secret color code in as few tries as possible.\n")
print("Please, enter your color code.\nYou can use (R)ed, (G)reen, (B)lue, M(agenta), (C)yan, and (Y)ellow")

colors = ["R", "G", "B", "M", "C", "Y", "R", "G", "B", "M", "C", "Y"]
color_hash = {"R": "red", "G":"green", "B":"blue", "M":"magenta", "C":"cyan", "Y":"yellow"}

attempts = 1
game = True

# computer randomly picks four-color code
color_code = random.sample(colors, 4)
#print(color_code)



root = Tk()


main_frame = Frame(root)
main_frame.pack()


guess_frames = []
guess_pins = []
result_pins = []

for i in range(13):
    frame = Frame(main_frame, width=300, height=40, relief="raised", borderwidth=5, bg="brown", highlightthickness=3)
    frame_pins = []
    frame_results = []

    c1 = Canvas(frame, width=40, height=40)
    c1.create_oval(5, 5, 35, 35,
                       fill="gray", width=2)
    c1.grid(row = 0, column = 0, sticky = "nsew")
    frame_pins.append(c1)

    c2 = Canvas(frame, width=40, height=40)
    c2.create_oval(5, 5, 35, 35,
                       fill="gray", width=2)
    c2.grid(row=0, column=1, sticky="nsew")
    frame_pins.append(c2)

    c3 = Canvas(frame, width=40, height=40)
    c3.create_oval(5, 5, 35, 35,
                       fill="gray", width=2)
    c3.grid(row=0, column=2, sticky="nsew")
    frame_pins.append(c3)

    c4 = Canvas(frame, width=40, height=40)
    c4.create_oval(5, 5, 35, 35,
                       fill="gray", width=2)
    c4.grid(row=0, column=3, sticky="nsew")
    frame_pins.append(c4)

    c5 = Canvas(frame, width=40, height=40, bg="yellow")
    r1 = c5.create_oval(5, 5, 15, 15, fill="gray", width=2) #top left
    r2 = c5.create_oval(5, 25, 15, 35, fill="gray", width=2) #bottom left
    r3 = c5.create_oval(25, 5, 35, 15, fill="gray", width=2) #top left
    r4 = c5.create_oval(25, 25, 35, 35, fill="gray", width=2) #bottom left
    frame_pins.append(c5)

    frame_results.append(r1)
    frame_results.append(r2)
    frame_results.append(r3)
    frame_results.append(r4)

    c5.grid(row=0, column=4, sticky="nsew")


    frame.config(highlightbackground="gray")
    frame.grid(row = i, column = 0, sticky = "nsew")

    result_pins.append(frame_results)
    guess_pins.append(frame_pins)
    guess_frames.append(frame)


bottom_frame = Frame(main_frame)

text_label = Label(bottom_frame, width=5, text="Tahmin")
text_entry = Entry(bottom_frame, width=10, bg="cyan")

def checkInput():
    player_guess = text_entry.get()
    player_guess = player_guess.upper()

    global attempts;
    print("Number of attemtps is" + str(attempts))
    print("Player guess is : " + player_guess)

    # checking if player's input is correct
    if len(player_guess) != len(color_code):
        print("\nError! Only 4 characters allowed")
        messagebox.showwarning("Mastermind", "Only 4 characters allowed")
        return False
    for i in range(4):
        if player_guess[i] not in colors:
            print("\nError! Only letters (R)ed, (G)reen, (B)lue, (M)agenta, (C)yan, and (Y)ellow allowed ")
            messagebox.showwarning("Mastermind", "Only letters;\n(R)ed\n(G)reen\n(B)lue\n(M)agenta\n(C)yan\n(Y)ellow allowed ")
            wrong_char = True
            return False

    correct_color = ""
    guessed_color = ""

    black_colors = 0
    white_colors = 0
    # comparison between player's input and secret code
    for i in range(4):
        if player_guess[i] == color_code[i]:
            black_colors += 1

        if player_guess[i] != color_code[i] and player_guess[i] in color_code:
            white_colors += 1

        guess_pins[attempts-1][i].create_oval(5, 5, 35, 35,
                       fill=color_hash[player_guess[i]], width=2)

    #fill in the circles for pins and results
    result_index = 0
    for i in range(white_colors):
        guess_pins[attempts - 1][4].itemconfig(result_pins[attempts-1][result_index], fill='white')
        result_index += 1

    for i in range(black_colors):
        guess_pins[attempts - 1][4].itemconfig(result_pins[attempts-1][result_index], fill='black')
        result_index += 1

    correct_color += "s: " + str(black_colors) + " "
    guessed_color += "b: " + str(white_colors) + " "
    print(correct_color + guessed_color + "\n")


    if black_colors == 4:
        if attempts == 1:
            print("Wow! You guessed at the first attempt!")
            messagebox.showinfo("Mastermind", "Wow!\nYou guessed at the first attempt!")
        else:
            print("You win... You used " + str(attempts) + " attempts to guess.")
            messagebox.showinfo("Mastermind", "You win...\nYou used " + str(attempts) + " attempts to guess.")
        exit(0)
    else:
        if attempts >= 13:
            print("You didn't guess! The secret color code was: " + str(color_code))
            messagebox.showinfo("Mastermind", "You couldn't guess!\nThe secret color code was: " + str(color_code))
            exit(0)

    attempts += 1
    return True


button = Button(bottom_frame, text="Gönder", width=10, command=checkInput)

text_label.grid(row = 0, column = 0, sticky = "nsew")
text_entry.grid(row = 0, column = 1, sticky = "nsew")
button.grid(row = 0, column = 2, sticky = "nsew")

bottom_frame.grid(row = 13, column = 0, sticky = "nsew")

root.geometry("300x900+600+200")
root.title("Mastermind")

root.mainloop()