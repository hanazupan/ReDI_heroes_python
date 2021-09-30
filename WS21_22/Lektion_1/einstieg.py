# print - schreib etwas
print("Hallo Welt!")

# Variable - ein Aufkleber auf einem Karton, Inhalt des Kartons kann sich mit der Zeit ändern
# Kalkulator - probiere alle mögliche Rechenoperationen aus
a = 5
b = 7
print("---- Addition ----")
print(a+b)
x = 18.45
y = 5.3
print("---- Subtraktion ----")
print(x - y)
eine_zahl = 2387
zweite_zahl = 17
print("---- Multiplikation ----")
print(a*b)
dividend = 356
divisor = 5
ergebnis = dividend/divisor
print("---- Division ----")
print("Das Quotient ist", ergebnis, ".")
# Eine alternative (optional)
print("Das Quotient ist " + str(ergebnis) + ".")
# Noch eine schönere Alternative (optional)
print(f"Das Quotient ist {ergebnis}.")
# und kann man durch 0 teilen?
zahl = 50
nul = 0
#print(f"Ich versuche 50 durch 0 zu teilen. Ergebnis: {zahl/nul}")
# Weiterführende mathematische Operationen: Potenzen, Division (ganze Zahlen), rest der Division (optional)
print(f"Was ist 2**4? {2**4}")
print(f"Was ist 9//4? {9//4}")
print(f"Was ist 9%4? {9%4}")
# runden kann auch nützlich sein
print(3861/24, round(3861/24))

# for-Schleifen: Ich will nicht immer das ganze wiederholen. lass den Computer arbeiten ...
print("Die einfachste for-Schleife der Welt.")
for x in range(10):
    print(x)
print("Willst du die Vielfachen von 3 nachgucken?")
for faktor in range(11):
    print(f"3 mal {faktor} ist {3*faktor}.")
print("Wie wäre es mit Potenzen?")
for potenze in range(11):
    print(f"2 hoch {potenze} ist {2**potenze}")
# ... und warum sind diese Zahlen wichtig für Computern?
print("Wie alt warst du in der Vergangenheit?")
for alter in range(24):
    print(f"Am 4.11.{1997+alter} war ich {alter} Jahre alt.")
print("Bald werde ich 24 Jahre alt! :O")
# und weitere Vorschläge