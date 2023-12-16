

# Input can be case insensitive.

# ADFGVX Cipher implementation :

#keyword = "hello234"

def generate_grid(keyword):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    

    key = keyword + alphabet
    key = ''.join(sorted(set(key), key=key.index))
    grid = [list(key[i:i+6]) for i in range(0, len(key), 6)]
    #print(grid)
    return grid

def encrypt(plaintext, keyword) :
    
    grid = generate_grid(keyword)
    
    adfgvx = "ADFGVX"
    result = ""
    for char in plaintext:
        for row in grid:
            if char.upper() in row:
                result += adfgvx[grid.index(row)]
                result += adfgvx[row.index(char.upper())]
    return result

def decrypt(ciphertext, keyword) :
    
    grid = generate_grid(keyword)
    
    adfgvx = "ADFGVX"
    result = ""
    i = 0
    while i < len(ciphertext):
        adfg = ciphertext[i].upper()
        i += 1
        vx = ciphertext[i].upper()
        i += 1
        result += grid[adfgvx.index(adfg)][adfgvx.index(vx)]
    return result



'''
def main():
    keyword = "HELLO"
    plaintext = "defend the east wall of the castle"
    
    grid = generate_grid(keyword)
    encrypted_text = encrypt(plaintext, grid)
    decrypted_text = decrypt(encrypted_text, grid)

    print(f"Keyword: {keyword}")
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    main()
'''

