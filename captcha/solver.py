from pytesseract import pytesseract
from PIL import Image

def solve_captcha(captcha_path):
    image = Image.open(captcha_path)
    text = pytesseract.image_to_string(image)
    return text.strip()
