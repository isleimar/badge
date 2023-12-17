from canvas.stage_canvas import StageCanvas
from canvas.object_canva import ElementCanva, GroupElementCanva, ObjectCanva

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# Registrar as fontes OpenSans-Bold e OpenSans-Italic
pdfmetrics.registerFont(TTFont('OpenSans', 'fonts/OpenSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('OpenSans-Bold', 'fonts/OpenSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('OpenSans-Oblique', 'fonts/OpenSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont('OpenSans-Bold-Oblique', 'fonts/OpenSans-BoldItalic.ttf'))
pdfmetrics.registerFontFamily('OpenSans',normal='OpenSans',bold='OpenSans-Bold',italic='OpenSans-Oblique',boldItalic='OpenSans-Bold-Oblique')


class PdfFileCanvas(StageCanvas):

    def __init__(self, file_name: str):
        super().__init__(file_name, None)        
        self.__pdf = canvas.Canvas(file_name)


    @property
    def file_name(self)-> str:
        return self.name
    
    @property
    def pdf(self)->canvas:
        return self.__pdf
    
    def save(self):
        self.pdf.save()

class PdfElementCanvas(ElementCanva):

    def __init__(self, name: str, parent: PdfFileCanvas = None):
        super().__init__(name, parent)
    
    def draw(self):
        pass

class PdfGroupElementCanvas(GroupElementCanva):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)

    @property
    def pdf(self):
        return None if self.parent is None else self.parent.pdf
    

    @property
    def grp_width(self)->int:
        width = 0
        for _, element in self.elements.items():
            width += element.width
        return width
    
    @property
    def shift_left(self):
        return 0
    
    def draw(self):
        shift = -self.shift_left
        for _, element in self.elements.items():
            ex, ey = element.origin
            element.origin = (ex + shift, ey)
            shift += element.width
            element.draw()


class PdfCenterGroupElementCanvas(PdfGroupElementCanvas):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)
    
    @property
    def shift_left(self):
        return int(self.grp_width / 2)


class PdfPageCanvas(PdfGroupElementCanvas):

    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)    
    
    def set_page_size(self, page_size):
        self.width, self.height = page_size
        self.pdf.setPageSize(page_size)

    def draw(self):        
        for _, element in self.elements.items():            
            element.draw()
        self.pdf.showPage()
        


    