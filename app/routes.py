from app import app, db
from app.models import User
from flask import redirect, url_for, render_template, request


@app.route('/')
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

    return redirect(url_for('index'))
