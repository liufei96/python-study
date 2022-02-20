# manage文件：专门放置服务器程序的代码，处理http协议，socket等。

from getMydata import get_data
from jinja2 import Template
from wsgiref.simple_server import make_server

def html():
    from_mysql_data = get_data()
    with open('./templates/flytemp.html', encoding='utf-8') as f1:
        data = f1.read()
    temp = Template(data)
    temp_data = temp.render({'userinfo': from_mysql_data})
    return temp_data.encode('utf-8')

def css():
    with open('./static/test.css', mode='rb') as f2:
        data = f2.read()
    return data


def jpeg():
    with open('./static/mv.jpeg', mode='rb') as f3:
        data = f3.read()
    return data


def js():
    with open('./static/test.js', mode='rb') as f4:
        data = f4.read()
    return data


def jd():
    with open('./static/favicon.ico', mode='rb') as f5:
        data = f5.read()
    return data

request_list = [
    ('/', html),
    ('/test.css', css),
    ('/mv.jpeg', jpeg),
    ('/test.js', js),
    ('/jd.ico', jd),
]

def application(environ, start_response):

    start_response('200 OK', [('k1', 'v1'), ('k2', 'v2')])
    print(environ)
    request_path = environ['PATH_INFO']
    for i in request_list:
        if request_path == i[0]:
            ret = i[1]()
            return [ret]
    else:

        return [b'<h1>404.....</h1>']




httpd = make_server('127.0.0.1', 8080, application)
print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()