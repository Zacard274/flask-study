from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    books = [
        {
            'name': '西游记',
            'author': '吴承恩',
            'price': 122
        },
        {
            'name': '红楼梦',
            'author': '曹雪芹',
            'price': 92
        },
        {
            'name': '三国演义',
            'author': '罗贯中',
            'price': 87
        },
        {
            'name': '水浒传',
            'author': '施耐庵',
            'price': 102
        },
    ]
    return render_template('index.html',books=books)


if __name__ == '__main__':
    app.run(debug=True)