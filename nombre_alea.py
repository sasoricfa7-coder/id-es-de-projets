#!/usr/bin/env python3
"""Génère un nombre aléatoire cryptographique du nombre de chiffres souhaité."""

import secrets


def nombre_aleatoire(nb_chiffres: int) -> str:
    """Renvoie une chaîne de nb_chiffres chiffres aléatoires (le premier != 0)."""
    if nb_chiffres < 1:
        raise ValueError("Il faut au moins 1 chiffre.")

    # Premier chiffre : entre 1 et 9 (pour éviter les zéros en tête)
    premier = str(secrets.randbelow(9) + 1)

    # Chiffres suivants : entre 0 et 9
    suivants = "".join(str(secrets.randbelow(10)) for _ in range(nb_chiffres - 1))

    return premier + suivants


if __name__ == "__main__":
    try:
        n = int(input("Combien de chiffres veux-tu ? "))
        resultat = nombre_aleatoire(n)
        print(f"\nNombre généré :\n{resultat}")
    except ValueError as e:
        print(f"Erreur : {e}")
