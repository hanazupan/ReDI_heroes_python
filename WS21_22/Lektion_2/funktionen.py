import turtle


# Optional - Funktionen
def schreibe_H(farbe):
    t = turtle.Turtle()
    t.color(farbe)
    t.left(90)
    t.forward(200)
    t.backward(100)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(100)
    t.backward(200)
    t.hideturtle()


def quadrat(farbe, seite):
    t = turtle.Turtle()
    t.color(farbe)
    for i in range(4):
        t.forward(seite)
        t.left(90)
    t.hideturtle()


def stern(farbe):
    t = turtle.Turtle()
    turtle.bgcolor("Black")
    t.color(farbe)
    for blatt in range(10):
        t.circle(100, extent=60)
        t.left(170)
        t.circle(100, extent=60)


def blume(farbe1, farbe2):
    t = turtle.Turtle()
    t.color(farbe1)
    t.begin_fill()
    for blatt in range(10):
        t.circle(100, extent=60)
        t.left(100)
        t.circle(100, extent=60)
    t.end_fill()
    t.color(farbe2)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.hideturtle()


schreibe_H("Red")
turtle.clearscreen()
quadrat("Blue", 100)
quadrat("Red", 50)
turtle.clearscreen()
stern("Yellow")
turtle.bgcolor("White")
turtle.clearscreen()
blume("Violet", "Yellow")
turtle.done()