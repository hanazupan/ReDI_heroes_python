import numpy as np
optionen = ("Schere", "Stein", "Papier")

spieler = input("Schere, Stein, Papier! Was wählst du? ")

computer = np.random.choice(optionen)
print(f"Computer hat {computer} ausgewählt!")

if spieler == "Stein" and computer == "Schere":
    print("Spieler gewinnt!")
elif spieler == "Papier" and computer == "Stein":
    print("Spieler gewinnt!")
elif spieler == "Schere" and computer == "Papier":
    print("Spieler gewinnt!")
elif computer == "Stein" and spieler == "Schere":
    print("Computer gewinnt!")
elif computer == "Papier" and spieler == "Stein":
    print("Computer gewinnt!")
elif computer == "Schere" and spieler == "Papier":
    print("Computer gewinnt!")
else:
    print("Niemand gewinnt.")