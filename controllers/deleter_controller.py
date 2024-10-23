from models import deleter_model as d_m
from views import deleter_view as d_v


class DeleterController:
    def __init__(self, deleter_view: d_v.DeleterView, deleter_model: d_m.DeleterModel):
        self.deleter_model = deleter_model
        self.deleter_view = deleter_view

    def delete_destination_contents(self):
        while True:
            self.deleter_view.show_delete_menu()
            pick: int = input("Enter: ")

            if pick == "1":
                # clear the Images_Source folder if it has contents
                images_src_files: list = self.deleter_model.get_images_src_files()
                if len(images_src_files) < 1:
                    # exit the method because the Images_Source doesn't have any content
                    self.deleter_view.display_folder_is_empty()
                    return
                else:
                    result = self.deleter_model.clear_image_src_folder("Images_Source")
                    if result[0]:
                        self.deleter_view.display_Exception_msg(result[1])
                    self.deleter_view.display_image_src_cleared()
                    return

            elif pick == "2":
                # clear the Images_Destination folder if it has contents
                images_dest_files: list = self.deleter_model.get_images_dest_files()
                if len(images_dest_files) < 1:
                    # exit the method because the Images_Destination doesn't have any content
                    self.deleter_view.display_folder_is_empty()
                    return
                else:
                    result = self.deleter_model.clear_image_dest_folder("Images_Destination")
                    if result[0]:
                        self.deleter_view.display_Exception_msg(result[1])
                    self.deleter_view.display_image_dest_cleared()
                    return

            elif pick == "3":
                return

            else:
                self.deleter_view.display_wrong_input()


            
