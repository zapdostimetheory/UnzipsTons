import zipfile
import os

def unzipFiles(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(destination_folder)

source_folder = ''
#You would put the folder where all the .zip files are located here. Ex: 'D:/Program Files/etc/'
destination_folder = ''
#This is the destination folder where all the contents of the .zip files will be located. Ex: 'D:/Steam/'

if not os.path.exists(destination_folder): 
    os.makedirs(destination_folder)
#I added this in the event I add functionality to accept input to name source/destination folders. 
#If the destination directory doesn't exist, it adds it.

unzipFiles(source_folder, destination_folder)
#Run it
