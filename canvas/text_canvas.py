from canvas.object_canva import ObjectCanva
from canvas.object_canva import ElementCanva
from canvas.object_canva import GroupElementCanva

class TextCanvas(ElementCanva):
    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)
        self.__font_name = ""
        self.__font_size = 10
        self.__bold = False
        self.__italic = False
        self.__font_color = (0,0,0)
        self.__text = ""
    
    @property
    def font_name(self)->str:
        return self.__font_name
    @font_name.setter
    def font_name(self, value: str):
        self.__font_name = value
    
    @property
    def font_size(self)->int:
        return self.__font_size
    @font_size.setter
    def font_size(self, value: int):
        self.__font_size = value
    
    @property
    def bold(self):
        return self.__bold
    @bold.setter
    def bold(self, value):
        self.__bold = value
    
    @property
    def italic(self):
        return self.__italic
    @italic.setter
    def italic(self, value):
        self.__italic = value
    
    @property
    def font_color(self):
        return self.__font_color
    @font_color.setter
    def font_color(self, value):
        self.__font_color = value
    
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, value):
        self.__text = value
    
    @property
    def shift_left(self)->int:
        return 0
    

class CenterTextCanvas(TextCanvas):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)
    
    @property
    def shift_left(self)->int:
        return int(self.width / 2)


class GroupTextCanvas(GroupElementCanva):

    def __init__(self, name: str, parent: ObjectCanva=None):
        super().__init__(name, parent)
    
    @property
    def shift_left(self)->int:
        return 0

    @property
    def grp_width(self)->int:
        max_width = 0
        for _, element in self.elements.items():
            max_width = max_width if max_width > element.width else element.width
        return max_width
    
class CenterGroupTextCanvas(GroupElementCanva):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)
    
    @property
    def shift_left(self)->int:
        return int(self.width / 2)    
    