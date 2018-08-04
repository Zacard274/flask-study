import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


artiii_tag = db.Table('artiii_tag',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id', primary_key=True)),
        db.Column('artiii_id', db.Integer,db.ForeignKey('artiii.id', primary_key=True))
        )


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class Artiii(db.Model):
    __tablename__ = 'artiii'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)

    tags = db.relationship('Tag', secondary=artiii_tag, backref='articles')

db.create_all()


@app.route('/')
def index():

    article1 = Artiii(title='aaa')
    article2 = Artiii(title='bbb')

    tag1 = Tag(name='111')
    tag2 = Tag(name='222')

    article1.tags.append(tag1)
    article1.tags.append(tag2)

    article2.tags.append(tag1)
    article2.tags.append(tag2)

    db.session.add(article1)
    db.session.add(article2)
    db.session.add(tag1)
    db.session.add(tag2)

    db.session.commit()

    x = Tag.query.filter(Tag.name=='111').first()
    articles = x.articles

    for i in articles:
        print(i.title)

    return 'db_demo4'


if __name__ == '__main__':
    app.run()

