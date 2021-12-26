import sys
# utility functions for copying and archiving files and directory trees
import shutil
# Read and write zip files.
import zipfile
from pathlib import Path



class ZipReplace:

    def __init__(self, filename, search_string, replace_string):
        # Filename
        self.filename = filename
        # Search String
        self.search_string = search_string
        # Replace String
        self.replace_string = replace_string
        # Temporary Directory
        self.temp_directory = Path(f"unzipped-{filename}")

    # Manager method to do all the required 3 tasks
    def zip_find_replace(self):
        # Unzip files
        self.unzip_files()
        # Find Replace
        self.find_replace()
        # Zip Files
        self.zip_files()

    # Step1: Unzip Files
    def unzip_files(self):
        # make a directory
        self.temp_directory.mkdir()
        # for each file in the zip files extract into the current directory.
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(self.temp_directory)

    # Step 2: Find Replace the files in the unzipped files
    def find_replace(self):
        # Go through each directory recently created
        for filename in self.temp_directory.iterdir():
            # open each filename
            with filename.open() as file:
                contents = file.read()
            # replace each content of the file
            contents = contents.replace(self.search_string, self.replace_string)
            # Open each file and write the file
            with filename.open("w") as file:
                file.write(contents)

    # Step 3: Zip the files
    def zip_files(self):
        # read each file with write flag
        with zipfile.ZipFile(self.filename, "w") as file:
            # for each file in the temporary directory
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)

if __name__=='__main__':
    ZipReplace(*sys.argv[1:4]).zip_find_replace()




