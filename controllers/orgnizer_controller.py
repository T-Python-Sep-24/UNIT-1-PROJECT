import os
import shutil

from views import orgnizer_view as o_v
from models import orgnizer_model as o_m


class OrgnizerController:
    def __init__(self, orgnizer_view: o_v.OrgnizerView, orgnizer_model: o_m.OrgnizerModel):
        self.orgnizer_view = orgnizer_view
        self.orgnizer_model = orgnizer_model

    def orgnize_images_by_year(self):
        images_dest_files: list = self.orgnizer_model.get_images_dest_files()
        if len(images_dest_files) > 0:
            # exit the method because the Images_Destination alread have contents
            self.orgnizer_view.display_try_again_after_delete_dest()
            return
        else:
            by_year_dict: dict = self.orgnizer_model.get_orgnized_by_year()
            if len(by_year_dict) < 1:
                # display failure message because there is no images to copy
                self.orgnizer_view.display_orgniz_msg(False)
            else:
                # create the directories and copy the relevant images to it
                for year, img_list in by_year_dict.items():
                    # create the directory if not existed
                    try:
                        # use os.path.join() for better portability across operating systems
                        directory_path: str = os.path.join("Images_Destination", year)
                        os.mkdir(directory_path)
                    except FileExistsError:
                        self.orgnizer_view.display_file_exist_error_msg(year)
                    except Exception as e:
                        self.orgnizer_view.display_Exception_msg(e)

                    # loop through images then copy it to the aproprite destination folder
                    for img in img_list:
                        img_source = os.path.join("Images_Source", img)
                        img_destination = os.path.join("Images_Destination", year)
                        shutil.copy2(img_source, img_destination)

                self.orgnizer_view.display_orgniz_msg(True)

    def orgnize_images_by_month(self):
        images_dest_files: list = self.orgnizer_model.get_images_dest_files()
        if len(images_dest_files) > 0:
            # exit the method because the Images_Destination alread have contents
            self.orgnizer_view.display_try_again_after_delete_dest()
            return
        else:
            by_month_dict: dict = self.orgnizer_model.get_orgnized_by_month()
            if len(by_month_dict) < 1:
                # display failure message because there is no images to copy
                self.orgnizer_view.display_orgniz_msg(False)
            else:
                for year, month in by_month_dict.items():
                    for month_key, img_list in month.items():
                        # create the directory if not existed
                        try:
                            # use os.path.join() for better portability across operating systems
                            directory_path: str = os.path.join("Images_Destination", year, month_key)
                            os.makedirs(directory_path)
                        except FileExistsError:
                            self.orgnizer_view.display_file_exist_error_msg(year)
                        except Exception as e:
                            self.orgnizer_view.display_Exception_msg(e)

                        # loop through images then copy it to the aproprite destination folder
                        for img in img_list:
                            img_source = os.path.join("Images_Source", img)
                            img_destination = os.path.join("Images_Destination", year, month_key)
                            shutil.copy2(img_source, img_destination)

                self.orgnizer_view.display_orgniz_msg(True)                
