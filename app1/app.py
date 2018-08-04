from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://fn:123@localhost/study"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    pwd = db.Column(db.String(50))

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

@app.route('/', methods=['GET','POST'])
def fn():
    return render_template('index.html')


@app.route('/registe',methods=['GET','POST'])
def registe():
    username = request.form["username"]
    password= request.form["password"]
    user = User(username,password)
    db.session.add(user)
    db.session.commit()
    return render_template('registe.html')

@app.route('/login',methods=['GET','POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    pwd = db.session.query(User.pwd).filter_by(name=username).first()
    db.session.commit()
    if password == str(pwd[0]):
        return f"success"
    else:
        return f"fail"


if __name__ == '__main__':
    app.run(debug=True)
