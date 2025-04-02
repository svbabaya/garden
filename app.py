from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import enum
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/database/data.db'
db = SQLAlchemy(app)

with open('templates/settings.json', mode='r', encoding='utf-8') as read_file:
    settings = json.load(read_file)

class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(300), unique=True, nullable=False)
    author = db.Column(db.String(100))
    def __repr__(self):
        return f'<Phrase {self.id}>'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_category = db.Column(db.Integer, nullable=False)
    sub_category = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    short_text = db.Column(db.String(300), nullable=False)
    long_text = db.Column(db.Text(1000), nullable=False)
    image_directory = db.Column(db.String(100), nullable=False, default='default.jpg')
    location = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'<Article {self.id}>'

class MainCategory(enum.Enum):
    tree = 1
    fruit_tree = 2
    bush = 3
    fruit_bush = 4
    herbaceous_plant = 5

class SubCategoryHerbaceousPlant(enum.Enum):
    perennial_ornamental = 1
    annuals_ornamental = 2
    perennial_wild = 3

# @app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', settings=settings)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', settings=settings)

@app.route('/about')
def about():
    return render_template('about.html', settings=settings)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', settings=settings)

@app.route('/cards/<int:id>')
def cards(id: int):

    return render_template('cards.html', settings=settings)

@app.route('/item/5')
def item():
    return render_template('item.html', settings=settings)



@app.route('/auth')
def auth():
    return render_template('auth.html', settings=settings)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
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
        return render_template('admin.html', settings=settings)

@app.route('/plant/<string:name>/<int:id>')
def plant(name, id):
    return 'Plant page'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
