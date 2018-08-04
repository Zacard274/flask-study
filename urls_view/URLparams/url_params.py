from flask import Flask,url_for,redirect


app = Flask(__name__)


@app.route('/')
def index():
    # print(url_for('my_list'))        # url反转，即从视图函数到url的转换
    # print(url_for('xxx',id='123'))   # 需要输入参数（id）的值
    # return redirect('/login/')       # 重定向。但是这只能指向/login/，如果login的url变化，则404报错
    return redirect(url_for('login'))  # 这样写的话，不管login的url变成什么，都能指向它的页面


@app.route('/list/')
def my_list():
    return 'list'


@app.route('/xxx/<id>')              # url传参，用<>
def xxx(id):
    return f'hello {id}'


@app.route('/login/')
def login():
    return '请登录'


@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return '欢迎来到知识问答页面'
    else:
        return redirect(url_for('login'))


if __name__=='__main__':
    app.run(debug=True)