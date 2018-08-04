from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article'  #带下划线表示被表示

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    context = db.Column(db.Text, nullable=False)


db.drop_all()
db.create_all()


@app.route('/')
def index():
    article1 = Article()
    article1.title = 'aaa'
    article1.context = 'bbb'
    db.session.add(article1)  #新增数据
    db.session.commit()       #凡是对数据做修改，都要提交
    return 'hello world'

@app.route('/search/')
def search():
    a = Article.query.filter(Article.title=='aaa').first()  #查询数据
    print(a)
    print(a.title)
    print(a.context)
    c = Article.query.filter(Article.title=='aaa')[0]
    print(c)
    b = Article.query.filter(Article.title=='aaa').all()
    print(b)

    # a.title = 'aaa1'          #修改数据（先查后改）
    # db.session.commit()

    db.session.delete(a)        #删除数据（先查后删）
    db.session.commit()

    return 'search'

if __name__ == '__main__':
    app.run()