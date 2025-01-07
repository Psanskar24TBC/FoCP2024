'''Question 1 Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used.'''

import sys
import platform

#Check if the script was executed with command-line arguments
if len(sys.argv) == 1:
#Report the operating system platform
    print(f"Operating System Platform: {platform.system()}")
else:
    print("This program doesn't require command-line arguments.")
    
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

''' Question 2 Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).'''

import sys

#Report how many arguments were provided (excluding the script name)
num_arguments = len(sys.argv) - 1

#Print the result
print(f"Number of arguments provided: {num_arguments}")

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 3 Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''

import sys

#check that at least one argument is provided (excluding the script name)
if len(sys.argv) > 1:
#Sort the arguments based on their length
    shortest_argument = sorted(sys.argv[1:], key=len)[0]

#Print the shortest argument
    print(f"The shortest argument is: {shortest_argument}")
else:
    print("No arguments provided!")

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 4 Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.'''

import sys
import requests

#Check if a URL was provided
if len(sys.argv) != 2:
    print("Usage: python check_website.py <URL>")
    sys.exit(1)

#Get the URL from the command line argument
url = sys.argv[1]

try:
#Send a GET request to the URL
    response = requests.get(url)

#Check if the status code indicates success (200 OK)
    if response.status_code == 200:
        print(f"The website at {url} is working!")
    else:
        print(f"The website at {url} returned a {response.status_code} status code.")
except requests.exceptions.RequestException as e:
#If an error occurs (e.g., invalid URL, network issues)
    print(f"Error: {e}")

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 5 Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!'''

import sys

#Function to calculate the mean of a list of numbers
def calculate_mean(temperatures):
    return sum(temperatures) / len(temperatures)

#Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#Main program
def process_temperatures():
#Check if arguments are provided (excluding the script name)
    if len(sys.argv) < 2:
        print("No temperature values provided. Please provide temperatures in Celsius.")
        sys.exit(1)

    temperatures = []

#Process each temperature argument
    for arg in sys.argv[1:]:
        try:
#Convert each argument to a float (Celsius)
            celsius = float(arg)
            fahrenheit = celsius_to_fahrenheit(celsius)  # Convert to Fahrenheit
            temperatures.append(fahrenheit)
        except ValueError:
            print(f"Invalid temperature value: {arg}. Skipping.")
    
#If no valid temperatures were provided, exit the program
    if not temperatures:
        print("No valid temperature values were provided.")
        sys.exit(1)
    
#Calculate max, min, and mean
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = calculate_mean(temperatures)
    
#Print the results
    print(f"Maximum temperature: {max_temp:.1f}F")
    print(f"Minimum temperature: {min_temp:.1f}F")
    print(f"Mean temperature: {mean_temp:.1f}F")

process_temperatures()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

''''Question 6 Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.'''

import sys
import shutil
import os


def create_backup():
#Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python backup_file.py <filename>")
        sys.exit(1)

    original_file = sys.argv[1]

#Check if the file exists
    if not os.path.isfile(original_file):
        print(f"The file '{original_file}' does not exist.")
        sys.exit(1)

#Create a backup file name by appending '_backup' to the original file name
    backup_file = f"{os.path.splitext(original_file)[0]}_backup{os.path.splitext(original_file)[1]}"

#Copy the contents of the original file to the backup file
    shutil.copy(original_file, backup_file)

    print(f"Backup of '{original_file}' created as '{backup_file}'")


create_backup()





