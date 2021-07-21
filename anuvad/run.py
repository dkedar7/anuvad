import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from urllib.parse import quote as urlquote
import flask
from flask import Flask, send_from_directory, send_file, request, session, _request_ctx_stack

import base64
import datetime
import io
import os
import string
import random
import re

from layout import layout as layout
from app import app, server, cache

app.layout = layout

@app.callback(
    Output('processed-image', 'src'),
    [Input('upload-image', 'contents'),
    Input('passage_dropdown', 'value')]
)
def update_processed_image(contents, model):
    if contents:
        content_type, content_string = contents.split(',')
        return None

@app.callback(
    Output('original-image', 'src'),
    [Input('upload-image', 'contents')]
)
def update_original_image(contents):
    if contents:
        content_type, content_string = contents.split(',')
        content_image_string = 'data:image/png;base64,{}'.format(content_string)
        return content_image_string


if __name__ == '__main__':
    app.server.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))