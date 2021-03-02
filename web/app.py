# importing libraries.
import os

# from dotenv import load_dotenv
from flask import Flask, request, render_template
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename

# init dotenv
# load_dotenv()

# init main application 
horse = Flask(__name__)

# hacky cracky.
KEY = os.environ.get("PRIVATE_KEY", "1234")


# indexing files feom main folder
@horse.route('/dir', methods=['GET'])
def index():
    AutoIndex(horse, browse_root=os.path.curdir + 'Engineering')

# home
@horse.route('/', methods=['GET'])
@horse.route('/home', methods=['GET'])
def home():
    return render_template(
        "home.html")

# route decorator.
@horse.route('/uploads/'+KEY, methods=['GET', 'POST'])

# upload files func.
def upload_():
  if request.method == 'POST':
    file = request.files["file"]
    
    # which branch ?
    UPLOAD = request.form["sub"]
    
    # indeed.
    filename = secure_filename(file.filename)
    
    # saving it.
    file.save(os.path.join(UPLOAD, filename))
    
    # lock the door.
    return "saved"
    
# POST form.
  return '''
    <!doctype html>
    <head>
    <title>Upload New Book</title> 
    </head>
    <body>
    <h1>Upload</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name=sub>
      <input type=file name=file>
      <input type=submit value=Upload>
      <h1> Fill text with subject name 
      BME BEE PPS ES MATHS </h1>
    </form>
    '''
