''' Question 1 Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''


def valid_integer(value):

    return 0 <= value <= 100

#Short program to test the function
def test_valid_integer():
    try:
        user_input = int(input("Enter an integer to check if it is in the range 0 to 100: "))
        result = valid_integer(user_input)
        print(f"Is {user_input} in the range 0 to 100? {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#Run the test
test_valid_integer()

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

''' Question 2 Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.'''

def case_letters(input_string):
    
    """Counts the number of uppercase and lowercase letters in a string."""

    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())
    return uppercase_count, lowercase_count

def test_case_letters():
    test_string = input("Enter a string to analyze: ")
    uppercase, lowercase =case_letters(test_string)
    print(f"The string contains {uppercase} uppercase letters and {lowercase} lowercase letters.")

#Calling Function
test_case_letters()

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 3 Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''


#Greetings program with name formatting
def greetings():
#Prompt the user to enter their name
    name = input("Enter your name: ")
    
#Format the name: first letter uppercase, the rest lowercase
    formatted_name = name.capitalize()
    
#Display the greeting with the formatted name
    print(f"Hello, {formatted_name}! Welcome!")

#Run the greetings function
greetings()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 4 When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)'''

#Function to remove the last character from a string
def remove_last_char(input_string):
#Check if the string has more than one character
    if len(input_string) > 1:
#Return the string without the last character
        return input_string[:-1]
#If the string has one or fewer characters, return it unchanged
    return input_string

test_string = input("Enter a String: ")

#Call the function directly on the input
modified_string = remove_last_char(test_string)
print(f"Original: '{test_string}' -> Modified: '{modified_string}'")

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''question 5 Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).'''

#Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def test_temperature_conversion():
#Test Celsius to Fahrenheit
    celsius_values = [-40, 0, 37, 100]
    print("Celsius to Fahrenheit:")
    for c in celsius_values:
        print(f"{c}°C -> {celsius_to_fahrenheit(c):.2f}°F")
    
#Test Fahrenheit to Celsius
    fahrenheit_values = [-40, 32, 98.6, 212]
    print("\nFahrenheit to Celsius:")
    for f in fahrenheit_values:
        print(f"{f}°F -> {fahrenheit_to_celsius(f):.2f}°C")
        
# Calling Function
test_temperature_conversion()

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 6 Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.'''

#Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#Main program
def convert_temperature():
#Prompt the user for input
    input_temperature = input("Enter a temperature in Centigrade (e.g., 25C): ").strip()
    
#Check if the input ends with 'C' or 'c'
    if input_temperature[-1].upper() == 'C':
        try:
#Extract the numeric part and convert to float
            celsius = float(input_temperature[:-1])
            
#Convert to Fahrenheit
            fahrenheit = celsius_to_fahrenheit(celsius)
            
#Display the result
            print(f"{celsius}C is equivalent to {fahrenheit:.1f}F")
        except ValueError:
            print("Invalid input! Please enter a valid number followed by 'C'.")
    else:
        print("Invalid format! Make sure the input ends with 'C'.")


convert_temperature()

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 7 Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.'''

#Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#Function to calculate the mean of a list of numbers
def calculate_mean(temperatures):
    return sum(temperatures) / len(temperatures)

#Main program
def convert_and_process_temperatures():
    temperatures = []
    
#Read 6 temperatures
    print("Enter 6 temperatures in Centigrade (e.g., 25C):")
    for _ in range(6):
        input_temperature = input().strip()
        
#Check if the input ends with 'C' or 'c'
        if input_temperature[-1].upper() == 'C':
            try:
#Extract the numeric part and convert to float
                celsius = float(input_temperature[:-1])
                
#Convert to Fahrenheit and add to the list
                fahrenheit = celsius_to_fahrenheit(celsius)
                temperatures.append(fahrenheit)
            except ValueError:
                print("Invalid input! Please enter a valid number followed by 'C'.")
                return
        else:
            print("Invalid format! Make sure the input ends with 'C'.")
            return
    
#Calculate max, min, and mean
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = calculate_mean(temperatures)
    
#Display the results
    print(f"\nMaximum temperature: {max_temp:.1f}F")
    print(f"Minimum temperature: {min_temp:.1f}F")
    print(f"Mean temperature: {mean_temp:.1f}F")

#Run the program
convert_and_process_temperatures()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 8 Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.'''

#Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#Function to calculate the mean of a list of numbers
def calculate_mean(temperatures):
    return sum(temperatures) / len(temperatures)

#Main program
def convert_and_process_temperatures():
    temperatures = []
    
#Read temperatures until the user presses Enter without entering a value
    print("Enter temperatures in Centigrade (e.g., 25C). Press Enter without any input to finish:")
    
    while True:
        input_temperature = input().strip()
        
#If the input is empty, break the loop (user pressed Enter without input)
        if input_temperature == "":
            break
        
#Check if the input ends with 'C' or 'c'
        if input_temperature[-1].upper() == 'C':
            try:
#Extract the numeric part and convert to float
                celsius = float(input_temperature[:-1])
                
#Convert to Fahrenheit and add to the list
                fahrenheit = celsius_to_fahrenheit(celsius)
                temperatures.append(fahrenheit)
            except ValueError:
                print("Invalid input! Please enter a valid number followed by 'C'.")
        else:
            print("Invalid format! Make sure the input ends with 'C'.")
    
#Check if at least one temperature was entered
    if temperatures:
#Calculate max, min, and mean
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = calculate_mean(temperatures)
        
#Display the results
        print(f"\nMaximum temperature: {max_temp:.1f}F")
        print(f"Minimum temperature: {min_temp:.1f}F")
        print(f"Mean temperature: {mean_temp:.1f}F")
    else:
        print("No valid temperatures were entered.")


convert_and_process_temperatures()




