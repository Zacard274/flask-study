from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)  #SQLAlchemy是一个类，此处为实例化

db.create_all()

@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)