from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    comments = [
        {
            'user': '路人1',
            'content': 'abc'
        },
        {
            'user': '路人2',
            'content': 'nmm'
        }
    ]
    return render_template('index.html', avatar='https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3546879296,3345703961&fm=173&app=25&f=JPEG?w=218&h=146&s=8F8C94451EEB573C5A95A8A90300701B',comments=comments)

#如果没有avatar=xxx，就显示默认图片，详见index.html的default过滤器

if __name__ == '__main__':
    app.run(debug=True)