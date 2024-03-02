from docx import Document
import string

def remove_punctuation(text):
    # Define a translation table that maps punctuations to None
    translation_table = str.maketrans("", "", string.punctuation)
    # Remove punctuations using translate() method
    return text.translate(translation_table)

def save_pages_to_text(docx_file, output_folder):
    document = Document(docx_file)
    current_page = None
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if text.startswith("PDF p"):
            if current_page is not None:
                current_page.close()
            try:
                page_number = int(text.split()[-1].replace("p", ""))  # Extract page number from "PDF pX" pattern
                current_page = open(f"{output_folder}/PDF_p{page_number}.txt", "w")
            except ValueError:
                # If page number extraction fails, skip this paragraph
                continue
        elif current_page is not None:
            # Remove punctuations from the text before writing to the file
            text_without_punctuation = remove_punctuation(text)
            current_page.write(text_without_punctuation + "\n")

# Example usage:
docx_file = "/home/shashank/Desktop/gitRepos/CRAFT-pytorch/Padilla - 1 Nobleza virtuosa_testTranscription.docx"  # Replace with the path to your DOCX file
output_folder = "output"     # Folder where the text files will be saved
save_pages_to_text(docx_file, output_folder)
