import directory_tree

class MainView:
    def __init__(self):
        pass

    def display_menu(self):
        print("Pick: \n" +
          "1: to show tree structure of Original_images folder\n"+
          "2: to show tree structure of Result_images folder\n" +
          "3: to orgnize images by year\n" +
          "4: to ....\n" +
          "5: to exit")
        
    def display_tree(self, directory_path):
        directory_tree.display_tree(directory_path)
        input("")
    
