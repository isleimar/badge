import csv

class BadgePage():
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__width = 0
        self.__height = 0        
        self.__formating = []        
        pass

    @property
    def name(self)->str:
        return self.__name
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def width(self)->int:
        return self.__width
    @width.setter
    def width(self, value: int):
        self.__width = value

    @property
    def height(self)->int:
        return self.__height
    @height.setter
    def height(self, value: int):
        self.__height = value    
    
    @property
    def page_size(self):
        return (self.width, self.height)
    
    @property
    def formatting(self)->str:
        return self.__formating
    @formatting.setter
    def formatting(self, value: str):
        self.__formating = value


class Badge:
    def __init__(self) -> None:
        self.__badge_pages = []
        self.__data = []
        pass    

    @property
    def badge_pages(self):
        return self.__badge_pages
    @badge_pages.setter
    def badge_pages(self, value):
        self.__badge_pages = value
    
    @property
    def data(self):
        return self.__data
    
    def inser_page(self, page: BadgePage):
        self.__badge_pages.append(page)
    
    def read_data(self, file_name):
        data = []
        with open(file_name, 'r', newline='', encoding='utf-8') as csv_file:
            read_csv = csv.DictReader(csv_file)
            for line in read_csv:            
                data.append(line)
        self.__data = data

    def create_badge(self, pdf_file_name):
        pass