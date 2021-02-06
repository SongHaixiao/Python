# Flask 基础框架优化

用python 实现 flask 启动 **app.run(host='0.0.0.0',port=5000)**

用python开启flask web服务时，有一下两种情况：

#### 1. 只需要本机访问时

**ip 只要不设置为0.0.0.0就可以，正常访问就好,即不带有 host 值**

```python
from flask import Flask     # 导入 flask 扩展中的 Flask 类
app = Flask(__name__)       # 定一个变量 app，并传递参数 __name__ 

@app.route("/")             # 名字为路由的装饰器，传入变量 /(pass)
def hello():                # 定义一个名为 hello 的函数
    return "Hello World!"   # 返回字符串 Hello World!

if __name__ == "__main__":
    app.run( debug=True) # 添加外网访问
```

#### 2. 需要访问外网时

**ip需要设置为0.0.0.0，即，host 值 需要设置为 0.0.0.0**

**此时，在本机上访问需要使用默认的127.0.0.1（也就是不设置ip时默认的ip）,在外网上访问则需要使用本机的ip，不要使用0.0.0.0。**

```python
from flask import Flask     # 导入 flask 扩展中的 Flask 类
app = Flask(__name__)       # 定一个变量 app，并传递参数 __name__ 

@app.route("/")             # 名字为路由的装饰器，传入变量 /(pass)
def hello():                # 定义一个名为 hello 的函数
    return "Hello World!"   # 返回字符串 Hello World!

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) # 添加外网访问
```

注意

```python
arr.run(host="0.0.0.0", debug=True)
```

 

这种是不太推荐的启动方式，这只做演示用，具体看 [官方启动方式参见链接](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)
