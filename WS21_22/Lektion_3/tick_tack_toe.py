# ein Brett - numpy, damit es schöner aussieht
import numpy as np

board = np.full((3, 3), "_")
print(board)


# Eine weiterführende Idee: der Benutzer definiert die beiden Zeichen (statt X und O)
# Noch eine: wie könnte der Benutzer das Spiel mehrmals spielen? Vielleicht beliebig viel mal?
# Oder: wie könnte man gleichzeitig die Zeile und die Spalte eingeben?


def ist_es_erlaubt(zeile, spalte, board):
    """
    Überprufe ob diese Position überhaupt sinnvoll und noch frei ist.

    :param zeile: Nummer zwischen 0 und 2
    :param spalte: Nummer zwischen 0 und 2
    :param board: Ein 3x3 Numpy array
    :return: True falls Position erlaubt, False falls nicht
    """
    ist_erlaubt = True
    if zeile < 0 or zeile > 2:
        print("Diese Zeile/Spalte ist nicht erlaubt!")
        ist_erlaubt = False
    elif spalte < 0 or spalte > 2:
        print("Diese Zeile/Spalte ist nicht erlaubt!")
        ist_erlaubt = False
    elif board[zeile][spalte] != "_":
        print("Diese Stelle ist schon gefüllt!")
        ist_erlaubt = False
    return ist_erlaubt


def ist_spiel_vorbei(zeichen, board):
    """
    Überprüfe, ob jemand gewonnen hat - mit 3 gleichen zeichen in der Reihe, Spalte oder auf
    einer der beiden Diagonalen.

    :param zeichen: entweder 'X' oder 'O'
    :param board: Ein 3x3 Numpy array
    :return: True falls zeichen gewonnen hat, False sonst.
    """
    spiel_vorbei = False
    for a in range(3):
        # Option 1: die ganze Zeile ist gleich
        if board[a][0] == zeichen and board[a][1] == zeichen and board[a][2] == zeichen:
            spiel_vorbei = True
        # Option 2: die ganze Spalte ist gleich
        if board[0][a] == zeichen and board[1][a] == zeichen and board[2][a] == zeichen:
            spiel_vorbei = True
    # Option 3: eine der Diagonalen ist gleich
    if board[0][0] == zeichen and board[1][1] == zeichen and board[2][2] == zeichen:
        spiel_vorbei = True
    if board[0][2] == zeichen and board[1][1] == zeichen and board[2][0] == zeichen:
        spiel_vorbei = True
    return spiel_vorbei


# spiel spielen - 9 Runden weil die 3x3 Tabelle 9 Platze zur Verfügung hat
for runde in range(9):
    if runde in (0, 2, 4, 6, 8):  # ich versuche % Operator zu vermeiden, kann man auch anders machen
        zeichen = "O"
    else:
        zeichen = "X"
    # spieler spielt
    while True:  # benutze "for versuch in range(100):" oder ähnliches um while-Schleife zu meiden
        zeile = int(input(f"Spieler {zeichen}: wähle die Zeile: "))
        spalte = int(input(f"Spieler {zeichen}: wähle die Spalte: "))
        # ist die Stelle erlaubt?
        if ist_es_erlaubt(zeile, spalte, board):
            break
    board[zeile][spalte] = zeichen
    print(board)
    # ist das Spiel vorbei?
    if ist_spiel_vorbei(zeichen, board):
        if zeichen == "X":
            print("""

██   ██     ██     ██ ██ ███    ██ ███████ ██ 
 ██ ██      ██     ██ ██ ████   ██ ██      ██ 
  ███       ██  █  ██ ██ ██ ██  ██ ███████ ██ 
 ██ ██      ██ ███ ██ ██ ██  ██ ██      ██    
██   ██      ███ ███  ██ ██   ████ ███████ ██ 

    """)
        elif zeichen == "O":
            print("""

 ██████      ██     ██ ██ ███    ██ ███████ ██ 
██    ██     ██     ██ ██ ████   ██ ██      ██ 
██    ██     ██  █  ██ ██ ██ ██  ██ ███████ ██ 
██    ██     ██ ███ ██ ██ ██  ██ ██      ██    
 ██████       ███ ███  ██ ██   ████ ███████ ██                                                       
      """)
        break

print("Das Spiel ist vorbei.")
# weitere coole Texte hier:
# https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=%0A