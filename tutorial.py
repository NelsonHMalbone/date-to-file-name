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
    # get the current day
    #day = datetime.now() # cant use in new_filename need to convert to str
    day = datetime.now().strftime("%A")
    # creating a new file name
    new_filename = f"{filename[:-4]}-{word_count}-{day}.txt"
    # [:-4] taking the last .txt out of the equation
    # creating a new file path
    new_filepath = os.path.join(directory, new_filename)
    # now to run program to rename files
    # requires two args
    # old file path(filepath) to new filepath(new_filepath)
    os.rename(filepath, new_filepath)
    print(f"filepath converted from {filepath} to {new_filepath}")