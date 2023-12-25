from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from badge import Badge

from pdf_canvas.pdf_file_canvas import PdfFileCanvas, PdfPageCanvas, PdfGroupElementCanvas, PdfCenterGroupElementCanvas, PdfLineGroupElementCanvas
from pdf_canvas.pdf_texto import PdfTexto, PdfCenterTexto
from pdf_canvas.pdf_image import PdfImage

def create_image(page, element, data):
    name = element['name']
    image = PdfImage(name)
    source = element.get("source", None)
    value = element.get("value", "sem valor" if source is None else data.get(source,"Chave inválida"))
    image.file_name = value
    image.width, image.height = element.get("size",(10.0,10.0))
    image.origin = element.get("origin",(0.0,0.0))
    page.insert(image)    

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
    text.font_color = element.get("font_color",(0,0,0))
    page.insert(text)

def create_group(page, elements, data):
    name = elements['name']
    center = elements.get("center", False)  
    line = elements.get("line", False)
    size = elements.get("size",(0,0))
    group = None
    if line:
        group = PdfLineGroupElementCanvas(name)
        group.width, group.height = size
    else:
        group = PdfCenterGroupElementCanvas(name) if center else PdfGroupElementCanvas(name)
    group.origin = elements['origin']
    for element in elements['value']:
        create_element(group, element, data)
    page.insert(group)

def create_element(page, element, data):
    type_element = element["type"]
    if type_element == "image":
        create_image(page, element, data)
    elif type_element == "text":
        create_texto(page, element, data)
    elif type_element == "group":
        create_group(page, element, data)    

def create_page(badge_page, pdf: PdfFileCanvas, data):
    pdf_page = PdfPageCanvas(badge_page.name)    
    pdf.insert(pdf_page)
    pdf_page.set_page_size(badge_page.page_size)
    for element in badge_page.formatting:
        create_element(pdf_page, element, data)        
    pass
    pdf_page.draw()
    

def create_pdf_file(output, photo_path, badge: Badge):
    for data in badge.data:
        id = data['id']
        full_name = data['full_name']
        siape = data['siape']
        file_name ="{}{}-{}.pdf".format(output,full_name,siape)
        pdf = PdfFileCanvas(file_name)
        data['photo_file'] = "{}{}.jpg".format(photo_path,data['id']) 
        for badge_page in badge.badge_pages:
            create_page(badge_page, pdf, data)
        pdf.save()
    