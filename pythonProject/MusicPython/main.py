from processing import *


def drawNote(note):
    if note == "C":
        line(20, 140, 60, 140)
        ellipse(40, 140, 20, 20)
    elif note == "D":
        ellipse(40, 130, 20, 20)
    elif note == "E":
        ellipse(40, 120, 20, 20)
    elif note == "F":
        ellipse(40, 110, 20, 20)
    elif note == "G":
        ellipse(40, 100, 20, 20)
    elif note == "A":
        ellipse(40, 90, 20, 20)
    elif note == "B":
        ellipse(40, 80, 20, 20)
    else:
        print("This note was not recognised. Try again by typing a note between A to G.")


def setup():
    strokeWeight(12)
    size(200, 200)
    background(250, 250, 250)
    fill(0, 0, 0)
    # Draw the 5 lines for the staff
    stroke(0, 0, 0)
    line(0, 40, 300, 40)
    line(0, 60, 300, 60)
    line(0, 80, 300, 80)
    line(0, 100, 300, 100)
    line(0, 120, 300, 120)

    note = input("Type a music note (A to G)?").upper()
    drawNote(note)


run()





