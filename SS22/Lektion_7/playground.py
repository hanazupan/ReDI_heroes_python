# numpy
import numpy as np
print(np.random.random())
print(np.random.randint(5, 10))
print(np.random.choice(['Katze', 'Hund']))
print(np.full((3, 3), 'X'))
board = np.zeros((8, 8))
print(board)
board[0][2] = 3
print(board)

# if-Sätze
regen_wahrsch = 0.9
if regen_wahrsch < 0.1:
    print("Heute kein Regen!")
elif 0.1 <= regen_wahrsch < 0.4:
    print("Regen ist unwahrscheinlich.")
elif 0.4 <= regen_wahrsch < 0.8:
    print("Regen ist ziemlich wahrscheinlich.")
else:
    print("Nimm Regenschirm mit! Es wird definitiv regnen!")

my_number = 3
if my_number <= 3:
    print("3 ist kleiner gleich 3")
if 5 > 7:
    print("5 ist größer als 7")
username = "Peter"
if username != 'Hana':
    print(f"username ist {username} und nicht Hana")
geld = -3
if geld == 0:
    print("Kein Geld!")
stop_game = True
if stop_game:
    print("Spiel ist vorbei.")

# Input und Drucken
name = input("Was ist dein Name? ")
alter = int(input("Wie alt bist du? "))
print(f"Mein Name ist {name}.")

# Schleifen
for x in range(9):
    print(x)
for reihe in range(-2, 8, 2):
    print(reihe)
for variable in range(100, 95, -1):
    print(variable)

while True:
    passwort = input("Bitte schreiben Sie Ihr Passwort: ")
    if len(passwort) < 5:
        print("Das Passwort muss mindestens 5 Zeichen haben!")
    else:
        break

# Funktionen


def print_dreimal_hallo():
    print("Hallo!")
    print("Hallo zum zweiten mal!")
    print("Hallo zum dritten mal!")


print_dreimal_hallo()


def ist_durch_2_teilbar(nummer):
    """
    Überpruft, ob die angegebene Nummer durch 2 teilbar ist.
    """
    if nummer%2 == 0:
        return True
    else:
        return False


print(f"Ist 17 durch 2 teilbar? {ist_durch_2_teilbar(17)}")