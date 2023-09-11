def Pierre(total_distance, max_steps):
    initial_distance = total_distance
    distance = initial_distance
    step = 1
    
    while distance > 0 and step <= max_steps:
        print(f"Étape {step}: Distance restante = {distance} mètres")
        distance /= 2  # Réduit la distance de moitié à chaque étape
        step += 1

if __name__ == "__main__":
    total_distance = 8  # Distance totale de 8 mètres
    max_steps = 10  # Nombre maximal d'étapes
    print(f"Simulation du paradoxe de Zénon pour une distance totale de {total_distance} mètres (arrêt après {max_steps} étapes) :")
    Pierre(total_distance, max_steps)