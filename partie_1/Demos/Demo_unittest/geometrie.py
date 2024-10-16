import math

def calcul_aire_cercle(rayon):
    if rayon < 0:
        raise ValueError("Le rayon doit être positif")
    return math.pi * rayon**2