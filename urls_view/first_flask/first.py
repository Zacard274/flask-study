from flask import Flask
from first_flask import config

app = Flask(__name__)
app.config.from_object(config)  #使用配置文件设置参数

@app.route('/')
def hello_world():
    return 'hello abc'

if __name__ == '__main__':
    app.run()