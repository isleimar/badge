
class ObjectCanva:
    def __init__(self, name: str):
        self.__name: str = name
        self.__origin = (0,0)
        self.__width = 0
        self.__height = 0
        pass

    @property
    def name(self)->str:
        return self.__name
    
    @property
    def x_origin(self)->float:
        return self.origin[0]
    
    @property
    def y_origin(self)->float:
        return self.origin[1]
    
    @property
    def origin(self):
        return self.__origin
    @origin.setter
    def origin(self, value):
        self.__origin = value
    
    @property
    def abs_origin(self):
        return self.origin
    
    @property
    def width(self)->float:
        return self.__width
    @width.setter
    def width(self, value: float):
        self.__width = value
    
    @property
    def rel_width(self)->float:
        return self.x_origin + self.width
    
    @property
    def height(self)->float:
        return self.__height
    @height.setter
    def height(self, value: float):
        self.__height = value
    
    @property
    def rel_height(self)->float:
        return self.y_origin + self.height

class ElementCanva(ObjectCanva):
    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name=name)
        self.__parent = parent
        pass

    @property
    def parent(self)->ObjectCanva:
        return self.__parent
    @parent.setter
    def parent(self, value: ObjectCanva):
        self.__parent = value

    @property
    def abs_origin(self):
        if self.parent is None:
            return self.origin
        x, y = self.origin
        px, py = self.parent.abs_origin
        return (x + px, y + py)  

class GroupElementCanva(ElementCanva):
    def __init__(self, name: str, parent: ObjectCanva=None):
        super().__init__(name=name, parent=parent)
        self.__elements = {}
        pass

    @property
    def elements(self):
        return self.__elements
    @elements.setter
    def elements(self, value):
        self.__elements = value
    
    @property
    def count(self)->int:
        return len(self.elements)
    
    def insert(self, element: ElementCanva):
        element.parent = self
        self.elements[element.name] = element
    
    @property
    def grp_width(self)->float:
        min_horizontal, max_horizontal = (0, super().width)        
        for _, element in self.elements.items():
            if min_horizontal is None:
                min_horizontal = element.x_origin
            else:
                min_horizontal = min_horizontal if (min_horizontal < element.x_origin) else element.x_origin
            if max_horizontal is None:
                max_horizontal = element.rel_width
            else:
                max_horizontal = max_horizontal if (max_horizontal > element.rel_width) else element.rel_width
        if ((min_horizontal is None) or (max_horizontal is None)):
            return 0
        return max_horizontal - min_horizontal    
    
    @property
    def grp_height(self)->float:
        min_vertical, max_vertical = (0, super().height)
        for _, element in self.elements.items():
            if min_vertical is None:
                min_vertical = element.y_origin
            else:
                min_vertical = min_vertical if (min_vertical < element.y_origin) else element.y_origin
            if max_vertical is None:
                max_vertical = element.rel_height
            else:
                max_vertical = max_vertical if (max_vertical > element.rel_height) else element.rel_height
        if ((min_vertical is None) or (max_vertical is None)):
            return 0
        return max_vertical - min_vertical