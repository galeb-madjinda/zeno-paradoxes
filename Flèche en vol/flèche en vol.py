import time

# Défini la position de la flèche
position_x = 0
position_y = 0

# Définir la vitesse de la flèche (changement de position par instant)
vitesse_x = 2  # Déplacez la flèche de 2 unités à chaque instant
vitesse_y = 1  # Déplacez la flèche de 1 unité à chaque instant

# Nombre total d'instants à simuler
nombre_instants = 10

# Boucle de simulation
for instant in range(nombre_instants):
    # Mettre à jour la position de la flèche
    position_x += vitesse_x
    position_y += vitesse_y

    # Afficher la position de la flèche à cet instant
    print(f"Instant {instant + 1}: Position de la flèche - X: {position_x}, Y: {position_y}")


# Afficher le résultat final
print("Simulation terminée. La flèche a parcouru sa trajectoire.")

