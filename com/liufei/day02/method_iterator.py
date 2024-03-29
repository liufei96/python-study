# 迭代器(函数名使用,新版格式化输出)
# 1. 函数名的运用

'''
你们说一下，按照你们的理解，函数名是什么？
    函数名的定义和变量的定义几乎一致，在变量的角度，函数名其实就是一个变量，具有变量的功能：可以赋值；但是作为函数名他也有特殊的功能就是加上()就会执行对应的函数，所以我们可以把函数名当做一个特殊的变量，
    那么接下来，我们就来研究一下这个特殊的变量。
'''

# 1.1 函数的内存地址
print('1.1 函数的内存地址'.center(30, '*'))


def func():
    print('呵呵')


print(func)  # <function func at 0x000001921F1E2790>

# 通过上面代码可以我们知道，函数名指向的是这个函数的内存地址，其实深一步理解可得知，与其说函数名()可以执行这个函数，不如说是函数的内存地址()才是执行这个函数的关键，就好比：
a = 1
b = 2
c = a + b
print(c)  # 3

# a + b 并不是变量的相加，而是 两个变量指向的int对象的相加。

print('1.2 函数名可以赋值给其他变量'.center(30, '*'))


# 1.2 函数名可以赋值给其他变量
def func():
    print("呵呵")


print(func)
a = func  # 把函数当成一个变量赋值给另一个变量
a()  # 函数调用 func()
# 通过变量的赋值，变量a，和变量func都指向的这个函数的内存地址，那么a() 当然可以执行这个函数了。

print('1.3 函数名可以当做容器类的元素'.center(30, '*'))


# 1.3 函数名可以当做容器类的元素
# 其实这个也不难理解，函数名就是一个变量，我的变量是可以当做容器类类型的元素的：

def func1():
    print("in func1: 嘻嘻")


def func2():
    print("in func2: 哈哈")


def func3():
    print("in func3: 咯咯")


def func4():
    print("in func4: 吱吱")


list = [func1, func2, func3, func4]
for i in list:
    i()

print('n1.4 函数名可以当做函数的参数'.center(30, '*'))


# 1.4 函数名可以当做函数的参数
# 变量可以做的，函数名都可以做到。

def func1():
    print('in func1')


def func2(f):
    print('in func2')
    f()


func2(func1)

print('1.5 函数名可以作为函数的返回值'.center(30, '*'))


def func1():
    print('in func1')


def func2(f):
    print('in func2')
    return f


ret = func2(func1)
ret()  # ret, f, func1 都是指向的func1这个函数的内存地址

# 小结：函数名是一个特殊的变量，他除了具有变量的功能，还有最主要一个特点就是加上() 就执行，其实他还有一个学名叫第一类对象。

# 2 Python新特性：f-strings格式化输出
'''
f-strings 是python3.6开始加入标准库的格式化输出新的写法，这个格式化输出比之前的%s 或者 format 效率高并且更加简化，非常的好用，相信我，你们学完这个之后，以后再用格式化输出这就是你们唯一的选择。
'''
print('2 Python新特性：f-strings格式化输出'.center(30, '*'))
# 2.1 简单举例
# 他的结构就是F(f)+ str的形式，在字符串中想替换的位置用{}展位，与format类似，但是用在字符串后面写入替换的内容，而他可以直接识别。碉堡了。
name = '刘飞'
age = 18
sex = '男'
msg = F'姓名：{name},性别：{age}，年龄：{sex}'  # 大写字母也可以
print(msg)

print('2.2 任意表达式'.center(30, '*'))
# 2.2 任意表达式
# 他可以加任意的表达式，非常方便：

print(f'{3 * 21}')  # 63

name = 'liufei'
print(f'全部大写：{name.upper()}')  # 全部大写：LIUFEI

# 字典也可以
teacher = {'name': '刘飞', 'age': 18}
msg = f"The teacher is {teacher['name']}, aged {teacher['age']}'"
print(msg)  # The teacher is 刘飞, aged 18'

# 列表也行
l1 = ['liufei', 18]
msg = F'姓名:{l1[0]}, 年龄:{l1[1]}'
print(msg)  # 姓名:liufei, 年龄:18

print('2.3 也可以插入表达式'.center(30, '*'))


# 2.3 也可以插入表达式
# 可以用函数完成相应的功能，然后将返回值返回到字符串相应的位置
def sum_a_b(a, b):
    return a + b


a = 1
b = 2
print('求和的结果为' + f'{sum_a_b(a, b)}')  # 求和的结果为3

