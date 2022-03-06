import cv2
import numpy as np
import pytesseract


def load_image_text_first_copy(filepath, is_show_file):
    # pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    kernel = np.ones((5, 5), np.uint8)

    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    result = pytesseract.image_to_string(img)

    print(result)
    if is_show_file:
        cv2.imshow('Result', img)
    cv2.waitKey(0)

    return result
