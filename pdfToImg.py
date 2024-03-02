import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path, output_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Iterate over each page in the PDF
    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_number)
        
        # Render the page as a Pixmap
        pixmap = page.get_pixmap()
        
        # Save the Pixmap as a PNG image
        image_path = os.path.join(output_folder, f'page_{page_number + 1}.png')
        pixmap.save(image_path)
        
    # Close the PDF
    pdf_document.close()
    
# Example usage
pdf_path = "/home/shashank/Desktop/gitRepos/CRAFT-pytorch/Padilla - Nobleza virtuosa_testExtract.pdf"  # Path to your PDF file
output_folder = "/home/shashank/Desktop/gitRepos/CRAFT-pytorch/testFolder"  # Output folder to save the images
pdf_to_images(pdf_path, output_folder)
