from models import main_model as m_m

# define OrgnizerModel as a subclass of MainModel
class OrgnizerModel(m_m.MainModel):
    def __init__(self):
        super().__init__()
        # create a dict to store tree stucture of images by date
        self.by_date_dict: dict = {}

    def get_orgnized_by_date(self) -> dict:
        """ method loops through Original_images then return a nested structured by date dict"""
        for img in self.original_images:
            # a variabel to store the year 
            year: str = ""
            # a counter to track the year starting_index
            starting_index: int = 0
            for char in img:
                ending_index: int = starting_index + 4
                if char.isdecimal():
                    year = img[starting_index:ending_index]
                    if year not in self.by_date_dict:
                        # add the year as key and an empty list as value 
                        self.by_date_dict[year] = []
                    # append the image name to the list inside of the year key
                    self.by_date_dict[year].append(img)
                    break
                starting_index += 1
        return self.by_date_dict
