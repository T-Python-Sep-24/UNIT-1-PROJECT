import os

class MainModel:
    def __init__(self):
        # store the list of Images_Source folder inside the variable
        self.original_images: list = os.listdir("./Images_Source")
        # remove the instruction.txt from the list
        self.original_images.remove("instructions.txt")
