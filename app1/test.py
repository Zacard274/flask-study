from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy
from app import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://fn:123@localhost/study"
db = SQLAlchemy(app)

@app.route('/test',methods=['GET'])
def test():
    pwd = db.session.query(User.pwd).filter_by(name=123).all()
    db.session.commit()
    return pwd


app.run(debug=False)