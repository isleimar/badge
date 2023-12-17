from canvas.object_canva import ObjectCanva
from canvas.text_canvas import TextCanvas

class PdfTexto(TextCanvas):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)

    def __format(self):
        font_name = self.__get_font_name()
        print(font_name)
        self.pdf.setFont(font_name, self.font_size)        
    
    def __get_font_name(self):
        return (self.font_name) + \
            ("-Bold" if self.bold else "") + \
            ("-Oblique" if self.italic else "")
    
    @property
    def pdf(self):
        return self.parent.pdf
    
    @property
    def width(self):        
        return self.pdf.stringWidth(self.text, self.__get_font_name(), self.font_size)
    
    @property
    def height(self):
        return self.pdf.stringHeight(self.text, self.__get_font_name(), self.font_size)

    def draw(self):
        x , y = self.abs_origin
        self.__format()
        self.pdf.drawString(x - self.shift_left, y, self.text)
        pass


class PdfCenterTexto(PdfTexto):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)

    @property
    def shift_left(self):
        return int(self.width / 2)
   
    