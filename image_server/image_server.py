from flask import Flask, request
from werkzeug.utils import secure_filename
import os
import datetime

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = secure_filename(file.filename)
        now = datetime.datetime.now()
        date_dir = now.strftime("%Y-%m-%d")
        hour_dir = now.strftime("%H")
        dir_path = os.path.join(date_dir, hour_dir)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file.save(os.path.join(dir_path, filename))
        return 'File saved successfully', 200

if __name__ == '__main__':
    app.run(debug=True)