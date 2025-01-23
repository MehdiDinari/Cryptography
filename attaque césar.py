

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

# Convertir la phrase en valeurs numériques
valeurs_numeriques = phraseNumerique(phrase)

# Tester toutes les valeurs de k de 1 à 25
for k in range(1, 26):
    # Décrémenter les valeurs numériques avec la valeur actuelle de k
    valeurs_decrementees = decrementer(valeurs_numeriques, k)

    # Rétransformer les valeurs décrémentées en lettres
    phrase_decrementee = retransformerEnLettres(valeurs_decrementees)

    # Afficher les résultats pour cette valeur de k
    print(f"\nRésultat pour k = {k} :")
    print(phrase_decrementee)
