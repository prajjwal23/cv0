from flask import Flask, request, jsonify, send_file
import os
from src.process_image import process_image

app = Flask(__name__)

# Define upload folder
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/process", methods=["POST"])
def process():
    # Check if file is provided
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save uploaded file
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Process image
    try:
        output_path = process_image(input_path, OUTPUT_FOLDER, sr_method="bicubic", inpaint_method="telea")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Return processed image
    return send_file(output_path, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
