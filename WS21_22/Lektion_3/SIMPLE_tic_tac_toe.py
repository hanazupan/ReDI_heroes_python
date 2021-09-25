# ein Brett - numpy, damit es schöner aussieht
import numpy as np
board = np.full((3, 3), "_")
print(board)

# spiel spielen - 9 Runden weil die 3x3 Tabelle 9 Platze zur Verfügung hat
for runde in range(9):
    if runde in (0, 2, 4, 6, 8):  # ich versuche % Operator zu vermeiden, kann man auch anders machen
        zeichen = "O"
    else:
        zeichen = "X"
    # spieler wählt die Stelle aus
    zeile = int(input(f"Spieler {zeichen}: wähle die Zeile: "))
    spalte = int(input(f"Spieler {zeichen}: wähle die Spalte: "))
    board[zeile][spalte] = zeichen
    print(board)
    # ist das Spiel vorbei?
    spiel_vorbei = False
    for a in range(3):
        # Option 1: die ganze Zeile ist gleich
        if board[a][0] == zeichen and board[a][1] == zeichen and board[a][2] == zeichen:
            print(f"{zeichen} ist der Gewinner!")
            spiel_vorbei = True
        # Option 2: die ganze Spalte ist gleich
        if board[0][a] == zeichen and board[1][a] == zeichen and board[2][a] == zeichen:
            print(f"{zeichen} ist der Gewinner!")
            spiel_vorbei = True
    # Option 3: eine der Diagonalen ist gleich
    if board[0][0] == zeichen and board[1][1] == zeichen and board[2][2] == zeichen:
        print(f"{zeichen} ist der Gewinner!")
        spiel_vorbei = True
    if board[0][2] == zeichen and board[1][1] == zeichen and board[2][0] == zeichen:
        print(f"{zeichen} ist der Gewinner!")
        spiel_vorbei = True
    if spiel_vorbei:
        break

# egal, ob jemand gewinnt oder nicht
print("Das Spiel ist vorbei.")