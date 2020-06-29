from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app =Flask(__name__)

@app.route('/')
def render_main():
        return render_template('main2.html')
    
@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileupload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/root/upload/'+ secure_filename(f.filename))
        return 'uploads dir에 업로드 성공'

if __name__ == '__main__':
    app.debug=True
    app.run('0.0.0.0')
