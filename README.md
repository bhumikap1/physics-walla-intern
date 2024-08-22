# Image-to-Text Converter

## Overview

The "Image-to-Text Converter" is a web application that allows users to upload images and convert the text within those images into editable text. The application also includes additional features like converting JPG to Word, PDF to Word, and JPG to PDF, all integrated into a user-friendly interface with a navigation bar.

## Features

- Image to Text Conversion: Upload an image and extract the text within it.
- JPG to Word: Convert JPG images to Word documents.
- PDF to Word: Convert PDF files to Word documents.
- JPG to PDF: Convert JPG images to PDF files.
- Download Files: Easily download files in any formats.

## Project Structure

```
image_to_text_converter/
│
├── converter/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   ├── templates/
│   │   └── upload_image.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── imagetotext/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- Bootstrap (included via CDN)
- Tesseract-OCR (for text extraction)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bhumikap1/physics-walla-intern.git
    cd image-to-text-converter
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Tesseract-OCR:

    - Download and install Tesseract-OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Make sure to add Tesseract to your system's PATH.

5. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the server:

    ```bash
    python manage.py runserver
    ```

7. Open the application in your web browser:

    Visit `http://127.0.0.1:8000/` to use the application.

## Usage

1. Home Page: The home page allows you to upload an image and convert it to text.

2. Navbar Options:
   - Text Converter: Converts the uploaded image to text.
   - JPG to Word: Convert a JPG image to a Word document.
   - PDF to Word: Convert a PDF file to a Word document.
   - JPG to PDF: Convert a JPG image to a PDF file.

3.Download Files: Easily download files in any formats.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django: The web framework used to build the application.
- Bootstrap: For providing a responsive design.
- Tesseract-OCR: For enabling text extraction from images.
```
