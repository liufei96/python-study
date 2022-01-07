# 内置函数Ⅱ,闭包,装饰器初识
# 1. 匿名函数
# 匿名函数，顾名思义就是没有名字的函数，那么什么函数没有名字呢？这个就是我们以后面试或者工作中经常用匿名函数 lambda，也叫一句话函数。
#
# 现在有一个需求：你们写一个函数，此函数接收两个int参数，返回和值。

def func(a, b):
    return a + b


print(func(3, 4))  # 7

# 那么接下来我们用匿名函数完成上面的需求：

func = lambda a, b: a + b
print(func(4, 5))  # 9

'''
我们分析一下上面的代码：
语法:
　　函数名 = lambda 参数:返回值
    1）此函数不是没有名字，他是有名字的，他的名字就是你给其设置的变量，比如func.
    2）lambda 是定义匿名函数的关键字，相当于函数的def.
    3）lambda 后面直接加形参，形参加多少都可以，只要用逗号隔开就行。
    4）返回值在冒号之后设置，返回值和正常的函数一样,可以是任意数据类型。
    5）匿名函数不管多复杂.只能写一行.且逻辑结束后直接返回数据
'''

func = lambda a, b, *args, sex='alex', c, **kwargs: kwargs
print(func(3, 4, c=666, name='alex'))  # {'name': 'alex'}
# 所有类型的形参都可以加，但是一般使用匿名函数只是加位置参数，其他的用不到。

# 接下来做几个匿名函数的小题：
#
# 写匿名函数：接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）。

func = lambda x: (x[0], x[2])
print(func('afafasd'))  # ('a', 'a')

# 写匿名函数：接收两个int参数，将较大的数据返回。
# func = lambda a, b: max(a, b)
func = lambda x, y: x if x > y else y
print(func(4, 9))

# 2. 内置函数Ⅱ
print('2. 内置函数Ⅱ'.center(30, '*'))
# 红色重点讲解：abs() enumerate() filter() map() max() min() open() range() print() len() list() dict() str() reversed() set() sorted() sum() tuple() type() zip() dir()
# 昨天，我们已经比较重要的内置函数讲完了，那么今天我们要讲的是最最重要的内置函数，这些内置函数是面试与工作中经常用到的，所以，今天的这些内置函数，我们一定要全部记住，并且熟练使用。

print('print() 屏幕输出。'.center(30, '*'))
# print() 屏幕输出。
''' 源码分析
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    file:  默认是输出到屏幕，如果设置为文件句柄，输出到文件
    sep:   打印多个值之间的分隔符，默认为空格
    end:   每一次打印的结尾，默认为换行符
    flush: 立即把内容输出到流文件，不作缓存
    """
'''
print(111, 222, 333, sep='*')  # 111*222*333
print(111, end='!')  # 111!
print(222)  # 两行的结果 111!222

f = open('file', 'w', encoding='utf-8')
print('写入文件', file=f, flush=True)  # 替换文件中的内容

# int():pass
#
# str():pass
#
# bool():pass
#
# set(): pass
#
# list() 将一个可迭代对象转换成列表
#
# tuple() 将一个可迭代对象转换成元组
#
# dict() 通过相应的方式创建字典。

l1 = list('abcd')
print(l1)  # ['a', 'b', 'c', 'd']
tu1 = tuple('abcd')
print(tu1)  # ('a', 'b', 'c', 'd')

# abs() 返回绝对值
print('abs() 返回绝对值'.center(30, '*'))
i = -5
print(abs(i))  # 5

# sum() 求和
print('sum() 求和'.center(30, '*'))
print(sum([1, 2, 3]))
print(sum((1, 2, 3), 100))

# min() 求最小值
print('min() 求最小值'.center(30, '*'))

print(min([1, 2, 3]))  # 返回此序列最小值
ret = min([1, 2, -5, ], key=abs)  # 按照绝对值的大小，返回此序列最小值
print(ret)  # 1
# 加key是可以加函数名，min自动会获取传入函数中的参数的每个元素，然后通过你设定的返回值比较大小，返回最小的传入的那个参数。
print(min(1, 2, -5, 6, -3, key=lambda x: abs(x)))  # 可以设置很多参数比较大小  # 1
dic = {'a': 3, 'b': 2, 'c': 1}
print(min(dic, key=lambda x: dic[x]))  # c
# x为dic的key，lambda的返回值（即dic的值进行比较）返回最小的值对应的键

# max() 最大值与最小值用法相同。

# reversed() 将一个序列翻转, 返回翻转序列的迭代器 reversed 示例:
print('reversed() 将一个序列翻转, 返回翻转序列的迭代器 reversed 示例:'.center(30, '*'))
l = reversed('你好')  # l 获取到的是一个生成器
print(list(l))  # ['好', '你']
ret = reversed([1, 4, 3, 7, 9])
print(list(ret))  # [9, 7, 3, 4, 1]

# bytes() 把字符串转换成bytes类型
s = '你好liufei'
bs = s.encode('utf-8')
print(bs)  # b'\xe4\xbd\xa0\xe5\xa5\xbdliufei'

