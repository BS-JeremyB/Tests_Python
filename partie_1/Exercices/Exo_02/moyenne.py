def calcul_moyenne(notes):
    if len(notes) == 0:
        raise ValueError("La liste est vide")
    return sum(notes) / len(notes)