import os

class MainModel:
    def __init__(self):
        self.images_src_files: list = self.get_images_src_files()
        self.images_dest_files: list = self.get_images_dest_files()

    def get_images_src_files(self) -> list:
        """ method returns Images_Source files as a list. Execlude instructions.txt & DS_Store """
        self.images_src_files: list = os.listdir("./Images_Source")
        
        try:
            self.images_src_files.remove("instructions.txt")
        except ValueError:
            pass

        try:
            self.images_src_files.remove(".DS_Store")
        except ValueError:
            pass

        return self.images_src_files

    def get_images_dest_files(self) -> list:
        """ method returns Images_Destination files as a list. Execlude instructions.txt & DS_Store """
        self.images_dest_files: list = os.listdir("./Images_Destination")
        
        try:
            self.images_dest_files.remove("instructions.txt")
        except ValueError:
            pass
        
        try:
            self.images_dest_files.remove(".DS_Store")
        except ValueError:
            pass
        return self.images_dest_files
    
    

