from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from badge import Badge

from pdf_canvas.pdf_file_canvas import PdfFileCanvas, PdfPageCanvas, PdfGroupElementCanvas, PdfCenterGroupElementCanvas
from pdf_canvas.pdf_texto import PdfTexto, PdfCenterTexto
from pdf_canvas.pdf_image import PdfImage

def create_image(page, element, data):
    name = element['name']
    image = PdfImage(name)
    source = element.get("source", None)
    value = element.get("value", "sem valor" if source is None else data.get(source,"Chave inválida"))
    image.file_name = value
    image.width, image.height = element.get("size",(10,10))
    image.origin = element.get("origin",(0,0))
    page.insert(image)
    print("Criar um imagem")

def create_texto(page, element, data):
    name = element['name']
    center = element.get("center", False)
    text = PdfCenterTexto(name) if center else PdfTexto(name) 
    source = element.get("source", None)
    value = element.get("value", "sem valor" if source is None else data.get(source,"Chave inválida"))
    text.text = value
    text.font_size = element['font_size']
    text.bold = element['bold']
    text.font_name = "OpenSans"
    text.origin= element['origin']
    page.insert(text)
    print("Criar um texto")

def create_group(page, element, data):
    name = element['name']
    center = element.get("center", False)
    group = PdfCenterGroupElementCanvas(name) if center else PdfGroupElementCanvas(name)
    group.origin = element['origin']
    for text in element['value']:
        create_texto(group, text, data)
    page.insert(group)
    print("Criar um grupo")



def create_page(badge_page, pdf: PdfFileCanvas, data):
    pdf_page = PdfPageCanvas(badge_page.name)    
    pdf.insert(pdf_page)
    pdf_page.set_page_size(badge_page.page_size)
    for element in badge_page.formatting:
        type_element = element["type"]
        if type_element == "image":
            create_image(pdf_page, element, data)
        elif type_element == "text":
            create_texto(pdf_page, element, data)
        elif type_element == "group":
            create_group(pdf_page, element, data)
    pass
    pdf_page.draw()
    

def create_pdf_file(file_name, badge: Badge):
    pdf = PdfFileCanvas(file_name)
    for data in badge.data:        
        for badge_page in badge.badge_pages:
            create_page(badge_page, pdf, data)
    pdf.save()
    