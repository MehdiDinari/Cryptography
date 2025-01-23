def vigenere_block_encrypt(message, key, block_size):
    """Chiffre un message avec la méthode Vigenère par bloc."""
    encrypted_message = []
    key = key.upper()
    key_index = 0

    for i in range(0, len(message), block_size):
        block = message[i:i + block_size].upper()
        encrypted_block = ""

        for char in block:
            if char.isalpha():  # Applique le chiffrement uniquement sur les lettres
                shift = ord(key[key_index % len(key)]) - ord('A')
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                encrypted_block += encrypted_char
                key_index += 1
            else:
                encrypted_block += char  # Garde les caractères non alphabétiques

        encrypted_message.append(encrypted_block)

    return ''.join(encrypted_message)


def vigenere_block_decrypt(encrypted_message, key, block_size):
    """Déchiffre un message avec la méthode Vigenère par bloc."""
    decrypted_message = []
    key = key.upper()
    key_index = 0

    for i in range(0, len(encrypted_message), block_size):
        block = encrypted_message[i:i + block_size].upper()
        decrypted_block = ""

        for char in block:
            if char.isalpha():  # Applique le déchiffrement uniquement sur les lettres
                shift = ord(key[key_index % len(key)]) - ord('A')
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
                decrypted_block += decrypted_char
                key_index += 1
            else:
                decrypted_block += char  # Garde les caractères non alphabétiques

        decrypted_message.append(decrypted_block)

    return ''.join(decrypted_message)


# Exemple d'utilisation
if __name__ == "__main__":
    print("Méthode Vigenère par bloc")
    choix = input("Voulez-vous chiffrer ou déchiffrer un message ? (chiffrer/déchiffrer) : ").strip().lower()
    message = input("Entrez le message : ")
    key = input("Entrez la clé : ")
    block_size = int(input("Entrez la taille du bloc : "))

    if choix == "chiffrer":
        result = vigenere_block_encrypt(message, key, block_size)
        print("Message chiffré :", result)
    elif choix == "déchiffrer":
        result = vigenere_block_decrypt(message, key, block_size)
        print("Message déchiffré :", result)
    else:
        print("Choix non valide !")
