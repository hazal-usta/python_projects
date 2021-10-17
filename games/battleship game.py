

from random import randint
import os


# Ship Class
class Ship:
    def __init__(self, size, orientation, location, name):
        self.size = size
        self.name = name

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'horizontal' or 'vertical'.")

        if orientation == 'horizontal':
            if location['row'] in range(row_size):
                self.coordinates = []
                for index in range(size):
                    if location['col'] + index in range(col_size):
                        self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
                    else:
                        raise IndexError("Column is out of range.")
            else:
                raise IndexError("Row is out of range.")
        elif orientation == 'vertical':
            if location['col'] in range(col_size):
                self.coordinates = []
                for index in range(size):
                    if location['row'] + index in range(row_size):
                        self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                    else:
                        raise IndexError("Row is out of range.")
            else:
                raise IndexError("Column is out of range.")

        if self.filled():
            print_board(board)
            print(" ".join(str(coords) for coords in self.coordinates))
            raise IndexError("A ship already occupies that space.")
        else:
            self.fillBoard()

    def filled(self):
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
                return True
        return False

    def fillBoard(self):
        for coords in self.coordinates:
            board[coords['row']][coords['col']] = 1

    def contains(self, location):

        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    def damaged(self):
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == '*':
                return True
            elif board_display[coords['row']][coords['col']] == 'X':
                raise RuntimeError("Board display inaccurate")
        return False


    def destroyed(self):
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == 'O':
                return False
            elif board_display[coords['row']][coords['col']] == 'X':
                raise RuntimeError("Board display inaccurate")
        return True

    def print_report(self):
        output = "1 adet " + self.name + " (" + str(self.size) + " kareyi kaplar) "

        status = "["
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == '*':
                status += " +"
            else:
                status += " -"

        status += "]"
        output += status
        if self.destroyed():
            output += " Battı."
        elif self.damaged():
            output += " Yaralı."

        print(output)


col_names = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J"]
# Settings Variables
board_size = 10
row_size = board_size  # number of rows
col_size = board_size  # number of columns
num_ships = 5
num_turns = 40

ascii_value = ord('A')

# Create lists
ship_list = []

board = [[0] * col_size for x in range(row_size)]

board_display = [["O"] * col_size for x in range(row_size)]


# Functions
def print_board(board_array):
    print("\n   " + " ".join(str(col_names[x-1]) for x in range(1, col_size + 1)))
    for r in range(row_size):
        if r != row_size-1:
            print(str(r + 1) + "  " + " ".join(str(c) for c in board_array[r]))
        else:
            print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))


def search_locations(size, orientation):
    locations = []

    if orientation != 'horizontal' and orientation != 'vertical':
        raise ValueError("Orientation must have a value of either 'horizontal' or 'vertical'.")

    if orientation == 'horizontal':
        if size <= col_size:
            for r in range(row_size):
                for c in range(col_size - size + 1):
                    if 1 not in board[r][c:c + size]:
                        locations.append({'row': r, 'col': c})
    elif orientation == 'vertical':
        if size <= row_size:
            for c in range(col_size):
                for r in range(row_size - size + 1):
                    if 1 not in [board[i][c] for i in range(r, r + size)]:
                        locations.append({'row': r, 'col': c})

    if not locations:
        return 'None'
    else:
        return locations


def random_location(shipsize):
    orientation = 'horizontal' if randint(0, 1) == 0 else 'vertical'

    locations = search_locations(shipsize, orientation)
    if locations == 'None':
        return 'None'
    else:
        return {'location': locations[randint(0, len(locations) - 1)], 'size': shipsize, \
                'orientation': orientation}


def get_row():
    while True:
        try:
            guess = int(input("Row Guess: "))

            if guess in range(1, row_size + 1):
                return guess - 1
            else:
                print("\nOops, that's not even in the ocean.")
        except ValueError:
            print("\nPlease enter a number")


def get_col():
    while True:
        try:
            guess = int(input("Column Guess: "))
            if guess in range(1, col_size + 1):
                return guess - 1
            else:
                print("\nOops, that's not even in the ocean.")
        except ValueError:
            print("\nPlease enter a number")

def get_guess(turn):
    while True:
        try:
            guess = input(str (turn+1) + ". tahmininizi giriniz? ")
            col_guess = guess[-1]
            row_index = int(guess[:-1])-1
            col_index = ord (col_guess) - ascii_value

            #print("Col tahmin " + str(col_index))
            #print("Row tahmin " + str(row_index))

            if row_index not in range(0, row_size) or col_index not in range(0,col_size):
                print("Hata: sayılar 1 ile 10, harfler de A ile J arasında olmalıdır. Tekrar giriniz.")
            else:
                return {"row": row_index, "col":col_index, "orj":guess}
        except ValueError:
            print("\nPlease enter a number")

def get_current_status(turn):
    print(str(turn) + " atış denemesi yaptınız.")

    for ship in ship_list:
        ship.print_report()


# Create the ships
ship_names = ["Mayın gemisi", "Denizaltı", "Firkateyn", "Muhrip gemisi", "Amiral Kruvazör gemisi"]

temp = 0
while temp < num_ships:
    ship_info = random_location(temp+1)
    if ship_info == 'None':
        continue
    else:
        ship_list.append(Ship(ship_info['size'], ship_info['orientation'], ship_info['location'], ship_names[temp]))
        temp += 1
del temp

# Play Game
print("Amiral Battı oynayalım!")
print_board(board_display)

turn = 0
program_input = ""

while True:
    print()

    guess_coords = {}
    while True:
        guess_coords = get_guess(turn)
        if board_display[guess_coords['row']][guess_coords['col']] == 'X' or \
                        board_display[guess_coords['row']][guess_coords['col']] == '*':
            print("\n[+"+ guess_coords['orj'] +"] Bu koordinata daha önce atış yapıldı. Tekrar atış yapınız.")
            turn += 1
        else:
            break

    turn += 1
    ship_hit = False
    guess_location = {}
    guess_location["row"] = guess_coords['row']
    guess_location["col"] = guess_coords['col']

    for ship in ship_list:
        if ship.contains(guess_location):
            ship_hit = True
            board_display[guess_coords['row']][guess_coords['col']] = '*'
            if ship.destroyed():
                print(ship.name + " battı.")
                ship_list.remove(ship)
            else:
                print("\n[" + guess_coords['orj'] + "] " + ship.name + " yara aldı.")
            break
    if not ship_hit:
        board_display[guess_coords['row']][guess_coords['col']] = 'X'
        print("\n[" + guess_coords['orj'] + "] Iska")

    program_input = input("Durum raporu icin (r), oyundan çıkmak için (q) giriniz.")
    if program_input == "q":
        break
    elif program_input == "r":
        get_current_status(turn)

    print_board(board_display)

    if not ship_list:
        break

# End Game
if ship_list:
    print("Kaybettiniz!")
else:
    print("Tüm gemileri batırdınız. Kazandınız, tebrikler!")