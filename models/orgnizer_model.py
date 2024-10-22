from models import main_model as m_m

# define OrgnizerModel as a subclass of MainModel
class OrgnizerModel(m_m.MainModel):
    def __init__(self):
        super().__init__()
        # create a dict to store tree stucture of images by date
        self.by_date_dict: dict = {}

    def get_orgnized_by_year(self) -> dict:
        """ method loops through Original_images then return a nested structured by year dict"""
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
    
    def get_orgnized_by_month(self) -> dict:
        """ method loops through Original_images then return a nested structured by year and months dict"""
        for img in self.original_images:
            # variabels to store the year and the month
            year: str = ""
            month: str = ""
            # counters to track the year and month starting indexes
            year_starting_index: int = 0
            month_starting_index: int = year_starting_index + 4
            for char in img:
                year_ending_index: int = year_starting_index + 4
                month_ending_index: int = month_starting_index + 2
                if char.isdecimal():
                    year = img[year_starting_index:year_ending_index]
                    month = img[month_starting_index:month_ending_index]
                    if year not in self.by_date_dict:
                        # add the year as key and the month dict with empty list as value 
                        self.by_date_dict[year] = {month: []}
                    elif month not in self.by_date_dict[year].keys():
                        self.by_date_dict[year][month] = []
                    # append the image name to the list inside of the month key
                    self.by_date_dict[year][month].append(img)
                    break
                year_starting_index += 1
                month_starting_index += 1
        return self.by_date_dict
