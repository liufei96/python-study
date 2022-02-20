
# https://www.cnblogs.com/jin-xin/articles/12243188.html

# import socket
# server = socket.socket()
# server.bind(('127.0.0.1', 8002))
# server.listen()

# while 1:
#     conn, addr = server.accept()
#     while 1:
#         client_data = conn.recv(1024).decode('utf-8')
#         print(client_data)
#         # 服务端与客户端建立联系必须要遵循一个协议，此时我们用http协议示例。
#         conn.send('HTTP/1.1 200 OK \r\n\r\n'.encode('utf-8'))
#         # conn.send('<h1>hello</h1>'.encode('utf-8'))
#         with open('demo_upgrade.html', mode='rb') as f1:
#             conn.send(f1.read())
#     conn.close()

# 我们通过浏览器请求服务端，服务端给我们返回一个hello标签。客户端请求过来之后，要想让服务端给客户端返回消息，必须基于一个协议，我们用http协议示例。那么服务端如果返回给浏览器一个页面呢？
# 这么我们发现一个问题，当你的浏览器访问服务端时，服务端会接受到这些信息：

'''
Connected to pydev debugger (build 211.7142.13)
GET / HTTP/1.1
Host: 127.0.0.1:8002
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
'''

'''
这些是什么信息？这是因为服务端与客户端遵循http协议，这是协议做的事情，所以在我们研究web框架之前，必不可少的需要研究一下这个协议，协议到底做了什么事情。

http协议详见：xxxxx.
'''

# 3. http协议具体研究
print('3. http协议具体研究 '.center(30, '='))

'''
3.1 请求步骤

1. 建立链接：客户端连接到Web服务器。
一个HTTP客户端，通常是浏览器，与Web服务器的HTTP端口（默认为80）建立一个TCP套接字连接。例如，http://www.baidu.com。

2. 发送HTTP请求
通过TCP套接字，客户端向Web服务器发送一个文本的请求报文，一个请求报文由请求行、请求头部、空行和请求数据4部分组成。

这里分不同的请求，主要是get、post请求。

首先看get请求：

更改一下我们的html页面：
'''

# GET http://127.0.0.1:8002/?username=liufei&password=123

'''
GET /?username=liufei&password=123 HTTP/1.1
Host: 127.0.0.1:8002
Connection: keep-alive
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
'''

# 此时你发送的是post请求，服务器接受到的消息为：

'''
4. 释放连接TCP连接
若connection 模式为close，则服务器主动关闭TCP连接，客户端被动关闭连接，释放TCP连接;若connection 模式为keepalive，则该连接会保持一段时间，在该时间内可以继续接收请求;

5. 客户端浏览器解析HTML内容
客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。然后解析每一个响应头，响应头告知以下为若干字节的HTML文档和文档的字符集。客户端浏览器读取响应数据HTML，根据HTML的语法对其进行格式化，并在浏览器窗口中显示。
'''

#  3.2 重要知识点
#  URL、请求方式、http协议的特点，请求流程，请求格式，响应格式。响应状态码等。

print('post与get请求的区别：'.center(30, '='))
'''
GET提交的数据会放在URL之后，也就是请求行里面，以?分割URL和传输数据，参数之间以&相连，如EditBook?name=test1&id=123456.（请求头里面那个content-type做的这种参数形式，后面讲） 
POST方法是把提交的数据放在HTTP包的请求体中.

GET提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST方法提交的数据没有限制.

GET与POST请求在服务端获取请求数据方式不同，就是我们自己在服务端取请求数据的时候的方式不同了，这句废话昂。
常用的get请求：浏览器输入网址，a标签，form标签默认get请求。
常用的post请求：一般就是用来提交数据，比如用户名密码登录。
'''

# 二、构建web框架
print('二、构建web框架'.center(30, '='))


'''
虽然浏览器发送了四个请求，但是我们统一回复的就是一个html页面，相当于我们重复回复了4次同一个html页面，这也导致了我们的页面没有css，js的效果：

所以我们应该怎么做？对不同的请求返回给不同的文件资源，比如他请求的css文件，我们就返回css文件资源，这样页面就有了更加丰富的样式。那么如何区分他的请求呢？就是通过每次请求的第一行的请求路径，所以我们应该把每次的请求路径分割，根据不同的请求路径，返回给其不同的文件资源。
'''
# import socket
# server = socket.socket()
# server.bind(('127.0.0.1', 8002))
# server.listen()

# while 1:
#     conn, addr = server.accept()
#     client_data = conn.recv(1024)
#     request_path = client_data.decode('utf-8').split('\r\n')[0].split()[1]
#     # 服务端与客户端建立联系必须要遵循一个协议，此时我们用http协议示例。
#     conn.send('HTTP/1.1 200 OK \r\nk1:v1\r\n\r\n'.encode('utf-8'))
#     if request_path == '/':
#         with open('demo_upgrade.html', mode='rb') as f1:
#             conn.send(f1.read())
#     elif request_path == '/test.css':
#         with open('test.css', mode='rb') as f1:
#             conn.send(f1.read())
#     elif request_path == '/mv.jpeg':
#         with open('mv.jpeg', mode='rb') as f1:
#             conn.send(f1.read())
#     elif request_path == '/test.js':
#         with open('test.js', mode='rb') as f1:
#             conn.send(f1.read())
#     elif request_path == '/favicon.ico':
#         with open('favicon.ico', mode='rb') as f1:
#             conn.send(f1.read())
#     conn.close()

