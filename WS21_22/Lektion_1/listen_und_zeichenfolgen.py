# Verschiedene Typen von Variablen
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

# Operationen auf Listen
die_laenge = len(eine_liste)
print(f"Die Liste hat {die_laenge} Elementen.")
print(" ".join(eine_liste))
print("-".join(eine_liste))
#print(" ".join(beliebig_gemischt))   # das geht nicht
eine_liste.sort()
print(eine_liste)
#beliebig_gemischt.sort()       # geht auch nicht
nur_zahlen = [4, 13, 8, -12.3, 99, 0.29843]
nur_zahlen.sort()
print(nur_zahlen)
# man kann listen erweitern
nur_zahlen.append(4)
for x in range(10):
    nur_zahlen.append(x)
print(nur_zahlen)
print(f"4 wiederholt sich {nur_zahlen.count(4)}-mal.")
# wie kann man das nutzen?
meine_noten = [1.0, 2.3, 1.7, 1.0, 1.3, 3.5, 3.0, 1.3, 2.5]
durchschnitt = sum(meine_noten)/len(meine_noten)
print(f"Meine Durchschnittsnote ist {durchschnitt}.")
# man kann auch etwas verändern ...
meine_noten[5] = 1.0
meine_noten[6] = 1.0
print(meine_noten)
durchschnitt = sum(meine_noten)/len(meine_noten)
print(f"Meine Durchschnittsnote ist jetzt {durchschnitt}.")

for index in range(len(meine_noten)):
    print(f"Meine {index}-te Note ist {meine_noten[index]}.")

meine_freundinnen = ["Iwona", "Mateja", "Clea"]
for freundin in meine_freundinnen:
    print(f"Ich mag {freundin}.")
print(f"Ich gehe spazieren mit {', '.join(meine_freundinnen)}.")

meine_noten.sort()
print(f"Die besten 5 Noten sind:")
for index in range(5):
    print(meine_noten[index])
meine_noten.reverse()
print(f"Die schlechtesten 5 Noten sind:")
for index in range(5):
    print(meine_noten[index])

# optional: strings (Zeichenfolgen) bieten auch viele Optionen
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
