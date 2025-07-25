import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('E:/sample_ship.jpg')  # Đổi bằng ảnh thật của bạn
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray, config='--psm 6')
print("OCR result:", text)
