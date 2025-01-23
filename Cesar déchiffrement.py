def phraseNumerique(phrase):
    valeurs = []

    for lettre in phrase:
        if lettre.isalpha():
            lettre = lettre.lower()
            valeur = ord(lettre) - ord('a')
            valeurs.append(valeur)
        else:
            valeurs.append(-1)

    return valeurs

def decrementer(valeurs, k):
    valeurs_decrementees = [((valeur - k + 26) % 26) if valeur != -1 else -1 for valeur in valeurs]
    return valeurs_decrementees

def retransformerEnLettres(valeurs):
    phrase = ''.join([chr(valeur + ord('a')) if valeur != -1 else ' ' for valeur in valeurs])
    return phrase

print("Taper la phrase à décrypter")
phrase = input()

valeurs_numeriques = phraseNumerique(phrase)

# Lecture de l'incrément k
print("Choisir une valeur de k (entre 1 et 25) pour décrémenter la phrase :")
k = int(input())

# Décrémentation des valeurs numériques par k
valeurs_decrementees = decrementer(valeurs_numeriques, k)

# Rétransformation des valeurs décrémentées en lettres
phrase_decrementee = retransformerEnLettres(valeurs_decrementees)

# Affichage des résultats
print("Les valeurs numériques de la phrase sont :")
print(valeurs_numeriques)

print(f"Les valeurs numériques après décrémentation par {k} sont :")
print(valeurs_decrementees)

print("La phrase décryptée est :")
print(phrase_decrementee)
