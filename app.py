# Import Dependencies
from flask import Flask

# Initialize Application
app = Flask(__name__)

# GET /
@app.route('/')
def index():
  return 'Hello There!'

# Run Server
if __name__ == '__main__':
  app.run(debug=True)