

# Bifid Cipher implementation :

key = [['p', 'h', 'q', 'g', 'm', '4'],
       ['e', 'a', 'y', 'l', 'n', '5'],
       ['o', 'f', 'd', 'x', 'k', '6'],
       ['r', 'c', 'v', 's', 'z', '7'],
       ['w', 'b', 'u', 't', 'i', '8'],
       ['j', '0', '1', '2', '3', '9']]
period = 5

# Function to encrypt using Bifid Cipher :
def encrypt(P) :
    
    P = P.lower()
    
    C = ''  # Resultant cipher.
    rows = []
    cols = []
    
    for char in P :
        
        for i in range(len(key)) :

            if char in key[i] :
                
                rows.append(i)
                
                col = key[i].index(char)
                cols.append(col)
    
    
    midCipher = ''
    rowLen = len(rows)
    
    for i in range(0, rowLen, period) :
        
        for j in range(i, min(i + period, rowLen)) :
            midCipher += str(rows[j])
        
        for j in range(i, min(i + period, rowLen)) :
            midCipher += str(cols[j])

    for i in range(0, len(midCipher), 2) :
        row = int(midCipher[i])
        col = int(midCipher[i + 1])
        
        C += key[row][col]
    
    return C

# Function to decrypt using Bifid Cipher :
def decrypt(C) :
    
    C = C.lower()
    
    P = ''
    rows = []
    cols = []
    
    # String that stores the row and col of each character in Cipher text.
    midCipher = ''
    

    # Finding row and column of each char of Cipher text.
    for char in C :
        
        for i in range(len(key)) :

            if char in key[i] :
                
                # If current character is found in the ith row of the key then append the row to the string "midCipher".
                midCipher += str(i)
                
                col = key[i].index(char)  # Corresponding column.
                
                midCipher += str(col)


    for i in range(0, len(midCipher), period + period) :
        
        if i + period + period <= len(midCipher) :
            rows += list(midCipher[i : period + i])
            cols += list(midCipher[period + i: period + period + i])
        
        
        else :
            Len = len(midCipher) - i
            rows += list(midCipher[i : i + Len // 2])
            cols += list(midCipher[i + Len // 2 :])
        

    for i in range(len(rows)) :
        
        P += key[int(rows[i])][int(cols[i])]


    return P


