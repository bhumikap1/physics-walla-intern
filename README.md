# Image-to-Text Converter

## Overview

The **Image-to-Text Converter** is a web application that allows users to upload images and convert the text within those images into editable text.
The application also includes additional features like converting JPG to Word, PDF to Word, and JPG to PDF, all integrated into a user-friendly interface with a navigation bar.

## Features

- **Image to Text Conversion**: Upload an image and extract the text within it.
- **JPG to Word**: Convert JPG images to Word documents.
- **PDF to Word**: Convert PDF files to Word documents.
- **JPG to PDF**: Convert JPG images to PDF files.
- **Download the text**: Download the text in all formats.
- **Copy the Text**: copy text to clipboard.

## Project Structure

image_to_text/
├── beeware-tutorial
│  ├── beeware-venv/
│      ├── hello
│  │
│  ├── src/
│     ├── hello/
│         ├── __init__.py
│         ├── app.py
│         └── resources/
│             └── __init__.py
│
├── image_to_text.egg-info/
│   │
│   ├── build/
│   │
│   ├── dist/
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_app.py
├── README.md 
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── converter/
│ ├── migrations/
│ ├── static/
│ │ └── css/
│ ├── templates/
│ │ └── upload_image.html
│ │ ├── index.html
│ │ ├── upload_pdf.html
│ │ └── upload_docx.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
│
├── imagetotext/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── README.md


## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- Bootstrap (included via CDN)
- Tesseract-OCR (for text extraction)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/image-to-text-converter.git
    cd image-to-text-converter
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tesseract-OCR:**

    - Download and install Tesseract-OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Make sure to add Tesseract to your system's PATH.

5. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the server:**

    ```bash
    python manage.py runserver
    ```

7. **Open the application in your web browser:**

    Visit `http://127.0.0.1:8000/` to use the application.

## Usage

1. **Home Page**: The home page allows you to upload an image and convert it to text.

2. **Navbar Options**:
   - **Text Converter**: Converts the uploaded image to text.
   - **JPG to Word**: Convert a JPG image to a Word document.
   - **PDF to Word**: Convert a PDF file to a Word document.
   - **JPG to PDF**: Convert a JPG image to a PDF file.
     
## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Django**: The web framework used to build the application.
- **Bootstrap**: For providing a responsive design.
- **Tesseract-OCR**: For enabling text extraction from images.

ImageToText BeeWare App
Overview
This project is an Image to Text Converter application developed using the BeeWare framework. The application allows users to upload an image (JPEG, PNG, etc.), converts the image to text using Optical Character Recognition (OCR), and displays the extracted text.

Features
Upload Image: Users can upload an image file from their local system.
Text Extraction: The app uses OCR to extract text from the uploaded image.
Display Text: The extracted text is displayed within the application interface.
Requirements
Python 3.8+
Toga (BeeWare's GUI toolkit)
Django (for the backend server to process the images)
Requests (for handling HTTP requests)
Tkinter (for file dialog operations)

Installation
Clone the Repository:
git clone https: [https://github.com/bhumikap1/physics-walla-intern.git]
cd your-repo-name

Install Dependencies:
pip install toga requests
Run the Django Backend:

Ensure you have a Django server running. If you have not set up the Django backend, please follow the setup instructions in your Django application repository.

Run the BeeWare App:
briefcase dev

Usage: Start the Django backend server on http://127.0.0.1:8000/.

Open the BeeWare app by running briefcase dev in your terminal.

In the app, click on the Upload Image button to select an image file.

The app will send the image to the Django backend for processing.

The extracted text will be displayed within the app.

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

License
This project is licensed under the MIT License.

Contact
For any questions or feedback, please contact [bhumikap754@gmail.com].