# 2.4 多行f
name = 'liufei'
age = 18
ajd = 'handsome'

speaker = f'''Hi {name}.
You are {age} years old
You are a {ajd} guy!!
'''

print(speaker)

print('2.5 其他细节'.center(30, '*'))
# 2.5 其他细节
# 这里有一些注意的细节，了解一下就行。

print(f"{{73}}")  # {73}
print(f"{{{73}}}")  # {73}
print(f"{{{{73}}}}")  # {{73}}

m = 21
# ! , : { } ;这些标点不能出现在{} 这里面。
# print(f'{;12}')  # 报错
# 所以使用lambda 表达式会出现一些问题。
# 解决方式：可将lambda嵌套在圆括号里面解决此问题。

x = 5
print(f'{(lambda x: x * 2)(x)}')  # 10

# 总结：f-string的格式化输出更加简洁，方便，易读。而且他的处理速度对之前的%s 或者format 有了较高的提升，所以以后尽量使用此种格式化输出。

print()
# 3. 迭代器
print('3.1 可迭代对象'.center(30, '*'))
'''
1) 可迭代对象定义
    对于迭代器来说，我们更熟悉的应该是可迭代对象，之前无论是源码还是讲课中或多或少我们提到过可迭代对象这个词。之前为了便于大家理解可迭代对象，可能解释的不是很正确，所以今天我们正式的聊一聊什么是可迭代对象。从字面意思来说，我们先对其进行拆解：什么是对象？Python中一切皆对象，之前我们讲过的一个变量，一个列表，一个字符串，文件句柄，函数名等等都可称作一个对象，其实一个对象就是一个实例，就是一个实实在在的东西。那么什么叫迭代？其实我们在日常生活中经常遇到迭代这个词儿，更新迭代等等，迭代就是一个重复的过程，但是不能是单纯的重复（如果只是单纯的重复那么他与循环没有什么区别）每次重复都是基于上一次的结果而来。比如你爹生你，你生你爹，哦不对，你生你儿子，你儿子生你孙子等等，每一代都是不一样的；还有你使用过得app，微信，抖音等，隔一段时间就会基于上一次做一些更新，那么这就是迭代。可迭代对象从字面意思来说就是一个可以重复取值的实实在在的东西。
    那么刚才我们是从字面意思分析的什么是可迭代对象，到目前为止我们接触到的可迭代对象有哪些呢？
    str  list   tuple  dic  set  range 文件句柄等，那么int，bool这些为什么不能称为可迭代对象呢？虽然在字面意思这些看着不符合，但是我们要有一定的判断标准或者规则去判断该对象是不是可迭代对象。
在python中，但凡内部含有__iter__方法的对象，都是可迭代对象。
'''

'''
2) 查看对象内部方法
    该对象内部含有什么方法除了看源码还有什么其他的解决方式么？当然有了， 可以通过dir() 去判断一个对象具有什么方法
'''
s1 = 'alex'
print(dir(s1))

# dir()会返回一个列表，这个列表中含有该对象的以字符串的形式所有方法名。这样我们就可以判断python中的一个对象是不是可迭代对象了：
i = 10
print('__iter__' in dir(s1))  # True
print('__iter__' in dir(i))  # False

'''
3) 小结：
    从字面意思来说：可迭代对象就是一个可以重复取值的实实在在的东西。
    从专业角度来说：但凡内部含有__iter__方法的对象，都是可迭代对象。
    可迭代对象可以通过判断该对象是否有’__iter__’方法来判断。
    可迭代对象的优点：
        可以直观的查看里面的数据。
    可迭代对象的缺点：
        1. 占用内存。
        2. 可迭代对象不能迭代取值（除去索引，key以外）。
    那么这个缺点有人就提出质疑了，即使抛去索引,key以外，这些我可以通过for循环进行取值呀！对，他们都可以通过for循环进行取值，其实for循环在底层做了一个小小的转化，就是先将可迭代对象转化成迭代器，然后在进行取值的。那么接下来，我们就看看迭代器是个什么鬼。
'''
print('3.2 迭代器'.center(30, '*'))
'''
1) 迭代器的定义
    从字面意思来说迭代器，是一个可以迭代取值的工具，器：在这里当做工具比较合适。
    从专业角度来说：迭代器是这样的对象：实现了无参数的__next__方法，返回序列中的下一个元素，如果没有元素了，那么抛出StopIteration异常.python中的迭代器还实现了__iter__方法，因此迭代器也可以迭代。 出自《流畅的python》
    那么对于上面的解释有一些超前，和难以理解，不用过于纠结，我们简单来说：在python中，内部含有'__Iter__'方法并且含有'__next__'方法的对象就是迭代器。
2) 如何判断该对象是否是迭代器
    ok，那么我们有了这个定义，我们就可以判断一些对象是不是迭代器或者可迭代对象了了，请判断这些对象：str list tuple dict set range 文件句柄 哪个是迭代器，哪个是可迭代对象：
'''
o1 = 'alex'
o2 = [1, 2, 3]
o3 = (1, 2, 3)
o4 = {'name': '太白', 'age': 18}
o5 = {1, 2, 3}
f = open('file', encoding='utf-8', mode='w')
print('__iter__' in dir(o1))  # True
print('__iter__' in dir(o2))  # True
print('__iter__' in dir(o3))  # True
print('__iter__' in dir(o4))  # True
print('__iter__' in dir(o5))  # True
print('__iter__' in dir(f))  # True

