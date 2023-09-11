import time

# Vitesses d'Achille et de la Tortue
vitesse_achille = 3
vitesse_tortue = 2

# Positions initiales d'Achille et de la Tortue
position_achille = 0
position_tortue = 4

# Distance totale de la course
distance_course = 10

# Boucle de la course
while position_achille < distance_course and position_tortue < distance_course:
    # Avance d'une étape en fonction de leurs vitesses respectives
    position_achille += vitesse_achille
    position_tortue += vitesse_tortue

    # Affichage des positions actuelles
    print(f"Achille est à la position {position_achille}, Tortue est à la position {position_tortue}")

    # Pause pour rendre la simulation visible
    time.sleep(1)

# Déterminer le gagnant
if position_achille > position_tortue:
    print("Achille a gagné la course !")
elif position_tortue > position_achille:
    print("La Tortue a gagné la course !")
else:
    print("C'est une égalité !")

