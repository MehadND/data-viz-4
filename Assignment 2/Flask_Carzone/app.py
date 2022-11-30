from flask import Flask, render_template, url_for, request, redirect
from werkzeug.datastructures import ImmutableMultiDict
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cars.db"

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcar', methods=['GET', 'POST'])
def addcar():
    if request.method == 'POST':
        content = json.dumps(request.form)
        return content
    else:
        return render_template('addcar.html')
    
if __name__ == "__main__":
    app.run(debug=True)