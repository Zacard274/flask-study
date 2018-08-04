from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {
        'username': '小明',
        'age': 20
    }
    websites = ['www.baidu.com','www.google.com']

    for k,v in user.items():
        print(k)
        print(v)
    return render_template('index.html',user=user,websites=websites)


if __name__ == '__main__':
    app.run(debug=True)