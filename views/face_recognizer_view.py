from views import main_view as m_v


# define FaceRecognizerView as a subclass of MainView
class FaceRecognizerView(m_v.MainView):
    def __init__(self):
        super().__init__()