'''Question 1 Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!'''

def to_binary(n):
#check the number is positive
    if n <= 0:
        return "Input must be a positive integer."
    
#Convert the integer to binary (removing the '0b' prefix)
    return bin(n)[2:]


number = 10  #Example number
print(f"The binary representation of {number} is: {to_binary(number)}")

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 2 Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

def find_factors(n):
#Ensure the number is a positive integer
    if n <= 0:
        return "Input must be a positive integer."
    
    factors = []
    
#Iterate over all numbers from 1 to n
    for i in range(1, n + 1):
        if n % i == 0:  # Check if i is a factor of n
            factors.append(i)
    
    return factors


number = 12  # Example number
print(f"The factors of {number} are: {find_factors(number)}")

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 3 Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers'''

import math

def is_prime(n):
#check the number is greater than 1 (prime numbers are greater than 1)
    if n <= 1:
        return False
    
#Check for divisibility from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If divisible by i, it is not a prime
            return False
    
    return True

#Take user input
try:
    number = int(input("Enter an integer: "))
    
#Check if the number is prime
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 4 Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.'''

def encrypt_message(message):
#Remove spaces and reverse the string
    return message.replace(" ", "")[::-1]

#Test the function
message = input("Enter a message to encrypt: ")
encrypted_message = encrypt_message(message)

print(f"Encrypted message: {encrypted_message}")

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 5 Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye'''

import random
import string

def encrypt_with_interval(message):
#Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
#Initialize an empty list for the encrypted message
    encrypted_message = []
    
#Loop through the message and add characters to the encrypted message
    for i in range(len(message)):
        if i % interval == 0:
            encrypted_message.append(message[i])  #Add the message character at the interval
        else:
            encrypted_message.append(random.choice(string.ascii_lowercase))  #Add a random letter
    
#Join the list into a string and return it with the interval
    return ''.join(encrypted_message), interval

#Test the function
message = input("Enter a message to encrypt: ")
encrypted_message, interval = encrypt_with_interval(message)

print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval}")



'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 6 Write a program that decrypts messages encoded as above.'''

import random
import string

def decrypt_with_interval(encrypted_message, interval):
#Initialize an empty string for the decrypted message
    decrypted_message = []
    
#Loop through the encrypted message, taking every `interval`-th character
    for i in range(len(encrypted_message)):
        if i % interval == 0:
            decrypted_message.append(encrypted_message[i])  # Only take the message character at the interval
    
#join the list into a string and return the decrypted message
    return ''.join(decrypted_message)

#Test the function
encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the interval used: "))

decrypted_message = decrypt_with_interval(encrypted_message, interval)

print(f"Decrypted message: {decrypted_message}")




















