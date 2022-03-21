import turtle as t

# Lass uns zusammen einen Regenbogen zeichnen
# zeige das ganze erst auf einer Tafel!
t.width(30)
t.left(90)
# erster Bogen
t.color("red")
t.circle(150, 180)
# Position verändern
t.up()
t.left(90)
t.forward(30)
t.right(90)
t.down()
# zweiter Bogen
t.color("yellow")
t.circle(120, -180)
# Position verändern
t.up()
t.left(90)
t.forward(30)
t.right(90)
t.down()
# dritter Bogen
t.color("light green")
t.circle(90, 180)
# Position verändern
t.up()
t.left(90)
t.forward(30)
t.right(90)
t.down()
# vierter Bogen
t.color("blue")
t.circle(60, -180)

#t.done()