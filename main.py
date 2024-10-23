# import local modules
from controllers import deleter_controller as d_c
from controllers import face_recognizer_controller as f_c
from controllers import main_controller as m_c
from controllers import orgnizer_controller as o_c
from models import deleter_model as d_m
from models import face_recognizer_model as f_m
from models import orgnizer_model as o_m
from views import deleter_view as d_v
from views import face_recognizer_view as f_v
from views import orgnizer_view as o_v
from views import main_view as m_v

# create instances of MainView, MainController
main_view = m_v.MainView()
main_controller = m_c.MainController(main_view)

# creat instances of OrgnizerModel, OrgnizerView, OrgnizerController
orgnizer_model = o_m.OrgnizerModel()
orgnizer_view = o_v.OrgnizerView()
orgnizer_controller = o_c.OrgnizerController(orgnizer_view, orgnizer_model)

# creat instances of FaceRecognizerModel, FaceRecognizerView, FaceRecognizerController
face_recognizer_model = f_m.FaceRecognizerModel()
face_recognizer_view = f_v.FaceRecognizerView()
face_recognizer_controller = f_c.FaceRecognizerController(face_recognizer_view, face_recognizer_model)

# creat instances of OrgnizerModel, OrgnizerView, OrgnizerController
deleter_model = d_m.DeleterModel()
deleter_view = d_v.DeleterView()
deleter_controller = d_c.DeleterController(deleter_view, deleter_model)

while True:
    main_controller.show_menu()
    pick: int = input("Enter: ")
    print()

    if pick == "1":
        main_controller.display_source()
    elif pick == "2":
        main_controller.display_destination()
    elif pick == "3":
        orgnizer_controller.orgnize_images_by_year()
    elif pick == "4":
        orgnizer_controller.orgnize_images_by_month()
    elif pick == "5":
        face_recognizer_controller.orgnize_images_by_face_rec()
    elif pick == "6":
        deleter_controller.delete_destination_contents()
    elif pick == "7":
        main_controller.display_thanks()
        break
    else:
        main_controller.display_wrong_input()
                



