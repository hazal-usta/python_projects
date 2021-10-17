
#@author: Hazal Usta

from numpy import*
from tkinter import*
import turtle
import random
import codecs

# Create turtle object
t = turtle.Turtle()

# Create a screen
screen = turtle.Screen()
screen.setup(800,800)
screen.bgpic('snowmanTree.gif')
screen.update()


# Function to draw body of snowman
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto (x, y)
    t.pendown()
    t.fillcolor(color)

    t.begin_fill()
    t.circle (radius)
    t.end_fill()
    t.penup()

def draw_left_eye():
    draw_circle("black", 10, 30, -10)

def draw_right_eye():
    draw_circle("black", 10, 80, -10)

def draw_nose():
    draw_circle("#FF6600", 14, 55, -40)

def draw_buttons():
    t.pensize(1)
    t.pencolor("black")
    draw_circle("black", 7, 57, -120)
    draw_circle("black", 7, 57, -150)
    draw_circle("black", 7, 57, -180)

def draw_mouth():
    t.penup()
    t.goto(32, -45)
    t.pencolor("red")
    t.pensize(5)
    t.down()
    t.right(90)
    t.circle(23, 180)
    t.up()

def create_line(x, y, length, angle):
    t.penup()
    t.goto(x, y)
    t.pencolor("brown")
    t.pensize(5)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.setheading(angle + 20)
    t.forward(20)
    t.penup()
    t.back(20)
    t.pendown()
    t.setheading(angle - 20)
    t.forward(20)
    t.penup()
    #t.home()

def draw_left_arm():
    create_line(-5, -120, 100, 160)

def draw_right_arm():
    create_line(110, -120, 100, 20)

def draw_hat():
    t.penup()
    t.goto(-35, 8)
    t.color("black")
    t.pensize(6)
    t.pendown()
    t.goto(35, 8)

    t.goto(30, 8)
    t.fillcolor("black")
    t.begin_fill()
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(15)
    t.end_fill()

print("Kardan adam oyunu basladi!")

content = []
with codecs.open('cities.txt', encoding='utf-8') as f:
    for line in f:
        content.append(line)
# you may also want to remove whitespace characters like `\n` at the end of each line
words = [x.strip() for x in content]
#print(words)

# Function will choose one random
# word from this list of words
word = random.choice(words).lower()
#print(word)

print(str(len(word)) + " harfli bir sehir ismi? ")

guesses = set()

# any number of turns can be used here
turns = 0
win = False

t.hideturtle()


drawings = [draw_left_eye, draw_right_eye, draw_nose, draw_mouth, draw_left_arm, draw_right_arm, draw_buttons]

while turns < 7:

    # counts the number of times a user fails
    # all characters from the input
    # word taking one at a time.
    correct_chars = 0

    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end =" ")
            correct_chars += 1
        else:
            print("_", end =" ")

    print("\n")
    if correct_chars == len(word):
        print("...Bildiniz...")
        win = True
        break

    while True:
        harf = input("Bir harf tahmin ediniz: ")

        if harf in guesses:
            print("Bu harfi önceden girdiniz, yeniden deneyin.")
        else:
            if harf not in word:
                print("Maalesef " + harf + " harfinden hic yok.")
                drawings[turns]()
                turns += 1
            guesses.add(harf)
            break

if not win:
    print("Oyun bitti bilemediniz, dogru kelime: " + word)
turtle.Screen().exitonclick()


