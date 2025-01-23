import random
import string

def generate_unique_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)  # Mélange aléatoire des lettres
    return ''.join(alphabet)  # Renvoie l'alphabet mélangé comme clé

def vigenere_encrypt(plain_text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    key_index = 0

    for char in plain_text.lower():
        if char in alphabet:
            text_index = alphabet.index(char)
            key_char = key[key_index % len(key)]  # Utilise le caractère suivant de la clé
            key_index_value = alphabet.index(key_char)

            # Chiffrement
            encrypted_char = alphabet[(text_index + key_index_value) % 26]
            encrypted_text += encrypted_char

            key_index += 1
        else:
            encrypted_text += char  # On conserve les caractères non alphabétiques

    return encrypted_text

# Demande d'entrée utilisateur
plain_text = input("Entrez le texte à chiffrer : ")
key = generate_unique_key()

# Chiffrement
encrypted_text = vigenere_encrypt(plain_text, key)
print(f"\nClé générée : {key}")
print(f"Texte chiffré : {encrypted_text}")
