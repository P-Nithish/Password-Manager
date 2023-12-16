

def encrypt_rail_fence(text, rails):
    rail_fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        rail_fence[rail] += char
        rail += direction

        if rail == rails:
            rail -= 2
            direction = -1
        elif rail == -1:
            rail += 2
            direction = 1

    encrypted_text = ''.join(rail_fence)
    return encrypted_text

def decrypt_rail_fence(text, rails):
    rail_length = len(text) // rails
    rail_counts = [rail_length] * rails
    extra = len(text) % rails

    rail = 0
    direction = 1
    index = 0

    rail_fence = ['' for _ in range(rails)]

    for i in range(rails):
        rail_length = rail_counts[i]

        if extra > 0:
            extra -= 1
            rail_length += 1

        rail_fence[i] = text[index:index+rail_length]
        index += rail_length

    decrypted_text = ''

    for i in range(len(text)):
        if len(rail_fence[rail]) > 0:
            decrypted_text += rail_fence[rail][0]
            rail_fence[rail] = rail_fence[rail][1:]
        rail += direction

        if rail == rails:
            rail -= 2
            direction = -1
        elif rail == -1:
            rail += 2
            direction = 1

    return decrypted_text

# Example usage
plaintext = "Hello, Rail Fence Cipher!"
num_rails = 2   #always 2

encrypted_text = encrypt_rail_fence(plaintext, num_rails)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, num_rails)
print("Decrypted:", decrypted_text)


