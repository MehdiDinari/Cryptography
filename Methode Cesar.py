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


def incrementer(valeurs, k):
    valeurs_incrementees = [(valeur + k) % 26 if valeur != -1 else -1 for valeur in valeurs]
    return valeurs_incrementees


def retransformerEnLettres(valeurs):
    phrase = ''.join([chr(valeur + ord('a')) if valeur != -1 else ' ' for valeur in valeurs])
    return phrase


print("Taper la phrase à crypter")
phrase = input()

valeurs_numeriques = phraseNumerique(phrase)

print("Choisir une valeur de k (entre 1 et 25) pour incrémenter la phrase :")
k = int(input())

valeurs_incrementees = incrementer(valeurs_numeriques, k)

phrase_incrementee = retransformerEnLettres(valeurs_incrementees)

print("Les valeurs numériques de la phrase sont :")
print(valeurs_numeriques)

print(f"Les valeurs numériques après incrémentation par {k} sont :")
print(valeurs_incrementees)

print("La phrase cryptée est :")
print(phrase_incrementee)