# hsagn
print('__next__' in dir(o1))  # False
print('__next__' in dir(o2))  # False
print('__next__' in dir(o3))  # False
print('__next__' in dir(o4))  # False
print('__next__' in dir(o5))  # False
print('__next__' in dir(f))  # True
f.close()

# 通过以上代码可以验证，之前我们学过的这些对象，只有文件句柄是迭代器，剩下的那些数据类型都是可迭代对象。


# 3) 可迭代对象如何转化成迭代器：
print('3) 可迭代对象如何转化成迭代器：'.center(30, '*'))
l1 = [1, 2, 3, 4, 5, 6]
obj = l1.__iter__() # 或者是 iter(l1)
print(obj) # <list_iterator object at 0x0000026E28CA1460>

# 4) 迭代器取值：
print('4) 迭代器取值：'.center(30, '*'))
'''
可迭代对象是不可以一直迭代取值的（除去用索引，切片以及Key），但是转化成迭代器就可以了，迭代器是利用__next__()进行取值：
'''
l1 = [1, 2, 3,]
obj = l1.__iter__()  # 或者 iter(l1)
print(obj) # <list_iterator object at 0x000002C0D69F2070>
ret = obj.__next__()
print(ret) #1
ret = obj.__next__()
print(ret) # 2
ret = obj.__next__()
print(ret) # 3
# ret = obj.__next__()  # StopIteration
# print(ret)

# # 迭代器利用next取值：一个next取对应的一个值，如果迭代器里面的值取完了，还要next，
# # 那么就报StopIteration的错误。

print('5) while模拟for的内部循环机制：'.center(30, '*'))
# 5) while模拟for的内部循环机制：
'''
刚才我们提到了，for循环的循环对象一定要是可迭代对象，但是这不意味着可迭代对象就可以取值，因为for循环的内部机制是：将可迭代对象转换成迭代器，然后利用next进行取值，最后利用异常处理处理StopIteration抛出的异常。
'''

l1 = [1, 2, 3, 4, 5, 6]
# 1 将可迭代对象转化成迭代器
obj = iter(l1)
# 2,利用while循环，next进行取值
while 1:
    try:
        print(next(obj))
    except StopIteration:
        break

print('6)小结：'.center(30, '*'))
'''
从字面意思来说：迭代器就是可以迭代取值的工具。
        从专业角度来说：在python中，内部含有'__Iter__'方法并且含有'__next__'方法的对象就是迭代器。
        迭代器的优点：
                节省内存。
                    迭代器在内存中相当于只占一个数据的空间：因为每次取值都上一条数据会在内存释放，加载当前的此条数据。
                惰性机制。
                    next一次，取一个值，绝不过多取值。​
        有一个迭代器模式可以很好的解释上面这两条：迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。这就是迭代器模式。
        迭代器的缺点：
            不能直观的查看里面的数据。
            取值时不走回头路，只能一直向下取值。
'''

l1 = [1, 2, 3, 4, 5, 6]
obj = iter(l1)

for i in range(2):
    print(next(obj))

for i in range(2):
    print(next(obj))

print('3.3 可迭代对象与迭代器对比'.center(30, '*'))
'''
我们今天比较深入的了解了可迭代对象与迭代器，接下来我们说一下这两者之间比较与应用：
    可迭代对象：
    是一个私有的方法比较多，操作灵活（比如列表，字典的增删改查，字符串的常用操作方法等）,比较直观，但是占用内存，而且不能直接通过循环迭代取值的这么一个数据集。
    应用：当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。
    迭代器：
    是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。
    应用：当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。（可参考为什么python把文件句柄设置成迭代器）。
'''