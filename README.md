# Image Text Extractor

This is a simple web application built with Python and Flask that extracts text from images uploaded by users. It uses the Tesseract OCR engine to perform optical character recognition on the images.

## Installation

```markdown

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Send a POST request to the `/extract_text` endpoint with an image file included in the request body.
3. The application will process the image, extract text using Tesseract, and return a response indicating whether the keyword "abuzar" is found in the extracted text.

## API Endpoint

- `/extract_text` (POST): Endpoint for extracting text from an image file uploaded in the request body.

## Dependencies

- Flask
- pytesseract
- Pillow

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
