import turtle

# Wiederholung - for-Schleifen
turtle.color("Red")
for i in range(40):
    turtle.forward(15-i/3)
    turtle.left(i*2+i/9)
turtle.hideturtle()

#turtle.clearscreen()
turtle.clear()

# Noch komplizierter
#turtle.color('red', 'yellow')
turtle.color('red')
#turtle.begin_fill()
for runde in range(50):
    turtle.forward(200)
    turtle.left(170)
#turtle.end_fill()

#turtle.clearscreen()
turtle.clear()


# Wiederholung - Listen
farben = ["Green", "Blue", "Red", "Black", "Yellow", "Pink", "Orange", "Violet"]

for zahl in range(len(farben)):
    turtle.color(farben[zahl])
    turtle.circle(10*zahl)

turtle.done()
