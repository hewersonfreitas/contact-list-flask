from app import app
from flask import render_template, request



@app.route('/')
@app.route('/index',methods = ['POST','GET'])
def index():
    return render_template("form.html")


@app.route('/register',methods = ['POST','GET'])
def register():
    if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)