from dash.dependencies import Input, Output

import base64
import os

from layout import layout as layout
from app import app

from callbacks import detect_and_translate

app.layout = layout

@app.callback(
    Output('processed-text', 'children'),
    [Input('upload-image', 'contents')]
)
def update_translation(contents):
    if contents:
        _, content_string = contents.split(',')
        return detect_and_translate(content_string)
    else:
        return "कधीही शिकणे थांबवू नका, कारण आयुष्य कधीही अध्यापन थांबवत नाही."


@app.callback(
    Output('original-image', 'src'),
    [Input('upload-image', 'contents')]
)
def update_original_image(contents):
    if contents:
        _, content_string = contents.split(',')
        content_image_string = 'data:image/png;base64,{}'.format(content_string)
        return content_image_string
    else:
        image_filename = 'assets/defaultimage.png' # replace with your own image
        encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")
        default_image = 'data:image/png;base64,{}'.format(encoded_image)
        return default_image


if __name__ == '__main__':
    app.server.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))