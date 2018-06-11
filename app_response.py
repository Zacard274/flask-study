from flask import Flask
from werkzeug.wrapper import Response
app=Flask(__name__)

class JSONResponse(Response):
    @classmethod   #用于装饰类方法，调用某个类的方法时，直接用类而不是实例去调用：可以直接调用JSONResponse.force_type
    def force_type(cls,rv,environ=None):
        if isinstance(rv,dict):   #isinstance()判断rv是否是dict
            rv=jsonify(rv)        #将dict类型转换为json串
        return super(JSONResponse,cls).force_type(rv,environ)

app.response_class=JSONResponse

@app.route('/')
def hello_world():
    return {'message':'Hello World!'}

@app.route(',custom_headers')
def headers():
    return {'headers':[1,2,3]},201,[('X_Request-Id','100')]

if __name__ == '__main__':
    app.run()
