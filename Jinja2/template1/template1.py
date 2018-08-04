from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    class person():
        name = '冯楠'
        age = 16

    p = person()

    context = {            # 当参数比较多时，建立一个context字典，将参数全部写进去
        'username': '杨光',
        'gender': '男',
        'person': p,       # 模版中访问属性
        'websites': {      # 模版中访问字典
            'baidu': 'www.baidu.com',
            'google': 'www.google.com',
            'tencent': 'www.qq.com'
        }
    }
    return render_template('index.html', age=18, **context)   # 只有一个传参age时直接写在这里


if __name__ == '__main__':
    app.run(debug=True)