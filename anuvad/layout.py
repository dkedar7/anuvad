import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64

theme_color_code = "#ffffff" #Indigo

image_filename = 'assets/icon.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")

# 1. Navbar placeholder (currently black row)
navbar = dbc.Row()

# 2. Mosaic icon image
icon_image = dbc.Row(
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image),
                    style={'width':'250px'}),
                    justify='center'
)


### 3. Body title
body_paragraph = dbc.Row(
    [
        dbc.Col(
                [
                    html.Br(),
                    html.H5("Translate text from English to many different languages.",
                        style={'text-align':'center', "color":"darkgray", "font-family": "Verdana; Gill Sans"}),
                    html.Br(),
                    html.H6("This application currently only supports translating English text to Marathi.",
                        style={'text-align':'center', "color":"darkgray", "font-family": "Verdana; Gill Sans"})
                ],
                style ={"padding":"1% 1% 3% 0%", "background-color":theme_color_code}
               )
    ],
    style = {'text-align':'center', "padding":"1% 1% 1% 0%", "background-color":theme_color_code}
)

### 4. Github logo
github_logo = dbc.Row(
            html.A(
                html.I(className = "fa-2x fab fa-github", style={'color':'#000000'}),
                href = "https://github.com/dkedar7/anuvad", target="_blank",
                className="mr-3"
        ),
        justify='center'
)

### 5. Upload button
upload_button = dbc.Col(
    [
        dcc.Upload(id='upload-image',
                   children = dbc.Col(
                       [
                           'Click to upload an image'
                       ]
                   ),
                   style={
                       'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                   }
            ),
        ]
)


### 7. Display original and processed images
images = dbc.Row(
    [
        dbc.Col(dbc.CardImg(id='original-image'), style = {"padding" : "2% 1% 1% 2%", 
                                                            'lineHeight': '60px',
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'margin': '10px'}),
        dbc.Col(html.P(id='processed-text'), style = {"padding" : "2% 1% 1% 2%", 
                                                        'lineHeight': '60px',
                                                        'borderWidth': '1px',
                                                        'borderStyle': 'dashed',
                                                        'borderRadius': '5px',
                                                        'margin': '10px'}
                    )
    ]
)

### 8. Footer
footer = dbc.Row(
    dbc.Col(
        html.Div(
        [
            'To be able to translate text in this manner, the model must first identify English text from an image '
            'and then translate it into the chosen language. '
            'This application uses Google Vision APIs to do both of these tasks. '
            'Visit the ',
            html.A("GitHub repository", 
                    href = "https://github.com/dkedar7/anuvad/",
                    target = "_blank"),
            ' to learn more.'
        ],
    ),
    width={"size": 10}
), 
    justify='center',
    align='center',
    style={'margin-bottom': "10%"}
)

### Bring it together
top = dbc.Container(
    [
        dcc.Store(id='memory-output', storage_type='memory'),
        navbar,
        icon_image,
        body_paragraph,
        github_logo
    ],
    fluid = False
)

middle = dbc.Container(
    [
        upload_button,
        images
    ],
    fluid = False
)

bottom = dbc.Container(
    [   
        footer
    ],
    fluid = False
)

layout = dbc.Container(
    [
        top, 
        middle,
        bottom
    ]
)