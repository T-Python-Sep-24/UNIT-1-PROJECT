import face_recognition

from models import face_recognizer_model as f_m
from views import face_recognizer_view as f_v


class FaceRecognizerController():
    def __init__(self, face_rec_view: f_v.FaceRecognizerView, face_rec_model: f_m.FaceRecognizerModel):
        self.face_rec_view = face_rec_view
        self.face_rec_model = face_rec_model
    
    def orgnize_images_by_face_rec(self):
        images_dest_files: list = self.face_rec_model.get_images_dest_files()
        images_src_files: list = self.face_rec_model.get_images_src_files()
        if len(images_dest_files) > 0:
            # exit the method because the Images_Destination alread have contents
            self.face_rec_view.display_try_again_after_delete_dest()
            return
        elif len(images_src_files) < 1:
            self.face_rec_view.display_try_again_after_put_in_src()
            return
        else:
            while True:
                # show images list to pick a face from
                self.face_rec_view.display_face_rec_menu(images_src_files)
                
                while True:
                    try:
                        pick: int = input("Enter: ")
                        if pick.lower() == "q":
                            return
                        # check if enterd number can be used as list index
                        elif int(pick) <= len(images_src_files):
                            break
                    except:
                        pass

                have_many_faces: list = self.face_rec_model.check_many_faces(pick)

                # if image has many faces:
                if have_many_faces[0]:
                    self.face_rec_view.display_wrong_image()
                else:
                    while True:
                        try:
                            dest_folder_name: str = input("Type the of the folder to save images to: ")
                            if len(dest_folder_name) > 0:
                                break
                        except:
                            pass

                    img_path = have_many_faces[1]

                    self.face_rec_model.copy_mathced_images(dest_folder_name, img_path)
                    
                    return
