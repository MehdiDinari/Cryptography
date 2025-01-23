def xor_encrypt_decrypt(message, key):

    result = ''.join(chr(ord(c) ^ key) for c in message)
    return result


# Interface utilisateur
if __name__ == "__main__":
    print("Méthode XOR - Chiffrement/Déchiffrement")
    action = input("Voulez-vous (C)hiffrer ou (D)échiffrer un message ? (C/D): ").strip().upper()

    if action in ('C', 'D'):
        message = input("Entrez le message : ")
        try:
            key = int(input("Entrez une clé numérique (entier) : "))
            result = xor_encrypt_decrypt(message, key)
            print(f"Résultat : {result}")
        except ValueError:
            print("Erreur : La clé doit être un entier.")
    else:
        print("Action non reconnue. Veuillez choisir 'C' ou 'D'.")