'''
favicon.ico 就是窗口小图标，浏览器一直会向服务器发送请求。
图片的索取与文件是一样的，也就是通过路径索取资源。

这样升级版web框架我们就完成了。
'''

# 2.3 函数版web框架
print('2.3 函数版web框架'.center(30, '='))
'''
上一个版本用了多个if elif elif....... 这种方式比较low，并且代码应该整合成函数而不能使用纯面向过程方式，所以我们进行改版：
'''

# import socket
# server = socket.socket()
# server.bind(('127.0.0.1', 8002))
# server.listen()
#
# def html(conn):
#     with open('04 函数进阶版html.html', mode='rb') as f1:
#         conn.send(f1.read())
#         conn.close()
#
# def css(conn):
#     with open('test.css', mode='rb') as f1:
#         conn.send(f1.read())
#         conn.close()
#
# def js(conn):
#     with open('test.js', mode='rb') as f1:
#         conn.send(f1.read())
#         conn.close()
#
# def jpeg(conn):
#     with open('mv.jpeg', mode='rb') as f1:
#         conn.send(f1.read())
#         conn.close()
#
# def jd(conn):
#     with open('favicon.ico', mode='rb') as f1:
#         conn.send(f1.read())
#         conn.close()
#
# request_list = [
#     ('/', html),
#     ('/test.css', css),
#     ('/mv.jpeg', jpeg),
#     ('/test.js', js),
#     ('/jd.ico', jd),
# ]
#
# while 1:
#     conn, addr= server.accept()
#     client_data = conn.recv(1024)
#     request_path = client_data.decode('utf-8').split('\r\n')[0].split()[1]
#     # 服务端与客户端建立联系必须要遵循一个协议，此时我们用http协议示例。
#     conn.send('HTTP/1.1 200 OK \r\nk1:v1\r\n\r\n'.encode('utf-8'))
#     for i in request_list:
#         if request_path == i[0]:
#             i[1](conn)
#     conn.close()

'''
虽然这个这个版本感觉更加简洁明了了，但是这个版本还是不完美，现在虽然是异步处理请求，但是上一阶段我们学完并发，
我们对于这些异步请求应该用并发处理更加合理。
'''

# 2.4 并发版web框架
print('2.4 并发版web框架'.center(30, '='))
# 此时我们要加上多线程处理浏览器发送过来的请求。

# import socket
# import time
# from threading import Thread
# server = socket.socket()
# server.bind(('127.0.0.1', 8002))
# server.listen()
#
# def html(conn):
#     time_now = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
#     with open('05 并发版web框架html.html',encoding='utf-8') as f1:
#         data = f1.read().format(time_now=time_now)
#     conn.send(data.encode('utf-8'))
#     conn.close()
#
#
# def css(conn):
#     with open('test.css', mode='rb') as f2:
#         data = f2.read()
#     conn.send(data)
#     conn.close()
#
#
# def jpeg(conn):
#     with open('mv.jpeg', mode='rb') as f3:
#         data = f3.read()
#     conn.send(data)
#     conn.close()
#
# def js(conn):
#     with open('test.js', mode='rb') as f4:
#         data = f4.read()
#     conn.send(data)
#     conn.close()
#
# def jd(conn):
#     with open('favicon.ico', mode='rb') as f5:
#         data = f5.read()
#     conn.send(data)
#     conn.close()
#
# request_list = [
#     ('/', html),
#     ('/test.css', css),
#     ('/mv.jpeg', jpeg),
#     ('/test.js', js),
#     ('/jd.ico', jd),
# ]
# while 1:
#     conn, addr = server.accept()
#     client_data = conn.recv(1024)
#     request_path = client_data.decode('utf-8').split('\r\n')[0].split()[1]
#     print(request_path)
#     # 服务端与客户端建立联系必须要遵循一个协议，此时我们用http协议示例。
#     conn.send('HTTP/1.1 200 OK \r\n\r\n'.encode('utf-8'))
#     # 只要有一个线程处理conn管道，accept就会接受新的请求创建另一个管道
#     for i in request_list:
#         if request_path == i[0]:
#             t = Thread(target=i[1], args=(conn,))
#             t.start()
    # conn.close()


# 2.6 wsgiref模块版+数据库web框架
print('2.6 wsgiref模块版+数据库web框架'.center(40, '='))

