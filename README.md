# py_todo

## Setup

### Create Virtual Enviroment
```
virtualenv env
```

### Activate Virtual Evironment
```
source env/bin/activate
```

### Install Dependencies
```
pip3 install flask flask-sqlalchemy
```

### Create Database
```
python3
from app import db
db.create_all()
exit()
```

### Run Server
http://localhost:5000
```
python3 app.py
```