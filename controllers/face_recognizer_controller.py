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
                pass
                # show images list to pick a face from

                # if image has many faces:
                    # display image has many faces. Please pick another image
                # else:
                    # type the folder_name:
                    # create the folder

                    # known_image = ...
                    # known_encoding = ....(known_image)[0]

                    # for img in images_src:
                        # unknown_image = ....
                        # unknown_encoding = ....(unkown_image)[0]

                        # result = compare(known_encoding, unknown_encoding)
                        # if result[0]:
                            # copy image to dest/folder_name
