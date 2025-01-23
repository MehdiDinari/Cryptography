def vigenere_decrypt(encrypted_text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''
    key_index = 0

    for char in encrypted_text.lower():
        if char in alphabet:
            text_index = alphabet.index(char)
            key_char = key[key_index % len(key)]  # Utilise le caractère suivant de la clé
            key_index_value = alphabet.index(key_char)

            # Déchiffrement
            decrypted_char = alphabet[(text_index - key_index_value) % 26]
            decrypted_text += decrypted_char

            key_index += 1
        else:
            decrypted_text += char  # On conserve les caractères non alphabétiques

    return decrypted_text

# Demande d'entrée utilisateur pour déchiffrer
encrypted_text = input("Entrez le texte chiffré : ")
key = input("Entrez la clé : ")

# Déchiffrement
decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Texte déchiffré : {decrypted_text}")
