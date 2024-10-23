import face_recognition

import os
import shutil

from models import main_model as m_m


class FaceRecognizerModel(m_m.MainModel):
    def __init__(self):
        super().__init__()

    def check_many_faces(self, pick: str) -> list:
        img_index: int = int(pick) - 1
        img_name: str = self.images_src_files[img_index]
        img_path: str = os.path.join("Images_Source", img_name)

        # load image and get the list of how many faces location
        picked_image = face_recognition.load_image_file(img_path)
        face_location = face_recognition.face_locations(picked_image)    

        if len(face_location) == 1:
            return [False, img_path]
        else:
            return [True, "wrong image"]

    def copy_mathced_images(self, folder_name: str, img_path: str):
        pass
        # create the folder
        folder_path: str = os.path.join("Images_Destination", folder_name)
        os.makedirs(folder_path)

        known_image = face_recognition.load_image_file(img_path)
        known_encoding = face_recognition.face_encodings(known_image)[0]

        for img in self.images_src_files:
            unknown_img_path = os.path.join("Images_Source", img)

            unknown_image = face_recognition.load_image_file(unknown_img_path)
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            result = face_recognition.compare_faces([known_encoding], unknown_encoding)

            # copy the matched faces to the destination folder
            if result[0]:
                shutil.copy2(unknown_img_path, folder_path)
