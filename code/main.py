import sys
import json
import requests
import os
import os.path

import pytesseract

from docx import Document
from docx.shared import Pt  # Point font size

try:
    from PIL import Image
except ImportError:
    import Image

# example token
GOOGLE_API_TOKEN = ""

DIR = 'herman_hesse'  # input("Enter name of the folder with images of scanned book: ")

chosen_path = os.path.join(DIR)

if not os.path.isdir(chosen_path):
    sys.exit("No folder named {}, exiting.".format(DIR))

LANGUAGE_TO_TRANSLATE = 'mr'  # for marathi

def ocr_from_images(dir):
    # Returns array of strings where each string is an original text from a scanned page

    files = [
        name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))
    ]
    files.sort()
    array_of_pages = []
    print("Scanning {} images for text...".format(str(len(files))))
    for index, PHOTO in enumerate(files):
        if PHOTO != ".DS_Store":  # for OSX Users
            # If you don't have tesseract executable in your PATH, include the following:
            # pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
            # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
            print("...")
            # Scan the photo to obtain text
            original_text = pytesseract.image_to_string(
                Image.open("{}/{}".format(dir, PHOTO))
            )
            array_of_pages.append(original_text)
    return array_of_pages

def translate_with_google_api(array_of_original_pages, google_api_token, to):
    # Returns array of strings where each string is a translated text from a scanned page
    print("Translating document to {}...".format(to))
    url = "https://translation.googleapis.com/language/translate/v2"

    headers = {
        "Authorization": "Bearer {}".format(google_api_token),
        "Content-Type": "application/json",
    }
    translation = []
    for page_to_translate in array_of_original_pages:
        print("...")
        payload = json.dumps({"q": [page_to_translate], "target": to})
        response = requests.request("POST", url, headers=headers, data=payload)
        translated_page = json.loads(response.text)
        print(translated_page)
        translated_page = translated_page["data"]["translations"][0]["translatedText"]
        translation.append(translated_page)
    return translation

def translate_to_marathi(DIR):
    original_images = ocr_from_images(DIR)

    translated_pages = translate_with_google_api(
    original_pages, GOOGLE_API_TOKEN, to=LANGUAGE_TO_TRANSLATE
    )

    return translated_pages

