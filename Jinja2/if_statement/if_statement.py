from flask import Flask,render_template

app = Flask(__name__)

@app.route('/<is_login>/')
def index(is_login):
    if is_login == '1':
        user = {           # 定义类
            'username': '小明',
            'age': 16
        }
        return render_template('index.html',user=user)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)