print('from the liufei.py')
name = '刘飞'

def read1():
    print('liufei模板', name)


def read2():
    print('刘飞模块')
    read1()

def change():
    global name
    name = 'barry'