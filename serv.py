import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import prediction

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['wav', '3gp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print ('**found file', file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # for browser, add 'redirect' function on top of 'url_for'
            return url_for('uploaded_file', filename=filename)
    return 'deeply sad story'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    path = "uploads/" + filename
    print (path)
    return prediction.predict(path)

if __name__ == '__main__':
    app.run(debug=True)
