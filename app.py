from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return '', 204

@app.route('/inventory')
def inventory():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('inventory.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
