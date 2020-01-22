export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
flask db init
flask db migrate
flask db upgrade