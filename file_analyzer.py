import argparse
import os
from docx import Document
import PyPDF2

def analyze_text(content):
    num_lines = content.count('\n') + 1
    num_words = len(content.split())
    num_chars = len(content)
    return num_lines, num_words, num_chars

def read_txt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def read_docx_file(filepath):
    doc = Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def read_pdf_file(filepath):
    content = ""
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content += page.extract_text() or ""
    return content

def main():
    parser = argparse.ArgumentParser(description='Analyze a text file.')
    parser.add_argument("filepath", help="Path to the text file.")
    args = parser.parse_args()
    
    filepath = args.filepath
    ext = os.path.splitext(filepath)[1].lower()
    
    try:
        if ext in ['.txt', '.html']:
            content = read_txt_file(filepath)
        elif ext == '.docx':
            content = read_docx_file(filepath)
        elif ext == '.pdf':
            content = read_pdf_file(filepath)
        else:
            print(f"Unsupported file type: {ext}")
            return

        num_lines, num_words, num_chars = analyze_text(content)

        print(f"\nAnalysis of '{os.path.basename(filepath)}':")
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")
            
    except FileNotFoundError:
        print(f"Error: File '{args.filepath}' not found.")
    except Exception as e:
        print(f"An error occurred:  {e}")

if __name__ == "__main__":
    main()