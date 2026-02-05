import string

# ----- Some Hints -----
# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase
print(f"{alphabet = }")

# You can look up the index of a letter in the alphabet like this:
index = alphabet.index("a")
print(f"position of 'a' in the alphabet: {index}")

# The computer already thinks of all the characters it can print out as numbers.
# If you want to, you can look up what number a character corresponds to in
# "ASCII" encoding:
ascii_number = ord("a")
print(f"ascii number representation of 'a': {ascii_number}")

ascii_letter = chr(97)
print(f"ascii letter at position #97: {ascii_letter}")

# ----- Your Algorithm -----

# Your task is to encrypt this secret message into ciphertext
plaintext = "This is a secret message."

# Initialize your ciphertext an empty string
ciphertext = ""


#encryption
for character in plaintext:
    if character in alphabet:
        index = alphabet.index(character.lower())
        new_index = (index + 5) % 26
        encrypted_character = alphabet[new_index]
        
        if character.isupper():
            encrypted_character = encrypted_character.upper()

    else: encrypted_character = character

    ciphertext += encrypted_character

#print encryption
print(f"{ciphertext = }")



decrypted_plaintext = ""


#decryption
for character in ciphertext:
    if character in alphabet:
        index = alphabet.index(character.lower())
        new_index = (index - 5) % 26
        decrypted_character = alphabet[new_index]
        
        if character.isupper():
            decrypted_character = decrypted_character.upper()

    else: decrypted_character = character

    decrypted_plaintext += decrypted_character

#print decryption
print(f"{decrypted_plaintext = }")