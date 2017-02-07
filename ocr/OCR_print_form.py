from PIL import Image, ImageEnhance
import pytesseract


def to_gray_img(image):
    _gray_img = Image.new('L', image.size)
    _gray_data = []
    _raw_data = image.getdata()

    for rgb in _raw_data:
        value = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
        if value < 128:
            _gray_data.append(0)
        else:
            _gray_data.append(255)

    _gray_img.putdata(_gray_data)
    return _gray_img


raw_img = Image.open("words.tiff")
gray_img = to_gray_img(raw_img)

# raw_img = ImageEnhance.Contrast(raw_img).enhance(4)
# gray_img = ImageEnhance.Contrast(gray_img).enhance(4)

raw_code = pytesseract.image_to_string(raw_img)
gray_code = pytesseract.image_to_string(gray_img)
print("raw:", raw_code, "\ngray:", gray_code)
