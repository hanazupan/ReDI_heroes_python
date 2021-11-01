import turtle


# Optional - Funktionen
def schreibe_H(farbe):
    turtle.color(farbe)
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(200)
    turtle.hideturtle()


def quadrat(farbe, seite):
    turtle.color(farbe)
    for i in range(4):
        turtle.forward(seite)
        turtle.left(90)
    turtle.hideturtle()


def stern(farbe):
    #turtle.bgcolor("Black")
    turtle.color(farbe)
    for blatt in range(10):
        turtle.circle(100, extent=60)
        turtle.left(170)
        turtle.circle(100, extent=60)


def blume(farbe1, farbe2):
    turtle.color(farbe1)
    turtle.begin_fill()
    for blatt in range(10):
        turtle.circle(100, extent=60)
        turtle.left(100)
        turtle.circle(100, extent=60)
    turtle.end_fill()
    turtle.color(farbe2)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.hideturtle()


schreibe_H("Red")
#turtle.clearscreen()
turtle.clear()
quadrat("Blue", 100)
quadrat("Red", 50)
#turtle.clearscreen()
turtle.clear()
stern("Yellow")
#turtle.bgcolor("White")
#turtle.clearscreen()
turtle.clear()
blume("Violet", "Yellow")
turtle.done()
