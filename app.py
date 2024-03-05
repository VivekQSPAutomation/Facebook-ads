import os
import requests
import base64
from bs4 import BeautifulSoup
from weasyprint import HTML
from fastapi import FastAPI, Request, File, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get('/')
async def hello_world():
    return {"message": "hello_world"}

@app.post('/download_pdf')
async def download_pdf(request: Request):
    form = await request.form()
    html_cont = form['html_content']

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
    # Create PDF from HTML
    pdf_filename = f'{os.getcwd()}/Draft.pdf'

    HTML(string=html_content).write_pdf(pdf_filename)
    return FileResponse(pdf_filename, media_type='application/pdf')
