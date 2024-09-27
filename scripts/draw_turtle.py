import turtle
import re

if __name__ == "__main__":
    f = open("turtle", "r")
    t = turtle.Turtle()
    t.speed(100)
    t.left(90)

    for line in f:
        num = 0
        tab = re.findall(r'\d+', line)
        if tab:
            num = int(tab[0])
        if "Avance" in line:
            t.forward(num)
        elif "Recule" in line:
            t.back(num)
        elif "Tourne droite" in line:
            t.right(num)
        elif "Tourne gauche" in line:
            t.left(num)
    turtle.done()