import os
import shutil

from models import main_model as m_m


class DeleterModel(m_m.MainModel):
    def __init__(self):
        super().__init__()

    def clear_image_src_folder(self, folder_path: str) -> list:
        # define a bool that will be changed to True if an exception happen
        is_Exception: bool = False
        # define a list that will be returned to the controller
        result_list: list = [is_Exception, "success"]
        
        for item in self.get_images_src_files():
            item_path: str = os.path.join(folder_path, item)
            try:
                if os.path.isfile(item_path):
                    # remove the file
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    # remove the directory with all of its content
                    shutil.rmtree(item_path)
            except Exception as e:
                is_Exception = True
                list[1] = e

        return result_list
                
    def clear_image_dest_folder(self, folder_path: str) -> list:
        # define a bool that will be changed to True if an exception happen
        is_Exception: bool = False
        # define a list that will be returned to the controller
        result_list: list = [is_Exception, "success"]
        
        for item in self.get_images_dest_files():
            item_path: str = os.path.join(folder_path, item)
            try:
                if os.path.isfile(item_path):
                    # remove the file
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    # remove the directory with all of its content
                    shutil.rmtree(item_path)
            except Exception as e:
                is_Exception = True
                list[1] = e

        return result_list