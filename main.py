import requests
import base64

from bs4 import BeautifulSoup
from weasyprint import HTML

html_cont = """<html>
      <head>
        <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
        <script src="https://use.typekit.net/lww3zic.js"></script>
        <script>try{Typekit.load();}catch(e){}</script>
        <style>
          html, body {{
            background: white;
            color:black;
            padding: 20px;
          }}
          body {{
            padding:10px;
          }}
          .inlineComment {{
            display:inline !important;
          }}
          .spacer {{
            display:none !important;
          }}
          h1 {{
            text-align:center;
          }}
          span,div,h1,h2,h4,h5,h6 {{
            background-color:transparent !important;
          }}
          img {{
            width:50%;
            margin:0px auto;
            display:block;
            height: auto;
          }}
          @page {{
            background: white;
            margin: 0;
            size: US-Letter portrait;
          }}
          .page {{ page-break-before: always }}
          .navigationThemeName {{ border-radius: 99999px }}
        </style>
      </head>
      <body>
      <h1>
      Social
      Brandable by
      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    </h1>
        <p>Testing #ad</p><p>🌟✨Hello! How are you today? 🌈😊 Just wanted to send some positive vibes your way! 🌻🌼 Life is
                   a beautiful journey, so embrace each moment <img src='https://qsp-ada.qa.quotient-cloud.com/muse-brandables-resized-images/brandable-images/105018/12adf703-e4c7-4e50-8640-02e02dbc1c92-image1.jpeg'> with joy and gratitude. 🌸💖 Remember, you're amazing
                   Sending virtual hugs and smiles your way! 😇 Keep shining bright! ✨💫<p>
        <img src="https://qsp-ada.qa.quotient-cloud.com/muse-brandables-resized-images/brandable-images/105018/12adf703-e4c7-4e50-8640-02e02dbc1c92-image1.jpeg"><p>cvsdvdsvdsvdsvdsvdsvdsvdsvdsvdvds</p>
        <img src="https://qsp-ada.qa.quotient-cloud.com/muse-brandables-resized-images/brandable-images/105018/12adf703-e4c7-4e50-8640-02e02dbc1c92-image1.jpeg"><p>cvsdvdsvdsvdsvdsvdsvdsvdsvdsvdvds</p>
        <img src="https://qsp-ada.qa.quotient-cloud.com/muse-brandables-resized-images/brandable-images/105018/12adf703-e4c7-4e50-8640-02e02dbc1c92-image1.jpeg"><p>cvsdvdsvdsvdsvdsvdsvdsvdsvdsvdvds</p>
        <img src="https://qsp-ada.qa.quotient-cloud.com/muse-brandables-resized-images/brandable-images/105018/12adf703-e4c7-4e50-8640-02e02dbc1c92-image1.jpeg">
        <p>🌟✨Hello! How are you today? 🌈😊 Just wanted to send some positive vibes your way! 🌻🌼 Life is
                   a beautiful journey, so embrace each moment <img src='https://qsp-ada.qa.quotient-cloud.com/muse-brandables-resized-images/brandable-images/105018/12adf703-e4c7-4e50-8640-02e02dbc1c92-image1.jpeg'> with joy and gratitude. 🌸💖 Remember, you're amazing
                   Sending virtual hugs and smiles your way! 😇 Keep shining bright! ✨💫</p>
      </body>
    </html>"""

soup = BeautifulSoup(html_cont, 'html.parser')

img_tags = soup.find_all('img')

image_data_dict = {}

for index, img_tag in enumerate(img_tags):
    image_url = img_tag['src']
    image_response = requests.get(image_url)
    image_data = base64.b64encode(image_response.content).decode('utf-8')
    key = f'image_{index}'
    image_data_dict[key] = image_data

    img_tag['src'] = f"data:image/jpeg;base64,{image_data_dict[key]}"

modified_body_content = str(soup.body)

html_content = f"""
<html>
      <head>
        <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
        <script src="https://use.typekit.net/lww3zic.js"></script>
        <script>try{{Typekit.load();}}catch(e)</script>
        <style>
          html, body {{
            background: white;
            color:black;
            padding: 20px;
          }}
          body {{
            padding:10px;
          }}
          .inlineComment {{
            display:inline !important;
          }}
          .spacer {{
            display:none !important;
          }}
          h1 {{
            text-align:center;
          }}
          span,div,h1,h2,h4,h5,h6 {{
            background-color:transparent !important;
          }}
          img {{
            width:50%;
            margin:0px auto;
            display:block;
            height: auto;
          }}
          @page {{
            background: white;
            margin: 0;
            size: US-Letter portrait;
          }}
          .page {{ page-break-before: always }}
          .navigationThemeName {{ border-radius: 99999px }}
        </style>
      </head>
        {modified_body_content}

    </html>
"""
HTML(string=html_content).write_pdf('Draft.pdf')
