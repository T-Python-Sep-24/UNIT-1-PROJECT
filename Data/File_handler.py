import pickle
import os
class Data_management:
    def save_file(obj,file_name):
        file_path=os.path.join('Data',file_name)
        with open (file_path,'wb')as file:
            pickle.dump(obj,file)

    def load_file(file_name):
        file_path=os.path.join('Data',file_name)
        if os.path.exists(file_path):
            with open(file_path,'rb')as file:
                return pickle.load(file)
        else:
            return {}
