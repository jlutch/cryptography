####################################################
# Author: Jonathan Lutch
# Date: 9/27/2020
# Description: This program will encrypt and decrypt
# several types of ciphers. 
#####################################################
import random
import math

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    Z_value = 90
    A_value = 65
    length_of_alphabet = 26

    #checking to see if the message is empty
    if len(plaintext) == 0:
        return "Please enter something with a length greater than 0"

    #checking to see if the offset is empty
    if len(str(offset)) == 0:
        return "Please enter something with a length greater than 0 for the offset"
    
    #converting text into ascii charecters
    ascii_text = []
    for charecter in plaintext:
        ascii_text.append(ord(charecter))
    
    #shifting each ascii charecter
    for number in range(0, len(ascii_text)):
        if ascii_text[number] >= A_value and ascii_text[number] <= Z_value:
            ascii_text[number] += offset
            #checking if the ascii value is greater than z
            #if it is, we will adjust the value
            if ascii_text[number] > Z_value:
                ascii_text[number] -= length_of_alphabet

    #turning the numbers back into letters
    encrytped = []
    for number in ascii_text:
        encrytped.append(chr(number))
    
    #making string easy to read
    linker = ''
    return linker.join(encrytped)

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    Z_value = 90
    A_value = 65
    length_of_alphabet = 26

    #checking to see if the message is empty
    if len(ciphertext) == 0:
        return "Please enter something with a length greater than 0"

    #checking to see if the offset is empty
    if len(str(offset)) == 0:
        return "Please enter something with a length greater than 0 for the offset"
   
    #converting text into ascii charecters
    ascii_text = turn_to_ascii(ciphertext)
    
    #shifting each ascii charecter
    for number in range(0, len(ascii_text)):
        if ascii_text[number] >= A_value and ascii_text[number] <= Z_value:
            ascii_text[number] -= offset
            #checking if the ascii value is less than a
            #if it is, we will adjust the value
            if ascii_text[number] < A_value:
                ascii_text[number] += length_of_alphabet

    #turning the numbers back into letters
    encrytped = turn_to_char(ascii_text)
    
    #making string easy to read
    linker = ''
    return linker.join(encrytped)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    Z_value = 90
    A_value = 65
    length_of_alphabet = 26

    #checking to see if the message is empty
    if len(plaintext) == 0:
        return "Please enter something with a length greater than 0"
   
    #making the key an equal length
    keyword = make_equal_length(plaintext, keyword)
   
    ascii_text = turn_to_ascii(plaintext)
    keyword = turn_to_ascii(keyword)
    for x in range(0, len(ascii_text)):
        ascii_text[x] += keyword[x]-A_value
        #checking if the ascii value is greater than z
        #if it is, we will adjust the value
        if ascii_text[x] > Z_value:
            ascii_text[x] -= length_of_alphabet
   
    #turing numbers into letters
    ascii_text = turn_to_char(ascii_text)

    #making string easy to read
    linker = ''
    return linker.join(ascii_text)

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    A_value = 65
    length_of_alphabet = 26

    #checking to see if the message is empty
    if len(ciphertext) == 0:
        return "Please enter something with a length greater than 0"
   
    #making the key an equal length
    keyword = make_equal_length(ciphertext, keyword)

    ascii_text = turn_to_ascii(ciphertext)
    keyword = turn_to_ascii(keyword)
    #subtracting ascii values to do a negative shift
    for x in range(0, len(ascii_text)):
        ascii_text[x] -= keyword[x]-A_value
        if ascii_text[x] < A_value:
            ascii_text[x] += length_of_alphabet

    #turing numbers into letters
    ascii_text = turn_to_char(ascii_text)

    #making string easy to read
    linker = ''
    return linker.join(ascii_text)

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    total = 1000
    super_increasing_list = []
    while len(super_increasing_list) < n+1:
        newentry = random.randrange(1,total)  
        #making new entry bigger than the sum of the list
        while sum(super_increasing_list) >= newentry:
            newentry += random.randrange(1,total)
        super_increasing_list.append(newentry)
        total = sum(super_increasing_list)*2
     
    Q = super_increasing_list.pop()
    W = super_increasing_list
    
    #we now need to find R
    R = random.randrange(1,total)
    while math.gcd(R, Q) != 1:
        R = random.randrange(1,total)
    
    return tuple(W),Q,R

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    #isolating parts of the private key
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    B = []
    
    #finding list B
    for x in range(0,len(private_key[0])):
        B.append((R*W[x])%Q)
    return B

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    C_values = []
    
    #for charecters in the text
    for x in plaintext:  
        #turing the x into binary
        x = bin(ord(x))
        x = str(x[2:])
        #making the string 8 charecters long to avoid length errors
        x = x.zfill(8)
        
        
        total_value = 0
        #for each bit in the binary
        for entry in range(0, 8):
            #multiply the bit by the corresponding entry in the public 
            total_value += int(x[entry])*public_key[entry]
        C_values.append(total_value)
    
    return C_values

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    C_prime_values = []
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    
    #finding an x value that satisfies this equation
    for x in range(2,Q-1):
        if (R * x) % Q == 1:
            S = x
    
    #calculating Cprime
    for entry in range(0, len(ciphertext)):
        C_prime_values.append((ciphertext[entry] * S) % Q)
    
    ascii_text = []
    print(C_prime_values[0])
  
    #goes through all values of Cprime
    for num in range(0, len(C_prime_values)):
        possible_indices = []
        #for every index in W
        for i in range(0, len(W)):     
            if W[len(W) - i - 1] <= C_prime_values[num]:
                possible_indices.append(len(W) - i - 1)
                C_prime_values[num] -= W[len(W) - i - 1]
        ascii_text.append(calculate_binary_value(possible_indices))


    linker = ''
    return linker.join(turn_to_char(ascii_text))

# Makes the contents of a list letters
def turn_to_ascii(listofchars):
    ascii_text = []
    for charecter in listofchars:
        ascii_text.append(ord(charecter))
    return ascii_text

# Makes the contents of a list letters
def turn_to_char(listofascii):
    #turning the numbers back into letters
    ascii_text = []
    for number in range(0,len(listofascii)):
        ascii_text.append(chr(listofascii[number]))
    return ascii_text

def make_equal_length(word, key):
    while len(word) > len(key):
       key += key
    while len(word) < len(key):
        key = key[:len(key)-1]
    return key

def calculate_binary_value(values):
    total = 0
    length_of_binary_repersentation = 8
    base = 2
    for x in values:
        total += base ** (length_of_binary_repersentation - (x + 1))
    return total

def main():
  pass
    
    

if __name__ == "__main__":
    main()
    