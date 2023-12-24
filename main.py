# from pdf_canvas.pdf_file_canvas import PdfFileCanvas, PdfPageCanvas, PdfGroupElementCanvas, PdfCenterGroupElementCanvas
# from pdf_canvas.pdf_texto import PdfTexto, PdfCenterTexto

from badge import Badge, BadgePage

from pdf_badge import *


# tamanho das páginas
page_size = (153,242)

# formação das páginas
page1_formatting = [
        {"type": "image", "name": "front_background", "value": "images/cracha_frente.jpg", "origin": (0,0), "size": page_size},
        {"type": "group", "name": "first_last_name", "origin": (77,43), "center": True, "value": [
            {"type": "text", "name": "first_name", "source": "first_name", "origin":(0,0), "bold" : True, "font_size": 10},
            {"type": "text", "name": "last_name", "source": "last_name", "origin":(0,0), "bold" : False, "font_size": 10},
        ]},
        {"type": "text", "name": "gender", "source": "gender", "origin":(77,29), "center": True, "bold" : True, "italic": True, "font_size": 10},
        {"type": "image", "name": "photo_file", "source": "photo_file", "origin": (45.2,65.5), "size": (62.5, 82.7)},
    ]
page2_formatting = [
        {"type": "image", "name": "back_background", "value": "images/cracha_verso.jpg", "origin": (0,0), "size": page_size},
        {"type": "text", "name": "full_name", "source": "full_name", "origin":(25,145), "bold" : False, "font_size": 7},
        {"type": "text", "name": "office", "source": "office", "origin":(25,125), "bold" : False, "font_size": 7},
        {"type": "text", "name": "siape", "source": "siape", "origin":(24,104), "bold" : False, "font_size": 7},
        {"type": "group", "name": "blood_rh", "origin": (24,82), "value": [
            {"type": "text", "name": "blood_type", "source": "blood_type", "origin":(0,0), "bold" : False, "font_size": 7},
            {"type": "text", "name": "rh_factor", "source": "rh_factor", "origin":(0,0), "bold" : False, "font_size": 7},
        ]},        
        {"type": "text", "name": "e_mail", "source": "e_mail", "origin":(24,62), "bold" : False, "font_size": 7},
    ]


def main():
    badge = Badge()    
    badge.read_data("data/cracha.csv")

    page1 = BadgePage("page1")
    page1.width, page1.height  = page_size    
    page1.formatting = page1_formatting
    badge.inser_page(page1)

    page2 = BadgePage("page2")
    page2.width, page2.height = page_size    
    page2.formatting = page2_formatting
    badge.inser_page(page2)

    create_pdf_file("output/","photos/", badge)    
    pass

if __name__ == "__main__":
    main()






    # pdf = PdfFileCanvas('output/saida.pdf')
    # page = PdfPageCanvas("nada")
    # pdf.insert(page)
    # page.set_page_size((300,500))

    # text1 = PdfTexto("text1") 
    # text1.text = "Testo 1 "
    # text1.font_size = 12    
    # text1.italic = True
    # text1.font_name = "OpenSans"

    # text2 = PdfTexto("text2") 
    # text2.text = "Texto 2"
    # text2.font_size = 6    
    # text2.bold = True
    # text2.font_name = "OpenSans"

    # text3 = PdfTexto("text3") 
    # text3.text = "Texto 3"
    # text3.font_size = 32    
    # text3.bold = True
    # text3.italic = True
    # text3.font_name = "OpenSans"

    # text4 = PdfCenterTexto("text4") 
    # text4.text = "Isso  Texto 4"
    # text4.font_size = 32    
    # text4.bold = True
    # text4.italic = True
    # text4.font_name = "OpenSans"
    # text4.origin = (150,250)

    # grp = PdfCenterGroupElementCanvas("grupo")
    # grp.origin = (150,50)
    # print(grp.origin)
    # page.insert(grp)

    # grp.insert(text1)
    # grp.insert(text2)
    # grp.insert(text3)

    # page.insert(text4)

    # page.draw()
    # pdf.save()
 
    
    