s1 = bs.decode('utf-8')

# 将字符串转换成字节
s = '你好'
bs = bytes(s, encoding='utf-8')
print(bs)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

bs1 = str(bs, encoding='utf-8')
print(bs1)  # 你好

# zip() 拉链方法。函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,
# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回，

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c', 'd']
lst3 = (11, 12, 13, 14, 15)

for i in zip(lst1, lst2, lst3):
    print(i)

# (1, 'a', 11)
# (2, 'b', 12)
# (3, 'c', 13)

# sorted排序函数
print('sorted排序函数'.center(30, '*'))
'''
语法:sorted(iterable,key=None,reverse=False)

iterable : 可迭代对象

key: 排序规则(排序函数),在sorted内部会将可迭代对象中的每一个元素传递给这个函数的参数.根据函数运算的结果进行排序

reverse :是否是倒叙,True 倒叙 False 正序
'''

lst = [1, 3, 2, 5, 4]
lst2 = sorted(lst)
print(lst)  # [1, 3, 2, 5, 4]  #原列表不会改变
print(lst2)  # [1, 2, 3, 4, 5] #返回的新列表是经过排序的

lst3 = sorted(lst, reverse=True)
print(lst3)  # 倒叙 # [5, 4, 3, 2, 1]

# 字典使用sorted排序
dic = {1: 'a', 3: 'c', 2: 'b'}
print(sorted(dic))  # [1, 2, 3] #  字典排序返回的就是排序后的key

# 和函数组合使用
# 定义一个列表,然后根据一元素的长度排序
lst = ['天龙八部', '西游记', '红楼梦', '三国演义']


# 计算字符串的长度
def func(s):
    return len(s)


print(sorted(lst, key=func))  # ['西游记', '红楼梦', '天龙八部', '三国演义']

# 和lambda组合使用
lst = ['天龙八部', '西游记', '红楼梦', '三国演义']
print(sorted(lst, key=lambda s: len(s)))  # ['西游记', '红楼梦', '天龙八部', '三国演义']

lst = [{'id': 1, 'name': 'alex', 'age': 18},
       {'id': 2, 'name': 'wusir', 'age': 17},
       {'id': 3, 'name': 'taibai', 'age': 16}, ]

# 按照年龄对学生信息进行排序
print(sorted(lst, key=lambda item: item[
    'age']))  # [{'id': 3, 'name': 'taibai', 'age': 16}, {'id': 2, 'name': 'wusir', 'age': 17}, {'id': 1, 'name': 'alex', 'age': 18}]

# filter筛选过滤
print('filter筛选过滤'.center(30, '*'))
'''
语法: filter(function,iterable)
function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,然后根据function返回的True或者False来判断是否保留此项数据
iterable:可迭代对象
'''

lst = [{'id': 1, 'name': 'alex', 'age': 18},
       {'id': 1, 'name': 'wusir', 'age': 17},
       {'id': 1, 'name': 'taibai', 'age': 16}, ]

ls = filter(lambda e: e['age'] > 16, lst)
print(ls)  # <filter object at 0x0000018B1565E2E0>
print(list(ls))  # [{'id': 1, 'name': 'alex', 'age': 18}, {'id': 1, 'name': 'wusir', 'age': 17}]

# map
'''
映射函数

语法: map(function,iterable) 可以对可迭代对象中的每一个元素进映射,分别取执行function

计算列表中每个元素的平方,返回新列表
'''
print('map'.center(30, '*'))
lst = [1, 2, 3, 4, 5]


def func(s):
    return s * s


map1 = map(func, lst)
print(map1)  # <map object at 0x000002BB592FF400>
print(list(map1))  # [1, 4, 9, 16, 25]

# 改写成lambda
# lst = [1,2,3,4,5]
print(list(map(lambda s: s * s, lst)))

# 计算两个列表中相同位置的数据的和
lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8, 10]

print(list(map(lambda x, y: x + y, lst1, lst2)))

# reduce
print('reduce'.center(30, '*'))

from functools import reduce


def func(x, y):
    return x + y


# reduce 的使用方式:
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行

ret = reduce(func, [3, 4, 5, 6, 7])
print(ret)  # 25

'''
reduce的作用是先把列表中的前俩个元素取出计算出一个值然后临时保存着,
接下来用这个临时保存的值和列表中第三个元素进行计算,求出一个新的值将最开始
临时保存的值覆盖掉,然后在用这个新的临时值和列表中第四个元素计算.依次类推
'''

'''
注意:我们放进去的可迭代对象没有更改
以上这个例子我们使用sum就可以完全的实现了.我现在有[1,2,3,4]想让列表中的数变成1234,就要用到reduce了.
普通函数版
'''


def func(x, y):
    return x * 10 + y
    # 第一次的时候 x是1 y是2  x乘以10就是10,然后加上y也就是2最终结果是12然后临时存储起来了
    # 第二次的时候x是临时存储的值12 x乘以10就是 120 然后加上y也就是3最终结果是123临时存储起来了
    # 第三次的时候x是临时存储的值123 x乘以10就是 1230 然后加上y也就是4最终结果是1234然后返回了


