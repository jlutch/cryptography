import random
import math
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
    asciitext = turn_to_ascii(ciphertext)
    
    #shifting each ascii charecter
    for number in range(0, len(asciitext)):
        if asciitext[number] >= 65 and asciitext[number] <= 90:
            asciitext[number] -= offset
            if asciitext[number] < 65:
                asciitext[number] += 26

    #turning the numbers back into letters
    encrytped = turn_to_char(asciitext)
    
    #making string easy to read
    linker = ''
    return linker.join(encrytped)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    Avalue = 65
    #checking to see if the message is empty
    if len(plaintext) == 0:
        return "Please enter something with a length greater than 0"
   
    #making the key an equal length
    keyword = make_equal_length(plaintext, keyword)
   
    asciitext = turn_to_ascii(plaintext)
    keyword = turn_to_ascii(keyword)
    for x in range(0, len(asciitext)):
        asciitext[x] += keyword[x]-Avalue
        if asciitext[x] > 90:
            asciitext[x] -= 26
   
    #turing numbers into letters
    asciitext = turn_to_char(asciitext)

    #making string easy to read
    linker = ''
    return linker.join(asciitext)


# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    Avalue = 65
    #checking to see if the message is empty
    if len(ciphertext) == 0:
        return "Please enter something with a length greater than 0"
   
    #making the key an equal length
    keyword = make_equal_length(ciphertext, keyword)

    asciitext = turn_to_ascii(ciphertext)
    keyword = turn_to_ascii(keyword)
    #subtracting ascii values to do a negative shift
    for x in range(0, len(asciitext)):
        asciitext[x] -= keyword[x]-Avalue
        if asciitext[x] < 65:
            asciitext[x] += 26

    #turing numbers into letters
    asciitext = turn_to_char(asciitext)

    #making string easy to read
    linker = ''
    return linker.join(asciitext)

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    total = 1000
    superincreasinglist = []
    while len(superincreasinglist) < n+1:
        newentry = random.randrange(1,total)  
        #making new entry bigger than the sum of the list
        while sum(superincreasinglist) >= newentry:
            newentry += random.randrange(1,total)
        superincreasinglist.append(newentry)
        total = sum(superincreasinglist)*2
    Q = superincreasinglist.pop()
    W = superincreasinglist
    
    #we now need to find R
    R = random.randrange(1,total)
    while math.gcd(R, Q) != 1:
        R = random.randrange(1,total)
    return tuple(W),Q,R
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

# Makes the contents of a list letters
def turn_to_ascii(listofchars):
    asciitext = []
    for charecter in listofchars:
        asciitext.append(ord(charecter))
    return asciitext

# Makes the contents of a list letters
def turn_to_char(listofascii):
    #turning the numbers back into letters
    asciitext = []
    for number in range(0,len(listofascii)):
        asciitext.append(chr(listofascii[number]))
    return asciitext

def make_equal_length(word, key):
    while len(word) > len(key):
       key += key
    while len(word) < len(key):
        key = key[:len(key)-1]
    return key

def main():
    print(encrypt_caesar("PYTHON", 3))
    print(decrypt_caesar(encrypt_caesar("PYTHON", 3), 3))
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
    print(decrypt_vigenere(encrypt_vigenere("ATTACKATDAWN", "LEMON"),"LEMON"))   
    print(generate_private_key())
    pass

if __name__ == "__main__":
    main()
    