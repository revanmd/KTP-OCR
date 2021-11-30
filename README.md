# KTP OCR
## Indonesian ID Card OCR using tesseract OCR

KTP OCR is python-flask with tesseract web application to convert Indonesian ID Card to text / JSON Data
- convert KTP to JSON
- text preprocessing for enhance the quality of result (in progres) 

## Installation (UBUNTU)

KTP OCR needs Python 3+ and tesseract OCR. Currently i'm using Ubuntu 20.0 and its running normaly.

To install tesseract OCR Click [here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

1. Clone GIT Repository
    ```sh
    git clone https://github.com/revanmd/KTP-OCR.git
    ```
2. Go root directory of this project 
    ```sh
    cd KTP-OCR
    ```
3. Optionally to use Virtual ENV (You can skip this step if you want install dependencies globaly)
    ```sh
    virtualenv venv
    source venv/bin/activate
    ```
4. Install dependencies
     ```sh
    pip install -r requirement.txt
    ```
5. running the server, this is for development server
    ```sh
    python wsgi.py
    ```
## Production
You can use gunicorn if using virtual env using this command
```sh
venv/bin/gunicorn -b 0.0.0.0:5000 -w 5 wsgi:app
```
