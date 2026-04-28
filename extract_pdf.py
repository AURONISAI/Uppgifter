import fitz
import easyocr
import os
import numpy as np
from PIL import Image

pdf_path = r'matematik-2\Öva_ Räta linjens ekvation - Omniway.pdf'
output_path = r'matematik-2\ova_rata_full_extract.txt'

def extract_content():
    reader = easyocr.Reader(['sv', 'en'])
    doc = fitz.open(pdf_path)
    full_text = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # 1. Embedded text
        embedded_text = page.get_text()
        full_text.append(f"--- Page {page_num + 1} (Embedded) ---\n")
        full_text.append(embedded_text)
        
        # 2. OCR text
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # Higher resolution
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_np = np.array(img)
        
        ocr_result = reader.readtext(img_np, detail=0)
        ocr_text = "\n".join(ocr_result)
        
        full_text.append(f"\n--- Page {page_num + 1} (OCR) ---\n")
        full_text.append(ocr_text)
        full_text.append("\n\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(full_text))
    
    # Print excerpts for the user
    text_content = "".join(full_text)
    print("EXTRACT_START")
    # Show more of the file content in sections to ensure we see the rest
    print(text_content)
    print("EXTRACT_END")

if __name__ == '__main__':
    extract_content()
