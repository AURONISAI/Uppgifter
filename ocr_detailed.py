import easyocr
import os
import PIL.Image

def ocr_and_print(index):
    try:
        reader = easyocr.Reader(['en', 'sv'])
        img_path = os.path.join('matematik-2', '_ocr_imgs', f'{index}.png')
        img = PIL.Image.open(img_path)
        # Use simple readtext first
        result = reader.readtext(img_path, detail=1)
        print(f"--- IMAGE {index} ---")
        for res in result:
             print(f"Box: {res[0]}, Text: {res[1]}, Conf: {res[2]}")
    except Exception as e:
        print(f"Error reading image {index}: {e}")

for i in range(1, 6):
    ocr_and_print(i)
