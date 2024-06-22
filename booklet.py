import PyPDF2
from PyPDF2 import PdfReader, PdfWriter, PageObject
import argparse

def create_booklet(input_pdf_path, output_pdf_path):
    # Leer el PDF original
    input_pdf = PdfReader(input_pdf_path)
    num_pages = len(input_pdf.pages)
    
    # Calcular el número de páginas adicionales necesarias
    additional_pages = num_pages % 4 
    
    # Crear un nuevo archivo PDF
    output_pdf = PdfWriter()
    
    # Obtener el tamaño de la primera página
    first_page = input_pdf.pages[0]
    width = first_page.mediabox.width
    height = first_page.mediabox.height
    
    # Recalcular el número total de páginas
    total_pages = num_pages + additional_pages
    
    # Reordenar las páginas para el booklet
    booklet_order = []
    for i in range(int(total_pages / 4)):
        booklet_order.append(total_pages - 1 - i * 2)
        booklet_order.append(i * 2)
        booklet_order.append(i * 2 + 1)
        booklet_order.append(total_pages - 2 - i * 2)
    
    # Añadir las páginas reordenadas al nuevo archivo PDF
    for page_num in booklet_order:
        if page_num < num_pages:
            output_pdf.add_page(input_pdf.pages[page_num])
        else:
            blank_page = PageObject.create_blank_page(width=width, height=height)
            output_pdf.add_page(blank_page)
    
    # Escribir el nuevo PDF
    with open(output_pdf_path, 'wb') as output_file:
        output_pdf.write(output_file)

if __name__ == "__main__":
    # Configurar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Crear un booklet a partir de un archivo PDF.")
    parser.add_argument("input_pdf_path", help="Ruta del archivo PDF de entrada")
    parser.add_argument("output_pdf_path", help="Ruta del archivo PDF de salida")
    
    args = parser.parse_args()
    
    # Crear el booklet
    create_booklet(args.input_pdf_path, args.output_pdf_path)

