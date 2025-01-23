def vernam_encrypt(message, key):
    """Chiffre un message avec la méthode Vernam (C = M + Key)."""
    encrypted_message = []
    for m, k in zip(message, key):
        encrypted_char = chr(((ord(m.upper()) - 65 + ord(k.upper()) - 65) % 26) + 65)
        encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)

def vernam_decrypt(encrypted_message, key):
    """Déchiffre un message chiffré avec la méthode Vernam (M = C - Key)."""
    decrypted_message = []
    for c, k in zip(encrypted_message, key):
        decrypted_char = chr(((ord(c.upper()) - 65 - (ord(k.upper()) - 65) + 26) % 26) + 65)
        decrypted_message.append(decrypted_char)
    return ''.join(decrypted_message)

# Menu principal
print("Choisissez une option :")
print("1. Chiffrer un message")
print("2. Déchiffrer un message")
choice = input("Entrez 1 ou 2 : ")

if choice == "1":
    message = input("Entrez le message à chiffrer (lettres uniquement) : ").upper()
    key = input("Entrez la clé (même taille que le message) : ").upper()

    # Vérification que la clé est de la même longueur que le message
    while len(key) != len(message):
        print("Erreur : La clé doit avoir la même taille que le message.")
        key = input("Entrez une clé valide : ").upper()

    # Chiffrement
    encrypted_message = vernam_encrypt(message, key)
    print(f"Message chiffré : {encrypted_message}")

elif choice == "2":
    encrypted_message = input("Entrez le message chiffré (lettres uniquement) : ").upper()
    key = input("Entrez la clé (même taille que le message) : ").upper()

    # Vérification que la clé est de la même longueur que le message chiffré
    while len(key) != len(encrypted_message):
        print("Erreur : La clé doit avoir la même taille que le message chiffré.")
        key = input("Entrez une clé valide : ").upper()

    # Déchiffrement
    decrypted_message = vernam_decrypt(encrypted_message, key)
    print(f"Message déchiffré : {decrypted_message}")

else:
    print("Choix invalide. Veuillez redémarrer le programme et entrer 1 ou 2.")
