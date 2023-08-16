import fitz  # PyMuPDF
from PIL import Image

# Set the location and file name
pdf_location = r"path location"
pdf_name = "pdf name"

# Combine location and file name to create the full file path
pdf_file_path = f"{pdf_location}\\{pdf_name}"

def render_pdf_page(pdf_path, page_number):
    pdf_document = fitz.open(pdf_path)
    page = pdf_document[page_number]
    pix = page.get_pixmap()
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return image

# Example usage
page_number = 0
pdf_image = render_pdf_page(pdf_file_path, page_number)
pdf_image.show()
