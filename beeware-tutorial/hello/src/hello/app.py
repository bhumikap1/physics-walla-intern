import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import requests
import os
from tkinter import Tk
from tkinter import filedialog
from tkinter import simpledialog
from docx import Document
from fpdf import FPDF
import pyperclip

class ImageToTextApp(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        # File selection buttons
        self.file_chooser_image = toga.Button('Choose Image (jpg/jpeg/png)', on_press=self.select_file_image)
        box.add(self.file_chooser_image)
        
        self.file_chooser_pdf = toga.Button('Choose PDF', on_press=self.select_file_pdf)
        box.add(self.file_chooser_pdf)

        self.file_chooser_docx = toga.Button('Choose DOCX', on_press=self.select_file_docx)
        box.add(self.file_chooser_docx)

        # Result label and buttons
        self.result_label = toga.Label('No file selected', style=Pack(padding_top=10))
        box.add(self.result_label)
        
        self.download_button = toga.Button('Download Text', on_press=self.download_text, style=Pack(padding_top=10))
        self.download_button.enabled = False
        box.add(self.download_button)
        
        self.copy_button = toga.Button('Copy to Clipboard', on_press=self.copy_to_clipboard, style=Pack(padding_top=10))
        self.copy_button.enabled = False
        box.add(self.copy_button)
        
        self.main_window.content = box
        self.main_window.show()

    def select_file_image(self, widget):
        self.select_file('image')

    def select_file_pdf(self, widget):
        self.select_file('pdf')

    def select_file_docx(self, widget):
        self.select_file('docx')

    def select_file(self, file_type):
        root = Tk()
        root.withdraw()
        
        filetypes = {
            'image': [('JPEG Files', '*.jpg;*.jpeg'), ('PNG Files', '*.png')],
            'pdf': [('PDF Files', '*.pdf')],
            'docx': [('DOCX Files', '*.docx')]
        }
        
        file_path = filedialog.askopenfilename(
            title=f'Choose a {file_type.upper()} File',
            filetypes=filetypes[file_type]
        )
        
        if file_path:
            self.result_label.text = f'Selected file: {file_path}'
            self.upload_file(file_path, file_type)

    def upload_file(self, file_path, file_type):
        url = f'http://127.0.0.1:8000/{file_type}/'
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                headers = {'Accept': 'application/json'}
                response = requests.post(url, files=files, headers=headers)
            
            if response.status_code == 200:
                response_data = response.json()
                self.extracted_text = response_data.get('extracted_text', 'No text extracted')
                self.result_label.text = f'{file_type.upper()} uploaded and text extracted successfully!'
                self.download_button.enabled = True
                self.copy_button.enabled = True
            else:
                self.result_label.text = f'Failed to upload {file_type.upper()}. Status code: {response.status_code}'
        except Exception as e:
            self.result_label.text = f'An error occurred: {str(e)}'

    def download_text(self, widget):
        if hasattr(self, 'extracted_text'):
            options = ['Text', 'PDF', 'DOCX']
            download_format = simpledialog.askstring("Download As", f"Choose format ({', '.join(options)}):")
            
            if download_format:
                download_format = download_format.lower()
                if download_format == 'text':
                    self.save_as_text()
                elif download_format == 'pdf':
                    self.save_as_pdf()
                elif download_format == 'docx':
                    self.save_as_docx()
                else:
                    self.result_label.text = 'Unsupported format!'
        else:
            self.result_label.text = 'No text to download!'

    def save_as_text(self):
        with open('extracted_text.txt', 'w') as f:
            f.write(self.extracted_text)
        os.startfile('extracted_text.txt', 'open')

    def save_as_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, self.extracted_text.encode('latin-1', 'replace').decode('latin-1'))
        pdf_file = 'extracted_text.pdf'
        pdf.output(pdf_file)
        os.startfile(pdf_file, 'open')

    def save_as_docx(self):
        doc = Document()
        doc.add_paragraph(self.extracted_text)
        doc_file = 'extracted_text.docx'
        doc.save(doc_file)
        os.startfile(doc_file, 'open')

    def copy_to_clipboard(self, widget):
        if hasattr(self, 'extracted_text'):
            pyperclip.copy(self.extracted_text)
            self.result_label.text = 'Text copied to clipboard!'
        else:
            self.result_label.text = 'No text to copy!'

def main():
    return ImageToTextApp('Image to Text App', 'org.example.imagetotext')

if __name__ == '__main__':
    main().main_loop()
