import turtle

# lass den Benutzer wählen, welche Farbe gut aussieht!
farbe = input("Welche farbe? ")
turtle.color(farbe)
for i in range(40):
    turtle.forward(15-i/3)
    turtle.left(i*2+i/9)
turtle.hideturtle()

#turtle.clearscreen()

# einfache if-Sätze: eine Entscheidung treffen
kosten = int(input("Wie viel kosten die Ferien? "))
freunde = int(input("Wie viele Menschen werden teilnehmen? "))
deine_kosten = kosten/freunde
#print(f"Du müsstest im diesen Fall {round(deine_kosten)}€ bezahlen.")
print("Du muesstest im diesen Fall " + str(round(deine_kosten)) + " Euro bezahlen.")
if deine_kosten > 100:
    print("Das kannst du dich leider nicht leisten.")
else:
    print("Das geht!")

# if-Sätze mit turtle
for schritt in range(10):
    turtle.forward(50)
    richtung = input("In welche Richtung willst du abbiegen? (l/r) ")
    if richtung == "r":
        turtle.right(90)
    else:
        turtle.left(90)

turtle.done()
