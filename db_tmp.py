from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'
app2.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app2)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<Student %r>' % self.name

if __name__ == '__main__':
    with app2.app_context():
        db.create_all()
    app2.run(debug=True)
    