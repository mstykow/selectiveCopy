# python3
# Program walks through current working directory tree and searches for files
# with a certain file extension (such as .pdf or .jpg). Copies these files
# from whatever location they are at to a user-specified subfolder of the cwd.

import shutil, os

# Prompt user for extension and destination folder.
extension = '.' + input('Enter a file extension, e.g., "pdf": ')
destFolder = input('Enter the destination folder name: ')
while os.path.isdir(destFolder):
    destFolder = input('Please enter a different folder name: ')

# Create the new folder.
absDestFolder = os.path.join(os.getcwd(),destFolder)
os.makedirs(absDestFolder)

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    if folderName == absDestFolder:
        continue
    for filename in filenames:
        # Only take filenames with the desired extension.
        if not filename.endswith(extension):
            continue
        # Check if currently processed filename already exists in destination
        # folder and modify filename if necessary.
        filenameCopy = filename
        i = 1
        while os.path.isfile(os.path.join(absDestFolder, filenameCopy)):
            filenameCopy = os.path.splitext(filenameCopy)[0] + '_' + str(i) + os.path.splitext(filenameCopy)[1]
            i += 1
        # Move currently processed file with possibly modified name.
        shutil.move(os.path.join(folderName, filename), os.path.join(absDestFolder, filenameCopy))
