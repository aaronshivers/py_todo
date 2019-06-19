# Import Dependencies
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Todo Class/Model
class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Task %r>' % self.id


# POST & GET /
@app.route('/', methods=['POST', 'GET'])
def index():
  return render_template('index.html')

# Run Server
if __name__ == '__main__':
  app.run(debug=True)