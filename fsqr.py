

# Input can be case insensitive.

# Four Square Implementation :

'''
key1 = "KEYWORD1"
key2 = "KEYWORD2"
'''

def generate_square(key1, key2):
    # Generate a 5x5 alphabet square for the first key
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key1 = key1.upper().replace("J", "I")
    key1 = "".join(dict.fromkeys(key1))
    square1 = key1 + "".join([c for c in alphabet if c not in key1])

    # Generate a 5x5 alphabet square for the second key
    key2 = key2.upper().replace("J", "I")
    key2 = "".join(dict.fromkeys(key2))
    square2 = key2 + "".join([c for c in alphabet if c not in key2])

    #print('keys :', square1, square2)
    return square1, square2


def four_square_encrypt(plaintext, key1, key2) :
    square1, square2 = generate_square(key1, key2)
    plaintext = plaintext.upper().replace("J", "I")
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext):
            pair1 = plaintext[i]
            pair2 = plaintext[i + 1]
        else:
            pair1 = plaintext[i]
            pair2 = 'X'

        row1, col1 = divmod(square1.index(pair1), 5)
        row2, col2 = divmod(square2.index(pair2), 5)

        ciphertext += square1[row1 * 5 + col2] + square2[row2 * 5 + col1]

    #print('cipher', ciphertext)
    return ciphertext


def four_square_decrypt(ciphertext, key1, key2):
    square1, square2 = generate_square(key1, key2)
    ciphertext = ciphertext.upper().replace("J", "I")
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            pair1 = ciphertext[i]
            pair2 = ciphertext[i + 1]
        else:
            pair1 = ciphertext[i]
            pair2 = 'X'

        row1, col1 = divmod(square1.index(pair1), 5)
        row2, col2 = divmod(square2.index(pair2), 5)

        plaintext += square1[row1 * 5 + col2] + square2[row2 * 5 + col1]

    #print('plain', plaintext)
    return plaintext

'''
# Example usage
key1 = "KEYWORD1"
key2 = "KEYWORD2"
plaintext = "HELLO"

cipher_text = four_square_encrypt(plaintext, key1, key2)
print("Cipher Text:", cipher_text)

decoded_text = four_square_decrypt(cipher_text, key1, key2)
print("Decoded Text:", decoded_text)
'''

