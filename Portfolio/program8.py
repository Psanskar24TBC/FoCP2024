'''Question 1 The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument.'''

import sys

def nl_command(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line}", end='')  #Print line number and line content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <filename>")
    else:
        filename = sys.argv[1]
        nl_command(filename)

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 2 The Unix diff command compares two files and reports the differences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)'''

import sys

def compare_files(file1, file2):
    try:
        # Open the first file and read its content
        with open(file1, 'r') as f1:
            content1 = f1.read()
        
        # Open the second file and read its content
        with open(file2, 'r') as f2:
            content2 = f2.read()

        # Compare the contents of the two files
        if content1 == content2:
            print("The files are the same.")
        else:
            print("The files are different.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_command.py <file1> <file2>")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        compare_files(file1, file2)


'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 3 The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string.'''

import sys

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')  #Print the matching line without an additional newline
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep_command.py <pattern> <filename>")
    else:
        pattern = sys.argv[1]
        filename = sys.argv[2]
        grep(pattern, filename)
        
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 4 The Unix wc command counts the number of lines, words, and characters in a file.
Write an implementation of this that takes a file name as a command-line
argument, and then prints the number of lines and characters.
Note: Linux (and Mac) users can use the "wc" command to check the results of their
implementation.'''

import sys

def wc_command(filename):
    try:
        with open(filename, 'r') as file:
            lines = 0
            characters = 0

            for line in file:
                lines += 1
                characters += len(line)

            print(f"Lines: {lines}")
            print(f"Characters: {characters}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc_command.py <filename>")
    else:
        filename = sys.argv[1]
        wc_command(filename)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''Question 5 The Unix spell command is a simple spell-checker. It prints out all the words in a
text file that are not found in a dictionary. Write and test an implementation of this,
that takes a file name as a command-line argument.
Note: You may want to simplify the program at first by testing with a text file that
does not contain any punctuation. A complete version should obviously be able to
handle normal files, with punctuation.
Another Note: You will need a list of valid words. Linux users will already have one
(probably in /usr/share/dict/words). It is more complicated, as usual, for
Windows users. Happily, there are several available on GitHub.'''

import sys
import string

def load_dictionary(dictionary_file):
    """Load valid words from a dictionary file into a set for fast lookup."""
    try:
        with open(dictionary_file, 'r') as file:
            dictionary = set(word.strip().lower() for word in file.readlines())
            print(f"Dictionary loaded with {len(dictionary)} words.")   #Debugging line
            return dictionary
    except FileNotFoundError:
        print(f"Error: The dictionary file '{dictionary_file}' was not found.")
        sys.exit(1)

def check_spelling(filename, dictionary):
    """Check the spelling of words in the provided file against the dictionary."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    #   Remove punctuation from the word and convert it to lowercase
                    cleaned_word = word.strip(string.punctuation).lower()
                    if cleaned_word and cleaned_word not in dictionary:
                        print(f"Misspelled word: {word} (cleaned: {cleaned_word})")     #\Debugging line
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell_command.py <dictionary_file> <text_file>")
    else:
        dictionary_file = sys.argv[1]
        text_file = sys.argv[2]
        dictionary = load_dictionary(dictionary_file)
        check_spelling(text_file, dictionary)


