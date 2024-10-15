# Udemy 10/15/2024
# tutorial Add Date to Filenames
import os
from datetime import datetime

# starting with the import to the output
# path should be in the same spot as file so no need for a "/"

directory = 'files'

# get the list of all files in directory
filenames = os.listdir(directory)

# processing the listdir with a for loop to count words in each file
for filename in filenames:
    filepath = os.path.join(directory, filename)
    # adding word count from each file
    with open(filepath, 'r') as file: # read thur all the files
        content = file.read()
        words = content.split() # spliting each word from content in file
        word_count = len(words) # getting total amount of words
        #print(word_count)

    # creating a new file name
    new_filename = f"{filename[:-4]}-{word_count}.txt"
    # [:-4] taking the last .txt out of the equation
    print(new_filename)