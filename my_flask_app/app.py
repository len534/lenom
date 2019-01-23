from flask import Flask,send_file,request,flash,redirect, url_for, render_template
from werkzeug.utils import secure_filename
import Excel_case
import os
app = Flask(__name__)

@app.route('/')
def upload_file():
	return '''
<html>
   <body>
      <form action = "http://localhost:5000/json" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
   </body>
</html>'''   
   
@app.route('/json', methods = ['GET', 'POST'])
def upload_file_1():
   if request.method == 'POST':
      f = request.files['file']
      Excel_case.excel_to_json_str(f)
      return Excel_case.excel_to_json_str(f)
		
if __name__ == "__main__":
    app.run()
