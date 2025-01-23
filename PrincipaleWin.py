import tkinter as tk
from tkinter import messagebox


def vernam_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("La longueur de la clé doit être égale à celle du message chiffré.")

    decrypted_message = ""
    for i in range(len(ciphertext)):
        decrypted_char_ascii = (ord(ciphertext[i]) - ord(key[i])) % 256
        decrypted_message += chr(decrypted_char_ascii)

    return decrypted_message


def decrypt_message():
    ciphertext = entry_ciphertext_vernam.get()
    key = entry_key_vernam_dec.get()

    if len(ciphertext) != len(key):
        messagebox.showerror("Erreur", "La clé doit avoir la même longueur que le message chiffré.")
        return

    try:
        result = vernam_decrypt(ciphertext, key)
        label_result.config(text="Message déchiffré : " + result)
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def vernam_cipher(message, key):
    if len(message) != len(key):
        raise ValueError("La longueur de la clé doit être égale à celle du message.")

    encrypted_message = ""

    for i in range(len(message)):
        message_char_ascii = ord(message[i])
        key_char_ascii = ord(key[i])

        encrypted_char_ascii = (message_char_ascii + key_char_ascii) % 256

        encrypted_message += chr(encrypted_char_ascii)

    return encrypted_message

def crypter_vernam():
    message = entry_message_vernam.get()  # Correction ici
    key = entry_key_vernam.get()  # Correction ici

    if len(message) != len(key):
        messagebox.showerror("Erreur", "La clé doit avoir la même longueur que le message.")
        return

    try:
        resultat_chiffre = vernam_cipher(message, key)
        messagebox.showinfo("Résultat", f"Message chiffré avec Vernam : {resultat_chiffre}")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def vigenere_decrypt(encrypted_text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''
    key_index = 0

    for char in encrypted_text.lower():
        if char in alphabet:
            text_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_index_value = alphabet.index(key_char)

            decrypted_char = alphabet[(text_index - key_index_value) % 26]
            decrypted_text += decrypted_char

            key_index += 1
        else:
            decrypted_text += char  # On conserve les caractères non alphabétiques

    return decrypted_text

def decrypter_vigenere():
    encrypted_text = entry_encrypted_text_vigenere.get()
    key = entry_key_vigenere_decrypt.get().lower()

    if not key.isalpha():
        messagebox.showerror("Erreur", "La clé doit contenir uniquement des lettres")
        return

    decrypted_text = vigenere_decrypt(encrypted_text, key)
    messagebox.showinfo("Résultat", f"Texte déchiffré avec Vigenère : {decrypted_text}")


def vigenere_encrypt(plain_text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    key_index = 0

    for char in plain_text.lower():
        if char in alphabet:
            text_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_index_value = alphabet.index(key_char)

            encrypted_char = alphabet[(text_index + key_index_value) % 26]
            encrypted_text += encrypted_char

            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text


def crypter_vigenere():
    plain_text = entry_plain_text_vigenere.get()
    key = entry_key_vigenere.get().lower()

    if not key.isalpha():
        messagebox.showerror("Erreur", "La clé doit contenir uniquement des lettres")
        return

    encrypted_text = vigenere_encrypt(plain_text, key)
    messagebox.showinfo("Résultat", f"Texte chiffré avec Vigenère : {encrypted_text}")


def show_frame(frame):
    frame.tkraise()

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

def attaque_cesar():
    phrase = entry_phrase_attack.get()
    valeurs_numeriques = phraseNumerique(phrase)
    resultats = []

    for k in range(1, 26):
        valeurs_decrementees = decrementer(valeurs_numeriques, k)
        phrase_decrementee = retransformerEnLettres(valeurs_decrementees)
        resultats.append(f"Résultat pour k = {k} : {phrase_decrementee}")

    messagebox.showinfo("Résultats de l'attaque César", "\n".join(resultats))

def incrementer(valeurs, k):
    valeurs_incrementees = [(valeur + k) % 26 if valeur != -1 else -1 for valeur in valeurs]
    return valeurs_incrementees

def retransformerEnLettres(valeurs):
    phrase = ''.join([chr(valeur + ord('a')) if valeur != -1 else ' ' for valeur in valeurs])
    return phrase

def decrementer(valeurs, k):
    valeurs_decrementees = [((valeur - k + 26) % 26) if valeur != -1 else -1 for valeur in valeurs]
    return valeurs_decrementees

def decrypter_cesar():
    phrase = entry_phrase_decrypt.get()
    try:
        k = int(entry_k_decrypt.get())
        if k < 1 or k > 25:
            messagebox.showerror("Erreur", "La valeur de k doit être entre 1 et 25")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un entier pour k")
        return

    valeurs_numeriques = phraseNumerique(phrase)
    valeurs_decrementees = decrementer(valeurs_numeriques, k)
    phrase_decrementee = retransformerEnLettres(valeurs_decrementees)

    messagebox.showinfo("Résultat", f"Phrase décryptée : {phrase_decrementee}")

def crypter_cesar():
    phrase = entry_phrase.get()
    try:
        k = int(entry_k.get())
        if k < 1 or k > 25:
            messagebox.showerror("Erreur", "La valeur de k doit être entre 1 et 25")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un entier pour k")
        return

    valeurs_numeriques = phraseNumerique(phrase)
    valeurs_incrementees = incrementer(valeurs_numeriques, k)
    phrase_incrementee = retransformerEnLettres(valeurs_incrementees)

    messagebox.showinfo("Résultat", f"Phrase cryptée : {phrase_incrementee}")

root = tk.Tk()
root.title("Application de Cryptage")
root.geometry("700x700")
root.config(bg="#333333")

main_frame = tk.Frame(root, bg="#444444")
encrypt_frame = tk.Frame(root, bg="#444444")
decrypt_frame = tk.Frame(root, bg="#444444")
attack_frame = tk.Frame(root, bg="#444444")
cesar_frame = tk.Frame(root, bg="#444444")
vigenere_frame = tk.Frame(root, bg="#444444")
vigenere_bloc_frame = tk.Frame(root, bg="#444444")
vernam_frame = tk.Frame(root, bg='#444444')
vernam_dec_frame = tk.Frame(root, bg="#444444")
cesar_decrypt_frame = tk.Frame(root, bg="#444444")
vigenere_decrypt_frame = tk.Frame(root, bg="#444444")
cesar_attack_frame = tk.Frame(root, bg="#444444")


for frame in (main_frame, encrypt_frame, decrypt_frame, attack_frame, cesar_frame,
              vigenere_frame, vigenere_bloc_frame, vernam_frame, cesar_decrypt_frame,
              vigenere_decrypt_frame, cesar_attack_frame , vernam_dec_frame):
    frame.grid(row=0, column=0, sticky="nsew")

button_style = {"font": ("Arial", 14, "bold"), "bg": "#555555", "fg": "#ffffff", "activebackground": "#666666", "width": 25, "height": 3}

# Page principale
tk.Label(main_frame, text="Choisissez une action", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=30)
tk.Button(main_frame, text="Crypter un message", command=lambda: show_frame(encrypt_frame), **button_style).pack(pady=10)
tk.Button(main_frame, text="Décrypter un message", command=lambda: show_frame(decrypt_frame), **button_style).pack(pady=10)
tk.Button(main_frame, text="Effectuer une attaque", command=lambda: show_frame(attack_frame), **button_style).pack(pady=10)

# Page de cryptage
tk.Label(encrypt_frame, text="Méthodes de Cryptage", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=30)
tk.Button(encrypt_frame, text="César", command=lambda: show_frame(cesar_frame), **button_style).pack(pady=5)
tk.Button(encrypt_frame, text="Vigenère", command=lambda: show_frame(vigenere_frame), **button_style).pack(pady=5)
tk.Button(encrypt_frame, text="Vigenère par Bloc", command=lambda: show_frame(vigenere_bloc_frame), **button_style).pack(pady=5)
tk.Button(encrypt_frame, text="Vernam", command=lambda: show_frame(vernam_frame), **button_style).pack(pady=5)
tk.Button(encrypt_frame, text="XOR", **button_style).pack(pady=5)
tk.Button(encrypt_frame, text="Retour", command=lambda: show_frame(main_frame), **button_style).pack(pady=10)

vigenere_bloc_frame = tk.Frame(root, bg="#444444")
vigenere_bloc_frame.grid(row=0, column=0, sticky="nsew")


# Page de cryptage de César
tk.Label(cesar_frame, text="Crypter avec César", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)
tk.Label(cesar_frame, text="Entrez la phrase à crypter :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_phrase = tk.Entry(cesar_frame, font=("Arial", 14), width=30)
entry_phrase.pack(pady=5)

cesar_attack_frame = tk.Frame(root, bg="#444444")
cesar_attack_frame.grid(row=0, column=0, sticky="nsew")

vigenere_frame = tk.Frame(root, bg="#444444")
vigenere_frame.grid(row=0, column=0, sticky="nsew")

# Interface pour le chiffrement Vernam
tk.Label(vernam_frame, text="Chiffrement avec Vernam", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)
tk.Label(vernam_frame, text="Entrez le texte à chiffrer :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_message_vernam = tk.Entry(vernam_frame, font=("Arial", 14), width=30)
entry_message_vernam.pack(pady=5)

tk.Label(vernam_frame, text="Entrez la clé (de même longueur que le message) :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_key_vernam = tk.Entry(vernam_frame, font=("Arial", 14), width=30)
entry_key_vernam.pack(pady=5)

tk.Button(vernam_frame, text="Crypter", command=crypter_vernam, **button_style).pack(pady=20)
tk.Button(vernam_frame, text="Retour", command=lambda: show_frame(encrypt_frame), **button_style).pack(pady=10)
tk.Label(vernam_dec_frame, text="Déchiffrement avec Vernam", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)

# Champ pour le message chiffré
tk.Label(vernam_dec_frame, text="Entrez le message chiffré :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_ciphertext_vernam = tk.Entry(vernam_dec_frame, font=("Arial", 14), width=30)
entry_ciphertext_vernam.pack(pady=5)

# Champ pour la clé
tk.Label(vernam_dec_frame, text="Entrez la clé (de même longueur que le message chiffré) :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_key_vernam_dec = tk.Entry(vernam_dec_frame, font=("Arial", 14), width=30)
entry_key_vernam_dec.pack(pady=5)

# Label pour afficher le résultat
label_result = tk.Label(vernam_dec_frame, text="", font=("Arial", 14), bg="#444444", fg="#ffffff")
label_result.pack(pady=10)

# Bouton pour déchiffrer
tk.Button(vernam_dec_frame, text="Décrypter", command=decrypt_message, **button_style).pack(pady=20)

# Bouton pour retourner à une autre frame
tk.Button(vernam_dec_frame, text="Retour", command=lambda: show_frame(encrypt_frame), **button_style).pack(pady=20)


# Interface pour le chiffrement Vigenère
tk.Label(vigenere_frame, text="Chiffrement avec Vigenère", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)
tk.Label(vigenere_frame, text="Entrez le texte à chiffrer :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_plain_text_vigenere = tk.Entry(vigenere_frame, font=("Arial", 14), width=30)
entry_plain_text_vigenere.pack(pady=5)

tk.Label(vigenere_frame, text="Entrez la clé :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_key_vigenere = tk.Entry(vigenere_frame, font=("Arial", 14), width=30)
entry_key_vigenere.pack(pady=5)

tk.Button(vigenere_frame, text="Crypter", command=crypter_vigenere, **button_style).pack(pady=20)
tk.Button(vigenere_frame, text="Retour", command=lambda: show_frame(encrypt_frame), **button_style).pack(pady=10)

vigenere_decrypt_frame = tk.Frame(root, bg="#444444")
vigenere_decrypt_frame.grid(row=0, column=0, sticky="nsew")

# Interface pour le déchiffrement Vigenère
tk.Label(vigenere_decrypt_frame, text="Déchiffrement avec Vigenère", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)
tk.Label(vigenere_decrypt_frame, text="Entrez le texte chiffré :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_encrypted_text_vigenere = tk.Entry(vigenere_decrypt_frame, font=("Arial", 14), width=30)
entry_encrypted_text_vigenere.pack(pady=5)

tk.Label(vigenere_decrypt_frame, text="Entrez la clé :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_key_vigenere_decrypt = tk.Entry(vigenere_decrypt_frame, font=("Arial", 14), width=30)
entry_key_vigenere_decrypt.pack(pady=5)

tk.Button(vigenere_decrypt_frame, text="Déchiffrer", command=decrypter_vigenere, **button_style).pack(pady=20)
tk.Button(vigenere_decrypt_frame, text="Retour", command=lambda: show_frame(decrypt_frame), **button_style).pack(pady=10)

# Interface pour l'attaque de César
tk.Label(cesar_attack_frame, text="Attaque par force brute de César", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)
tk.Label(cesar_attack_frame, text="Entrez la phrase cryptée :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_phrase_attack = tk.Entry(cesar_attack_frame, font=("Arial", 14), width=30)
entry_phrase_attack.pack(pady=5)

tk.Button(cesar_attack_frame, text="Lancer l'attaque", command=attaque_cesar, **button_style).pack(pady=20)
tk.Button(cesar_attack_frame, text="Retour", command=lambda: show_frame(attack_frame), **button_style).pack(pady=10)

tk.Label(cesar_frame, text="Entrez la valeur de k (1-25) :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_k = tk.Entry(cesar_frame, font=("Arial", 14), width=10)
entry_k.pack(pady=5)

tk.Button(cesar_frame, text="Crypter", command=crypter_cesar, **button_style).pack(pady=20)
tk.Button(cesar_frame, text="Retour", command=lambda: show_frame(encrypt_frame), **button_style).pack(pady=10)

# Page de décryptage
tk.Label(decrypt_frame, text="Méthodes de Décryptage", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=30)
tk.Button(decrypt_frame, text="César", command=lambda: show_frame(cesar_decrypt_frame), **button_style).pack(pady=5)
tk.Button(decrypt_frame, text="Vigenère", command=lambda: show_frame(vigenere_decrypt_frame), **button_style).pack(pady=5)
tk.Button(decrypt_frame, text="Vigenère par bloc", **button_style).pack(pady=5)
tk.Button(decrypt_frame, text="Vernam", command=lambda: show_frame(vernam_dec_frame),**button_style).pack(pady=5)
tk.Button(decrypt_frame, text="XOR", **button_style).pack(pady=5)
tk.Button(decrypt_frame, text="Retour", command=lambda: show_frame(main_frame), **button_style).pack(pady=10)

# Page d'attaque
tk.Label(attack_frame, text="Méthodes d'Attaque", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=30)
tk.Button(attack_frame, text="César", command=lambda: show_frame(cesar_attack_frame), **button_style).pack(pady=5)
tk.Button(attack_frame, text="Vigenère", **button_style).pack(pady=5)
tk.Button(attack_frame, text="Vigenère par bloc", **button_style).pack(pady=5)
tk.Button(attack_frame, text="Vernam", **button_style).pack(pady=5)
tk.Button(attack_frame, text="XOR", **button_style).pack(pady=5)
tk.Button(attack_frame, text="Retour", command=lambda: show_frame(main_frame), **button_style).pack(pady=10)

cesar_decrypt_frame = tk.Frame(root, bg="#444444")
cesar_decrypt_frame.grid(row=0, column=0, sticky="nsew")

# Page de décryptage de César
tk.Label(cesar_decrypt_frame, text="Décrypter avec César", font=("Arial", 18, "bold"), bg="#444444", fg="#ffffff").pack(pady=20)
tk.Label(cesar_decrypt_frame, text="Entrez la phrase à décrypter :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_phrase_decrypt = tk.Entry(cesar_decrypt_frame, font=("Arial", 14), width=30)
entry_phrase_decrypt.pack(pady=5)

tk.Label(cesar_decrypt_frame, text="Entrez la valeur de k (1-25) :", bg="#444444", fg="#ffffff").pack(pady=5)
entry_k_decrypt = tk.Entry(cesar_decrypt_frame, font=("Arial", 14), width=10)
entry_k_decrypt.pack(pady=5)

tk.Button(cesar_decrypt_frame, text="Décrypter", command=decrypter_cesar, **button_style).pack(pady=20)
tk.Button(cesar_decrypt_frame, text="Retour", command=lambda: show_frame(decrypt_frame), **button_style).pack(pady=10)


show_frame(main_frame)

root.mainloop()
