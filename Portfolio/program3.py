"""question 1 [Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before]"""

def greeting():
    name = input("Please enter your name: ").strip()  #Remove any extra whitespace
    if not name:  #Check if the input is empty
        print("Hello, Stranger!")
    else:
        print(f"Hello, {name}!")

#Call the function to run the program
greeting()

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 2 Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''

def password_setup():
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the new password: ")
    
    if password1 == password2:
        print("Password Set!")
    else:
        print("Error: Passwords do not match. Please try again.")

#Call the function to run the program
password_setup()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

''' question 3 Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

def password_setup():
    password1 = input("Enter a new password (8-12 characters): ")
    
#Check if the password length is valid
    if not (8 <= len(password1) <= 12):
        print("Error: Password must be between 8 and 12 characters. Please try again.")
        return #Exit the function if the password is invalid
    
    password2 = input("Re-enter the new password: ")
    
#Check if the two passwords match
    if password1 == password2:
        print("Password Set!")
    else:
        print("Error: Passwords do not match. Please try again.")

#Call the function to run the program
password_setup()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 4 Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

def password_setup():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    
    password1 = input("Enter a new password (8-12 characters): ")
    
#Check if the password length is valid
    if not (8 <= len(password1) <= 12):
        print("Error: Password must be between 8 and 12 characters. Please try again.")
        return  #Exit the function if the password is invalid
    
#Check if the password is in the list of bad passwords
    if password1.lower() in BAD_PASSWORDS:  #Convert to lowercase for case-insensitivity
        print("Error: The chosen password is too common. Please choose a more secure password.")
        return  #Exit the function if the password is in the bad passwords list
    
    password2 = input("Re-enter the new password: ")
    
#Check if the two passwords match
    if password1 == password2:
        print("Password Set!")
    else:
        print("Error: Passwords do not match. Please try again.")

#Call the function to run the program
password_setup()

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 5 Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

def password_setup():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    
    while True:
        password1 = input("Enter a new password (8-12 characters): ")
        
        #Check if the password length is valid
        if not (8 <= len(password1) <= 12):
            print("Error: Password must be between 8 and 12 characters. Please try again.")
            continue  #Restart the loop if the length check fails
        
        #Check if the password is in the list of bad passwords
        if password1.lower() in BAD_PASSWORDS:  # Convert to lowercase for case-insensitivity
            print("Error: The chosen password is too common. Please choose a more secure password.")
            continue  #Restart the loop if the password is in the bad passwords list
        
        password2 = input("Re-enter the new password: ")
        
#Check if the two passwords match
        if password1 == password2:
            print("Password Set!")
            break  #Exit the loop if the passwords match
        else:
            print("Error: Passwords do not match. Please try again.")
            continue  #Restart the loop if the passwords do not match

#Call the function to run the program
password_setup()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 6 Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on.'''

def seven_times_table():
    for i in range(13):  #Loop from 0 to 12 inclusive
        print(f"{i} x 7 = {i * 7}")

#Call the function to run the program
seven_times_table()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 7 Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.'''

def times_table():
    while True:
        try:
            table_number = int(input("Enter the number for the times table (0-12): "))
            if 0 <= table_number <= 12:
                break
            else:
                print("Error: Please enter a number between 0 and 12.")
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    for i in range(13):  #Loop from 0 to 12 inclusive
        print(f"{i} x {table_number} = {i * table_number}")

#Call the function to run the program
times_table()

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 8 Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".'''

def times_table():
    while True:
        try:
            table_number = int(input("Enter the number for the times table (0-12 or negative for reverse): "))
            
#Check if the absolute value of the number is within range
            if -12 <= table_number <= 12:
                break
            else:
                print("Error: Please enter a number between -12 and 12.")
        except ValueError:
            print("Error: Please enter a valid integer.")
    
#Determine the order of the loop based on positive or negative input
    if table_number >= 0:
        for i in range(13):  #Forward loop from 0 to 12
            print(f"{i} x {table_number} = {i * table_number}")
    else:
        for i in range(12, -1, -1):  # Reverse loop from 12 to 0
            print(f"{i} x {-table_number} = {i * -table_number}")

#Call the function to run the program
times_table()











