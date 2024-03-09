from flask import Flask, request
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    # Get the image file from the request
    image_file = request.files['image']
    
    # Open the image using PIL
    image = Image.open(image_file)
    
    # Extract text from the image using Tesseract OCR
    text = pytesseract.image_to_string(image)

    if "abuzar" in text:
        return "abuzar is found in the image"
    else:
        return "abuzar is not found in the image"
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
