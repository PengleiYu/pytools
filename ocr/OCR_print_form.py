from PIL import Image
import pytesseract

raw_img = Image.open("words.tiff")
gray_img = raw_img.convert("L")

# raw_img = ImageEnhance.Contrast(raw_img).enhance(4)
# gray_img = ImageEnhance.Contrast(gray_img).enhance(4)

raw_code = pytesseract.image_to_string(raw_img)
gray_code = pytesseract.image_to_string(gray_img)
print("raw:", raw_code, "\ngray:", gray_code)
