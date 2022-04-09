# ############## Verschiedene Typen von Variablen
eine_zahl = -15
print(type(eine_zahl))
auch_eine_zahl = 12.34
print(type(auch_eine_zahl))
keine_zahl = "Hallo ihr alle!"
print(type(keine_zahl))
eine_liste = ["Ich", "bin", "ein", "Berliner"]
print(type(eine_liste))
beliebig_gemischt = [1, 77, "hallo", 45.20973, "Wie heißt du?"]
print(type(beliebig_gemischt))

# ############## Operationen auf Listen
# len()
die_laenge = len(eine_liste)
print(f"Die liste ist {eine_liste}.")
print(f"Die Liste hat {die_laenge} Elementen.")
# "".join()
print(" ".join(eine_liste))
print("-".join(eine_liste))
#print(" ".join(beliebig_gemischt))   # das geht nicht
# Index
print(f"Der erste Element ist {eine_liste[0]}.")
print(f"Der zweite Element ist {eine_liste[0]}.")
print(f"Der letzte Element ist {eine_liste[-1]}.")
# sort()
eine_liste.sort()
print(f"Gesortet: {eine_liste}.")
#beliebig_gemischt.sort()       # geht auch nicht
nur_zahlen = [4, 13, 8, -12.3, 99, 0.29843]
nur_zahlen.sort()
print(nur_zahlen)
# man kann listen erweitern
nur_zahlen.append(4)
print(nur_zahlen)
print(f"4 wiederholt sich {nur_zahlen.count(4)}-mal.")

# ############## Meine Noten
meine_noten = [1.0, 2.3, 1.7, 1.0, 1.3, 3.5, 3.0, 1.3, 2.5]
# sum()
durchschnitt = sum(meine_noten)/len(meine_noten)
print(f"Meine Durchschnittsnote ist {durchschnitt}.")
# man kann auch etwas verändern ...
meine_noten[5] = 1.0
meine_noten[6] = 1.0
print(meine_noten)
durchschnitt = sum(meine_noten)/len(meine_noten)
print(f"Meine Durchschnittsnote ist jetzt {durchschnitt}.")

meine_noten.sort()
print(f"Die besten 5 Noten sind: {meine_noten[0:5]}.")
print(f"Die schlechtesten 5 Noten sind: {meine_noten[-1:-6:-1]}")

# Jetzt selbständig:
# - Liste meiner Freunden
# - Liste von Tieren
# - wie frühr bin ich diese Woche aufgestanden
# - ...oder was spannenderes
# und benutze mindestens einige dieser Funktionen!

# Fortgeschrittene Aufgaben mit Listen (for-schleifen!)
# - die Summe aller Elementen
# - finde den großten Element
# - finde Wörter länger als n Zeichnen
# - Quadraten
# - entferne Elemente die doppelt vorkommen

# Extra if someone is interested - operations on strings (let them google more)
print(" --------- strings -----------")
mein_name = "hana"
print(f"Mein Name : {mein_name.capitalize()}.")
print(f"Mein Name ist super wichtig: {mein_name.upper()}.")
print(mein_name.center(30, "@"))
print(mein_name.center(50, "!"))
# palindromen
print(f"Mein Name umgekehrt ist {mein_name[::-1].capitalize()}.")
palindrom = "neffen"
print(f"{palindrom} umgekehrt ist gleich {palindrom[::-1]}!")
ein_palinrom = "Bei der Edna redete der andere Dieb"
print(ein_palinrom[::-1].lower())
# ... und so weiter ...


# Fortgeschrittene Aufgaben mit strings (for-schleifen!)
# - wie viele Zeichen hat der String (ohne len() zu benutzen)
# - string aus ersten 2 und letzten 2 Charakter
# - entferne ein bestimmtes Wort aus dem Satz ...
