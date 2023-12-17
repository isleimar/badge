from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from badge import Badge

from pdf_canvas.pdf_file_canvas import PdfFileCanvas, PdfPageCanvas, PdfGroupElementCanvas, PdfCenterGroupElementCanvas
from pdf_canvas.pdf_texto import PdfTexto, PdfCenterTexto

def create_image(page, element):
    print("Criar uma imagem")

def create_texto(page, element):
    name = element['name']
    text = PdfCenterTexto(name)
    text.text = "Texto 2"
    text.font_size = 6    
    text.bold = True
    text.font_name = "OpenSans"
    page.insert(text)
    print("Criar um texto")

def create_group(page, element):
    print("Criar um grupo")



def create_page(badge_page, pdf: PdfFileCanvas):
    pdf_page = PdfPageCanvas(badge_page.name)    
    pdf.insert(pdf_page)
    pdf_page.set_page_size(badge_page.page_size)
    for element in badge_page.formatting:
        type_element = element["type"]
        if type_element == "image":
            create_image(pdf_page, element)
        elif type_element == "text":
            create_texto(pdf_page, element)
        elif type_element == "group":
            create_group(pdf_page, element)
    pass
    pdf_page.draw()
    

def create_pdf_file(file_name, badge: Badge):
    pdf = PdfFileCanvas(file_name)
    for badge_page in badge.badge_pages:
        create_page(badge_page, pdf)
    pdf.save()
    