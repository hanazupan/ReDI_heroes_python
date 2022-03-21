# Was haben wir letztes mal gelernt?

# Variablen und Druck
print("Guten Morgen")
tierart = "Elefant"
name = "Max"
print(f"Dieses {tierart} heißt {name}.")
name = "Elena"
print(f"Dieses {tierart} heißt {name}.")

# Listen
tieren = ["Elefant", "Gorilla", "Schnecke"]
print(f"Das zweite Tier ist {tieren[1]}.")
essen_menge = [3000, 200, 5]
durchschnitt_menge = sum(essen_menge)/len(essen_menge)
tieren.append("Adler")
tieren.remove("Schnecke")
print(tieren)

# turtle
import turtle as t
t.color("blue")
t.width(5)
t.circle(30, 270)
t.fd(100)
t.right(45)
t.fd(30)