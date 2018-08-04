import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)


class Arti(db.Model):
    __tablename__ = 'arti'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('abcd'))


db.create_all()


@app.route('/')
def index():
    # user1 = User(username='fn')
    # db.session.add(user1)
    # db.session.commit()

    # arti1 = Arti(title='aaa', content='bbb', author_id=1)
    # db.session.add(arti1)
    # db.session.commit()

    # arti2 = Arti(title='ccc', content='ddd', author_id=1)
    # db.session.add(arti2)
    # db.session.commit()

    #查找文章标题为aaa的作者的名字
    # article = Arti.query.filter(Arti.title == 'aaa').first()
    # authorid = article.author_id
    # author = User.query.filter(User.id == authorid).first()
    # name = author.username
    # print(name)

    # 建立relationship后直接简化成：
    article = Arti.query.filter(Arti.title=='aaa').first()
    print(article.author.username)

    #查找fn写过的所有文章
    user = User.query.filter(User.username=='fn').first()
    contents = user.abcd
    for i in contents:
        print(i.title,i.content)
    return 'db_demo3'


if __name__ == '__main__':
    app.run()

