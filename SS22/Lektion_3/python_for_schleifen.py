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
for alter in range(25):
    print(f"Am 4.11.{1997+alter} war ich {alter} Jahre alt.")
# und weitere Vorschläge

# Option: erkläre noch mehr
# Schleifen und Listen
meine_freundinnen = ["Iwona", "Mateja", "Clea"]
for freundin in meine_freundinnen:
    print(f"Ich mag {freundin}.")

for nummer in range(5, 22):
    print(f"Diese Zahl ist {nummer}.")

for nummer in range(5, 22, 2):
    print(f"Nur jede zweite Zahl: {nummer}")

for k in range(88, 80, -1):
    print(f"Ich zähle runter: {k}.")

# Für sehr fortgeschrittene:
# - Wie kann man das folgende ausdrucken?
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# - Fibonacci Zahlen
# - Wie kann man so was zeichnen?
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# - usw.