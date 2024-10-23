from views import main_view as m_v


# define FaceRecognizerView as a subclass of MainView
class FaceRecognizerView(m_v.MainView):
    def __init__(self):
        super().__init__()

    def display_face_rec_menu(self, image_files: list):
        print("\nPick an image contains only one face:")
        for index, img in enumerate(image_files, 1):
            print(f"{index}: {img}")
        print()

    def display_wrong_image(self):
        print("\n")
        print(f"---- The image you picked doesn't fit the critera ----")
        input("")
