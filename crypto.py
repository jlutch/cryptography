# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    #checking to see if the message is empty
    if len(plaintext) == 0:
        return "Please enter something with a length greater than 0"
    #converting text into ascii charecters
    asciitext = []
    for charecter in plaintext:
        asciitext.append(ord(charecter))
    
    #shifting each ascii charecter
    for number in range(0, len(asciitext)):
        if asciitext[number] >= 65 and asciitext[number] <= 90:
            asciitext[number] += offset
            if asciitext[number] > 90:
                asciitext[number] -= 26

    #turning the numbers back into letters
    encrytped = []
    for number in asciitext:
        encrytped.append(chr(number))
    
    #making string easy to read
    linker = ''
    return linker.join(encrytped)

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    #checking to see if the message is empty
    if len(ciphertext) == 0:
        return "Please enter something with a length greater than 0"
    #converting text into ascii charecters
    asciitext = []
    for charecter in ciphertext:
        asciitext.append(ord(charecter))
    
    #shifting each ascii charecter
    for number in range(0, len(asciitext)):
        if asciitext[number] >= 65 and asciitext[number] <= 90:
            asciitext[number] -= offset
            if asciitext[number] < 65:
                asciitext[number] += 26

    #turning the numbers back into letters
    encrytped = []
    for number in asciitext:
        encrytped.append(chr(number))
    
    #making string easy to read
    linker = ''
    return linker.join(encrytped)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
     #checking to see if the message is empty
    if len(plaintext) == 0:
        return "Please enter something with a length greater than 0"
    newkeyword = keyword
    if len(plaintext) > len(keyword):
        while len(newkeyword) != len(plaintext):
            




# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    pass

if __name__ == "__main__":
    main()
    print(encrypt_caesar("PYTHON", 3))
    print(decrypt_caesar(encrypt_caesar("PYTHON", 3), 3))
