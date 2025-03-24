from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/plants.db'
db = SQLAlchemy(app)

with open('templates/settings.json', mode='r', encoding='utf-8') as read_file:
    settings = json.load(read_file)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_category = db.Column(db.Integer, nullable=False)
    sub_category = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    short_text = db.Column(db.String(300), nullable=False)
    long_text = db.Column(db.Text(1000), nullable=False)
    preview_img = db.Column(db.String(100), nullable=False, default='default.jpg')
    status = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'<article {self.id}>'

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', settings=settings)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        name = request.form['name']
        short_text = request.form['short_text']
        long_text = request.form['long_text']
        article = Article(name=name, short_text=short_text, long_text=long_text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error'
    else:
        return render_template('create_article.html')

@app.route('/plant/<string:name>/<int:id>')
def plant(name, id):
    return 'Plant page'

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)