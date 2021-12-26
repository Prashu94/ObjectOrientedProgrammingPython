"""The Python Script will demonstrate the composition method to process different files
Here the processor is composed in the ZipReplace class.
"""

import os
import shutil
import sys
import zipfile
from pathlib import Path
from PIL import Image


class ZipProcessor:
    """Main Class will be inherited by various other classes."""
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:4]}")
        self.processor = processor

    def process_zip(self):
        # Unzip Files
        self.unzip_files()
        # Process the given files
        self.processor.process_files(self)
        # Zip the files
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(self.temp_directory)

    def zip_files(self):
        with zipfile.ZipFile(self.zipname,"w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)


class ZipReplace:
    """The ZipReplace will help in processing the replacing
    of files in a zip file with the required names. This class
    will extend the functionality in the ZipProcessor class
    - basically for unzip files and zip files"""
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self, zipprocessor):
        """Perform a search and replace all files in the
        temporary directory"""
        for filename in zipprocessor.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()

            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)


class ScaleZip(ZipProcessor):
    def process_files(self):
        """Scale each image in the directory to 640x4880"""
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(filename)


if __name__=="__main__":
    #ScaleZip(*sys.argv[1:4]).process_zip()
    zipreplace = ZipReplace(*sys.argv[2:4])
    ZipProcessor(sys.argv[1], zipreplace).process_zip()