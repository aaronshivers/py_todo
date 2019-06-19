# Import Dependencies
from flask import Flask, render_template, url_for

# Initialize Application
app = Flask(__name__)

# GET /
@app.route('/')
def index():
  return render_template('index.html')

# Run Server
if __name__ == '__main__':
  app.run(debug=True)