l = reduce(func, [1, 2, 3, 4])
print(l)  # 1234

# 匿名函数版
l = reduce(lambda x, y: x * 10 + y, [1, 2, 3, 4])
print(l)  # 1234

'''
在Python2.x版本中recude是直接 import就可以的, Python3.x版本中需要从functools这个包中导入

龟叔本打算将 lambda 和 reduce 都从全局名字空间都移除, 舆论说龟叔不喜欢lambda 和 reduce

最后lambda没删除是因为和一个人写信写了好多封,进行交流然后把lambda保住了.
'''

# 3.闭包

'''
由于闭包这个概念比较难以理解，尤其是初学者来说，相对难以掌握，所以我们通过示例去理解学习闭包。

给大家提个需求，然后用函数去实现：完成一个计算不断增加的系列值的平均值的需求。

例如：整个历史中的某个商品的平均收盘价。什么叫平局收盘价呢？就是从这个商品一出现开始，每天记录当天价格，然后计算他的平均值：平均值要考虑直至目前为止所有的价格。

比如大众推出了一款新车：小白轿车。
第一天价格为：100000元，平均收盘价：100000元
第二天价格为：110000元，平均收盘价：（100000 + 110000）/2 元
第三天价格为：120000元，平均收盘价：（100000 + 110000 + 120000）/3 元
........

'''

series = []


def make_averager(new_value):
    series.append(new_value)
    total = sum(series)
    return total / len(series)


print(make_averager(100000))  # 100000.0
print(make_averager(110000))  # 105000.0
print(make_averager(120000))  # 110000.0

'''
从上面的例子可以看出，基本上完成了我们的要求，但是这个代码相对来说是不安全的，因为你的这个series列表是一个全局变量，只要是全局作用域的任何地方，
都可能对这个列表进行改变。
'''

print(make_averager(100000))
print(make_averager(110000))
series.append(666)  # 如果对数据进行相应改变，那么你的平均收盘价就会出现很大的问题。
print(make_averager(120000))


# 那么怎么办呢？有人说，你把他放在函数中不就行了，这样不就是局部变量了么？数据不就相对安全了么？

def make_averager(new_value):
    series = []
    series.append(new_value)
    total = sum(series)
    return total / len(series)


print(make_averager(100000))  # 100000.0
print(make_averager(110000))  # 110000.0
print(make_averager(120000))  # 120000.0


# 这样计算的结果是不正确的,那是因为执行函数，会开启一个临时的名称空间，随着函数的结束而消失，所以你每次执行函数的时候，都是重新创建这个列表，
# 那么这怎么做呢？这种情况下，就需要用到我们讲的闭包了，我们用闭包的思想改一下这个代码。

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10000))  # 10000.0
print(avg(11000))  # 10500.0
print(avg(12000))  # 11000.0

'''
大家仔细看一下这个代码，我是在函数中嵌套了一个函数。那么avg 这个变量接收的实际是averager函数名，也就是其对应的内存地址，我执行了三次avg 也就是执行了三次averager这个函数。那么此时你们有什么问题？

肯定有学生就会问，那么我的make_averager这个函数只是执行了一次，为什么series这个列表没有消失？反而还可以被调用三次呢？这个就是最关键的地方，也是闭包的精华所在。我给大家说一下这个原理，以图为证：
'''

'''
闭包的定义：
    1. 闭包是嵌套在函数中的函数。
    2. 闭包必须是内层函数对外层函数的变量（非全局变量）的引用。
如何判断判断闭包？举例让同学回答：
'''


# 例一：
def wrapper():
    a = 1

    def inner():
        print(a)

    return inner


ret = wrapper()

# 例二：
a = 2


def wrapper():
    def inner():
        print(a)

    return inner


ret = wrapper()


# 例三：
def wrapper(a, b):
    def inner():
        print(a)
        print(b)

    return inner


a = 2
b = 3
ret = wrapper(a, b)

'''
以上三个例子，最难判断的是第三个，其实第三个也是闭包，如果我们每次去研究代码判断其是不是闭包，有一些不科学，或者过于麻烦了，
那么有一些函数的属性是可以获取到此函数是否拥有自由变量的，如果此函数拥有自由变量，那么就可以侧面证明其是否是闭包函数了（了解）：
'''


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()

# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)

# 当然还有一些参数，仅供了解：
# 函数名.__code__.co_varnames 查看函数的局部变量
print(avg.__code__.co_varnames)  # ('new_value', 'total')

# 函数名.__closure__ 获取具体的自由变量对象，也就是cell对象。
print(avg.__closure__[0].cell_contents)  # []

'''
闭包的作用：保存局部信息不被销毁，保证数据的安全性。
闭包的应用：
    1. 可以保存一些非全局变量但是不易被销毁、改变的数据。
    2. 装饰器。
'''
