import turtle as t

# Quadrat
# farbe = "blue"
# seite = 40
# t.color(farbe)
# for i in range(4):
#     t.forward(seite)
#     t.left(90)
# t.hideturtle()

# Stern
# farbe = "red"
# t.width(5)
# t.color(farbe)
# for blatt in range(10):
#     t.circle(100, 60)
#     t.left(170)
#     t.circle(100, 60)

# Spirale
# t.color("Red")
# for i in range(40):
#     t.forward(15-i/3)
#     t.left(i*2+i/9)
# t.hideturtle()

# Farben wechseln
# farben = ["green", "red", "blue", "light green", "brown", "orange"]
# grossen = [120, 100, 80, 60, 40, 20]
# t.width(3)
# for i in range(6):
#     t.color(farben[i])
#     t.circle(grossen[i])
# t.hideturtle()

# Blume
farbe1 = "black"
farbe2 = "violet"
t.color(farbe1)
t.begin_fill()
for blatt in range(10):
    t.circle(100, 60)
    t.left(100)
    t.circle(100, 60)
t.end_fill()
t.color(farbe2)
t.begin_fill()
t.circle(20)
t.end_fill()
t.hideturtle()