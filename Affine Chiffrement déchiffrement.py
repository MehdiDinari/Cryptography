import string
from math import gcd

# Alphabet et taille de l'alphabet
ALPHABET = string.ascii_uppercase
M = len(ALPHABET)


# Fonction pour trouver l'inverse modulaire
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Fonction de chiffrement affine
def affine_encrypt(plaintext, a, b):
    if gcd(a, M) != 1:
        raise ValueError("La clé 'a' doit être coprime avec m (taille de l'alphabet).")

    plaintext = plaintext.upper()
    encrypted = ""

    for char in plaintext:
        if char in ALPHABET:
            x = ALPHABET.index(char)
            y = (a * x + b) % M
            encrypted += ALPHABET[y]
        else:
            encrypted += char  # Garder les caractères spéciaux inchangés
    return encrypted


# Fonction de déchiffrement affine
def affine_decrypt(ciphertext, a, b):
    if gcd(a, M) != 1:
        raise ValueError("La clé 'a' doit être coprime avec m (taille de l'alphabet).")

    ciphertext = ciphertext.upper()
    decrypted = ""

    a_inv = mod_inverse(a, M)
    if a_inv is None:
        raise ValueError("Impossible de trouver l'inverse modulaire pour 'a'.")

    for char in ciphertext:
        if char in ALPHABET:
            y = ALPHABET.index(char)
            x = (a_inv * (y - b)) % M
            decrypted += ALPHABET[x]
        else:
            decrypted += char  # Garder les caractères spéciaux inchangés
    return decrypted


# Exemple d'utilisation
if __name__ == "__main__":
    mode = input("Choisissez le mode (chiffre/dechiffre) : ").strip().lower()
    message = input("Entrez le message : ").strip()
    a = int(input("Entrez la clé a (coprime avec 26) : "))
    b = int(input("Entrez la clé b : "))

    try:
        if mode == "chiffre":
            result = affine_encrypt(message, a, b)
            print(f"Message chiffré : {result}")
        elif mode == "dechiffre":
            result = affine_decrypt(message, a, b)
            print(f"Message déchiffré : {result}")
        else:
            print("Mode invalide. Choisissez 'chiffre' ou 'dechiffre'.")
    except ValueError as e:
        print(f"Erreur : {e}")
