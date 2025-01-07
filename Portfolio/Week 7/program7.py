'''Question 7 Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].'''

def unique_sorted_letters(string):
#Use a set to remove duplicates and then convert it to a sorted list
    unique_letters = sorted(set(string))
    return unique_letters

# Test the function
input_string = input("Enter a string: ")
result = unique_sorted_letters(input_string)
print(f"Sorted list of unique letters: {result}")

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 2 Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.'''

def letters_in_at_least_one(word1, word2):
    return sorted(set(word1) | set(word2))  # Union

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  #  Intersection

def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  #Symmetric difference
#Test the functions
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(f"Letters in at least one word: {letters_in_at_least_one(word1, word2)}")
print(f"Letters in both words: {letters_in_both(word1, word2)}")
print(f"Letters in either word but not both: {letters_in_either_but_not_both(word1, word2)}")

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 3 Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.'''

def manage_countries_and_capitals():
#Dictionary to store countries and their capitals
    countries_and_capitals = {}

    while True:
#Prompt the user for a country name
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip()

#Terminate the program if the user types 'exit'
        if country.lower() == 'exit':
            print("Exiting the program.")
            break

#Convert the country name to lowercase to handle case insensitivity
        country_lower = country.lower()

#Check if the capital for this country is already known
        if country_lower in countries_and_capitals:
            print(f"The capital city of {country} is {countries_and_capitals[country_lower]}.")
        else:
#Ask the user to input the capital if not known
            capital = input(f"Enter the capital city of {country}: ").strip()
            countries_and_capitals[country_lower] = capital  #Store the capital in the dictionary
            print(f"Got it! The capital city of {country} is now {capital}.")

manage_countries_and_capitals()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 4 One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.'''

from collections import Counter

def frequency_analysis(message):
 #Initialize an empty dictionary to store letter counts
    letter_counts = {}

#Loop through each character in the message
    for char in message.lower():
        if char.isalpha():  #  Consider only alphabetic characters
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

#Sort the dictionary by count (in descending order) and get the top 6
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:6]

#Display the results
    print("The six most common letters are:")
    for letter, count in sorted_letters:
        print(f"Letter: {letter.upper()}, Frequency: {count}")

#Test the function
message = input("Enter the encrypted message: ")
frequency_analysis(message)






