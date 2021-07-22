import os
import base64

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/kedardabhadkar/anuvad/anuvad/callbacks/web-apps-273916-36a791351d58.json"


def detect_text(content):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    content_base64 = base64.b64decode(content)
    image = vision.Image(content=content_base64)

    response = client.text_detection(image=image)
    text = response.text_annotations[0].description
    
    return text


def translate_text_with_model(target, text, model="nmt"):
    """Translates text into the target language.

    Make sure your project is allowlisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target, model=model)
    
    return result['translatedText']


def detect_and_translate(content):

    detected_text = detect_text(content)
    translated_text = translate_text_with_model(target='mr', text=detected_text)

    return translated_text