'''
wsgiref模块其实就是将整个请求信息给封装了起来，就不需要你自己处理了，假如它将所有请求信息封装成了一个叫做request的对象，
那么你直接request.path就能获取到用户这次请求的路径，request.method就能获取到本次用户请求的请求方式(get还是post)等，
那这个模块用起来，我们再写web框架是不是就简单了好多啊。

　　对于真实开发中的python web程序来说，一般会分为两部分：服务器程序和应用程序。

服务器程序负责对socket服务器进行封装，并在请求到来时，对请求的各种数据进行整理。

　　应用程序则负责具体的逻辑处理。为了方便应用程序的开发，就出现了众多的Web框架，例如：Django、Flask、web.py 等。不同的框架有不同的开发方式，但是无论如何，开发出的应用程序都要和服务器程序配合，才能为用户提供服务。

　　这样，服务器程序就需要为不同的框架提供不同的支持。这样混乱的局面无论对于服务器还是框架，都是不好的。对服务器来说，需要支持各种不同框架，对框架来说，只有支持它的服务器才能被开发出的应用使用。最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

　　正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口协议来实现这样的服务器软件，让我们专心用Python编写Web业务。

　　这时候，标准化就变得尤为重要。我们可以设立一个标准，只要服务器程序支持这个标准，框架也支持这个标准，那么他们就可以配合使用。一旦标准确定，双方各自实现。这样，服务器可以支持更多支持标准的框架，框架也可以使用更多支持标准的服务器。

　　WSGI（Web Server Gateway Interface）就是一种规范，它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦。

　　常用的WSGI服务器有uwsgi、Gunicorn。而Python标准库提供的独立WSGI服务器叫wsgiref，Django开发环境用的就是这个模块来做服务器。
'''

# 接下来我们先看一看wsgiref的简单用法：

# from wsgiref.simple_server import make_server
# # wsgiref本身就是个web框架，提供了一些固定的功能（请求和响应信息的封装，不需要我们自己写原生的socket了也不需要咱们自己来完成请求信息的提取了，提取起来很方便）
# # 函数名字随便起
# def application(environ, start_response):
#     '''
#     :param environ: 是全部加工好的请求信息，加工成了一个字典，通过字典取值的方式就能拿到很多你想要拿到的信息
#     :param start_response: 帮你封装响应信息的（响应行和响应头），注意下面的参数
#     :return:
#     '''
#     start_response('200 ok', [('k1','v1'),])
#     print(environ)
#     print(environ['PATH_INFO'])  # 输入地址127.0.0.1:8000，这个打印的是'/',输入的是127.0.0.1:8000/index，打印结果是'/index'
#     return [b'<h1>Hello Web!</h1>']
#
# # 和咱们学的socketserver那个模块很像啊
# httpd = make_server('127.0.0.1', 8080, application)
#
# print('Serving HTTP on port 8080...')
#
# # 开始监听HTTP请求:
#
# httpd.serve_forever()

print('-------------- 配置数据库 -----------')

# 配置数据库：
#
# 利用pymysql先创建一个表：

import pymysql

conn = pymysql.connect(
    host='192.168.220.130',
    port=3306,
    user='root',
    password='123456',
    database='test',
    charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)
# sql = 'create table userinfo(id int primary key auto_increment, name varchar(128), age int not null);'
#
# cursor.execute(sql)
# conn.commit()


# sql = 'insert into userinfo(name, age) values("liufei", 27);'
# cursor.execute(sql)
# conn.commit()

# 这样你成功的在数据库创建并插入了一些数据，然后就是三个文件了：

# 2.7 wsgiref模块版+数据库+jinja2 web框架
print('2.7 wsgiref模块版+数据库+jinja2 web框架'.center(50, '='))

'''
上面的代码实现了一个简单的动态页面(字符串替换)，我完全可以从数据库中查询数据，然后去替换我html中的对应内容（专业名词叫做模板渲染，你先渲染一下，再给浏览器进行渲染），然后再发送给浏览器完成渲染。 
这个过程就相当于HTML模板渲染数据。 
本质上就是HTML内容中利用一些特殊的符号来替换要展示的数据。 我这里用的特殊符号是我定义的，其实模板渲染有个现成的工具： 
jinja2，DJango有自带的模版渲染方法，和jinja2很像，但是只能适用于Django框架，而jinja2可以适用于多种框架。

下载：

'''

import pymysql

def get_data():
    conn = pymysql.connect(
        host='192.168.220.130',
        port=3306,
        user='root',
        password='123456',
        database='test',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 获取所有数据
    cursor.execute("select * from userinfo;")
    data = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return data


from jinja2 import Template
from wsgiref.simple_server import make_server

def html():
    from_mysql_data = get_data()
    with open('08 wsgiref版+数据库+jinja2html.html', encoding='utf-8') as f1:
        data = f1.read()
    temp = Template(data)
    temp_data = temp.render({'userinfo': from_mysql_data})
    return temp_data.encode('utf-8')

def css():
    with open('test.css', mode='rb') as f2:
        data = f2.read()
    return data


def jpeg():
    with open('mv.jpeg', mode='rb') as f3:
        data = f3.read()
    return data


def js():
    with open('test.js', mode='rb') as f4:
        data = f4.read()
    return data


def jd():
    with open('favicon.ico', mode='rb') as f5:
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

# 2.8 起飞版web框架
print('2.8 起飞版web框架'.center(30, '='))

'''
上面所有的还不能称为一个框架，真正的框架是分文件开发，也就是咱们在规范化格式目录时学习过的，不同的文件拥有不同的功能，真正的框架就是要分文件各司其职。
'''