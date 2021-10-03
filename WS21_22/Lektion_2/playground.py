import turtle
turtle.bgcolor("Black")
turtle.color("Green")
turtle.speed(10)
turtle.forward(100)
turtle.right(90)
turtle.backward(70)
turtle.left(30)
turtle.begin_fill()
turtle.circle(50, extent=180)
turtle.end_fill()
turtle.penup()
turtle.goto(20, 30)
turtle.pendown()
turtle.forward(100)
turtle.hideturtle()
turtle.clearscreen()

turtle.color("Blue")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.clearscreen()

turtle.color("Blue")
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.clearscreen()

def quadrat(farbe, lange):
    turtle.color(farbe)
    for i in range(4):
        turtle.forward(lange)
        turtle.left(90)

quadrat("Green", 30)
quadrat("Red", 50)
quadrat("Blue", 100)

turtle.done()

benutzer_name = input("Guten Morgen! Wie heißt du? ")
schwestern = int(input("Wie wiele Schwestern hast du? "))
brueder = int(input("Wie wiele Brüder hast du? "))
print(f"{benutzer_name} hat insgesamt {schwestern+brueder} Geschwister.")

temperatur = int(input("Wie viel Grad ist es heute? "))
if temperatur > 25:
    print("Iss unbedingt ein Eis.")
elif temperatur < 5:
    print("Bestelle eine heiße Schokolade.")
else:
    print("Trink am besten frischen Orangensaft.")