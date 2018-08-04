import urllib
from flask import Flask,url_for, redirect, request
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class ListConverter(BaseConverter):    #定义子类ListConverter，继承BaseConverter类

    def __init__(self,url_map,separator='+'):         #先继承，再重构
        super(ListConverter,self).__init__(url_map)   #继承父类的属性url_map，等同于BaseConverter.__init__(self,url_map)
        self.separator=urllib.parse.unquote(separator)      #设置自己的属性separator,urllib.unquote():字符串/字典被当作url提交时会被自动进行url编码处理
                                                      # separator='+',即将'+‘作为url提交时将对其进行url编码处理
    def to_python(self,value):
        return value.split(self.separator)            #split()分割，以‘+’为分割点

    def to_url(self,values):
        return self.separator.join(BaseConverter.to_url(value) for value in values)   #输入的values经url处理后 以‘+’相连

app.url_map.converters['list']=ListConverter

@app.route('/list1/<list:page_names>/')              #把page_names传入ListConverter类，即to_url处理
def list1(page_names):
    return 'Separator : {} {}'.format('+',page_names)

@app.route('/list2/<list(separator=u"|"):page_names>/')
def list2(page_names):
    return 'Separator : {} {}'.format('|',page_names)

@app.route("/")
def hello_world():
    return 'hello world'

@app.route('/get')
def reture_a():
    return 'a'

@app.route('/xman/<int:id>/')   #尖括号中的内容是动态的，凡匹配到/xman/前缀的URL都会被映射到这个路由上，'int:'表示只接受整数，<id>默认接受不含/的str
def xman(id):
    return f'id is {id}'

@app.route('/item/')
def item():
    return (url_for("address", arg="1"))  #/test1/?arg=1

@app.route('/test1/')      #尖括号中的内容是动态的，凡匹配到/item/前缀的URL都会被映射到这个路由上，'int:'表示只接受整数，<id>默认接受不含/的str
def address():
    return "arg"
app.run()


