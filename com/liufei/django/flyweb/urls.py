'''
urls：路由分发

我们代码中有一个列表，根据不同的路径执行不同的函数，这个列表就称为路由分发，所以要单独设立一个文件。
'''

import views

request_list = [
    ('/', views.html),
    ('/static/css/test.css', views.css),
    ('/static/img/mv.jpeg', views.jpeg),
    ('/static/js/test.js', views.js),
    ('/static/img/favicon.icon', views.jd),
]
