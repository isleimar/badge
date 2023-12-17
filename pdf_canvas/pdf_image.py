from pdf_canvas.pdf_file_canvas import PdfElementCanvas, PdfFileCanvas
from canvas.object_canva import ObjectCanva

class PdfImage(PdfElementCanvas):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)
        self.__file_name = ""
    
    @property
    def file_name(self)->str:
        return self.__file_name
    @file_name.setter
    def file_name(self, value: str):
        self.__file_name = value

    @property
    def pdf(self):
        return self.parent.pdf
    
    def draw(self):
        x , y = self.abs_origin        
        self.pdf.drawInlineImage(self.file_name, x, y, width=self.width, height=self.height)
        pass