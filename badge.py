import csv

class BadgePage():
    def __init__(self) -> None:
        self.__width = 0
        self.__height = 0
        self.__backgroud_file = ""
        self.__formating = []
        pass

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
    def backgroud_file(self)->str:
        return self.__backgroud_file
    @backgroud_file.setter
    def backgroud_file(self, value: str):
        self.__backgroud_file = value
    
    @property
    def formating(self)->str:
        return self.__formating
    @formating.setter
    def formating(self, value: str):
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