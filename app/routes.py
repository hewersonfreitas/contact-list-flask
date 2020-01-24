from app import app, db
from app.models import User
from flask import render_template, request


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    list_rows = User.query.all()
    return render_template("form_list.html", list_rows=list_rows)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        result = request.form
        if result:
            user = User(
                name=result['name'],
                telephone=result['telephone'],
                email=result['email']
            )
            db.session.add(user)
            db.session.commit()

    list_rows = User.query.all()
    return render_template("form_list.html", list_rows=list_rows)
