# ein Brett - numpy, damit es schöner aussieht
import numpy as np
board = np.zeros((8, 8))
print(board)
# einzige Zahlen ändern
print("----- ein paar Zahlen ändern -----")
board[0][5] = 5
board[6][2] = 3
print(board)
# die ganz einfachen for-Schleifen
print("----- die ganze zweite Zeile ändern -----")
for spalte in range(8):
    board[1][spalte] = 5
print(board)
print("----- die ganze vierte Spalte ändern -----")
for zeile in range(8):
    board[zeile][3] = 7
print(board)
# alles löschen um besser zu sehen
board = np.zeros((8, 8))
# Schleifen mit start und stop
print("----- die zweite Spalte in Zeilen 2-5 ändern -----")
for zeile in range(2, 6):
    board[zeile][1] = 4
print(board)
print("----- die erste Zeile in Reihen 1-3 ändern -----")
for y in range(0, 3):
    board[0][y] = 2
print(board)
# Schleifen mit start, stop und step
print("----- jede zweite überspringen -----")
for ort in range(0, 8, 2):
    board[7][ort] = 9
print(board)
# die Variable benutzen
print("----- nicht immer diesselbe Zahl -----")
for zahl in range(8):
    board[1][zahl] = zahl
print(board)
print("----- starten wir lieber mit 1 -----")
for zahl in range(8):
    board[1][zahl] = zahl + 1
print(board)
# rückwärts gehen
print("----- wir können auch rückwärts gehen -----")
for zahl in range(8):
    board[2][zahl] = 8 - zahl
print(board)
# alles löschen um besser zu sehen
board = np.zeros((8, 8))
print("----- die Diagonale ändern -----")
for a in range(8):
    board[a][a] = 1
print(board)
# doppelt-Schleifen
print("----- alles zugleich ändern -----")
for x in range(8):
    for y in range(8):
        board[x][y] = 8
print(board)
print("----- ein kleineres Rechteck -----")
for x in range(4, 7):
    for y in range(2, 6):
        board[x][y] = 1
print(board)
print("----- Multiplikationstabelle -----")
for x in range(8):
    for y in range(8):
        board[x][y] = (x+1)*(y+1)
print(board)

# weiterführende Ideen, z.B. für Hackaton:
# einfache Brettspiele z.B. "vier in einer Reihe",
# oder "Schiffe versenken"
