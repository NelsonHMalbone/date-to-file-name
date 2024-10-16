import os
from datetime import datetime

# the directory aka the folder to get files from
directory = 'files_project'

# getting a list of the dir from the directory variable
filepath = os.listdir(directory)
# ran a test to see if sys can see the files inside dic
#print(filepath)


for filename in filepath:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as file:
        # read content inside each file
        content = file.read()
        # print(content)

    day = datetime.now().strftime('%Y-%m-%d')
    # test to see if it prints out the yyyy-mm-dd
    #print(day)

    # create new file name
    new_filedate_name = f'{filename[:-4]}-{day}.txt'
    #print(new_filedate_name)

