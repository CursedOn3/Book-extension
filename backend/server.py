from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pdf2image import convert_from_path
from ebooklib import epub
from PIL import Image
import os
import io

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    if filename.lower().endswith('.pdf'):
        return jsonify({"type": "pdf", "filename": file.filename})
    elif filename.lower().endswith('.epub'):
        return jsonify({"type": "epub", "filename": file.filename})
    else:
        return jsonify({"error": "Unsupported file format"}), 400

@app.route('/pdf/<filename>/<int:page_num>')
def get_pdf_page(filename, page_num):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    pages = convert_from_path(filepath, first_page=page_num, last_page=page_num)

    if not pages:
        return jsonify({"error": "Page not found"}), 404

    img_io = io.BytesIO()
    pages[0].save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

@app.route('/epub/<filename>/<int:page_num>')
def get_epub_page(filename, page_num):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    book = epub.read_epub(filepath)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    if page_num < 1 or page_num > len(items):
        return jsonify({"error": "Page not found"}), 404

    content = items[page_num - 1].get_content().decode('utf-8')

    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
