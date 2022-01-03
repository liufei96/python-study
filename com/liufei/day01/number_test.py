num = 10
print(num.bit_length())  # 当十进制用二进制表示时，最少使用的位数

## 2. bool

# int --> bool
i = 100
print(bool(i))  # True  # 非零即True

i1 = 0
print(bool(i1))  # False 零即False

# bool ---> int
t = True
print(int(t))  # 1  True --> 1
t = False
print(int(t))  # 0  False --> 0

# int --> str
i1 = 100
print(str(i1))  # '100'

# str ---> int  # 全部由数字组成的字符串才可以转化成数字
s1 = '90'
print(int(s1))  # 90

# str ---> bool
s1 = '刘飞'
s2 = ''
print(bool(s1))  # True 非空即True
print(bool(s2))  # False

# bool ---> str
t1 = True
print(str(t1))  # 'True'

## 字符串切片
## 切片就是通过索引（索引：索引：步长）截取字符串的一段，形成新的字符串（原则就是顾头不顾腚）。
print("===== 字符串切片的使用 =====")
a = 'ABCDEFGHIJK'
print(a[0: 3])
print(a[2: 5])
print(a[:])  # 默认到最后
print(a[:-1])  # -1 是列表中最后一个元素的索引，但是要满足顾头不顾腚的原则，所以取不到K元素
print(a[:5:2])  # 加步长
print(a[-1:-5:-2])  # 反向加步长
print(a[1:78])  # 右边超出索引，不会报错。 BCDEFGHIJK
print(a[13:])  # 返回空，左边超出索引长度，也不会报错。

## 切片就是通过索引（索引：索引：步长）截取字符串的一段，形成新的字符串（原则就是顾头不顾腚）。
print("===== 字符串常用方法 =====")
# 字符串除了可以用切片（步长）之外，还有一些其他的操作方法。
# 数字符串中的元素出现的个数。
a1 = 'ahjdsabdsaa'
ret3 = a1.count("a", 0, 4)  # 可切片
print(ret3)

a4 = "dkfjdkfasf54"
# startswith 判断是否以...开头
# endswith 判断是否以...结尾
ret4 = a4.endswith('jdk', 3, 6)  # 顾头不顾腚
print(ret4)  # 返回的是布尔值 True
ret5 = a4.startswith("kfj", 1, 4)
print(ret5)  # True

# split 以什么分割，最终形成一个列表此列表不含有这个分割的元素。
ret9 = 'title,Tilte,atre,'.split('t')
print(ret9)
ret91 = 'title,Tilte,atre,'.rsplit('t', 1)
print(ret91)

# format的三种玩法 格式化输出
res = '{} {} {}'.format('egon', 18, 'male')
print(res)  # egon 18 male
res = '{1} {0} {1}'.format('egon', 18, 'male')
print(res)  # 18 egon 18
res = '{name} {age} {sex}'.format(sex='male', name='egon', age=18)
print(res)  # egon 18 male

# strip  去掉两边的什么内容
name = '*barry**'
print(name.strip('*'))  # barry
print(name.lstrip('*'))  # barry**
print(name.rstrip('*'))  # *barry

# replace
name = 'alex say :i have one tesla,my name is alex'
print(name.replace('alex', 'SB', 2))

# is系列
name = 'tAiBai123'
print(name.isalnum())  # 字符串由字母或数字组成
print(name.isalpha())  # 字符串只由字母组成
print(name.isdecimal())  # 字符串只由十进制组成

#############下面这些方法在数据类型补充时会讲到，现在不讲####################
# 寻找字符串中的元素是否存在
a4 = "dkfjdkfasf54"
ret6 = a4.find("fjdk", 1, 6)
print(ret6)  # 返回的找到的元素的索引，如果找不到返回-1

# ret61 = a4.index("fjdk",4,6)
# print(ret61) # 返回的找到的元素的索引，找不到报错。

# captalize,swapcase,title
print(name.capitalize())  # 首字母大写，其他全部小写
print(name.swapcase())  # 大小写翻转。 大写变小写，小写变大写
msg = 'taibai say hi'
print(msg.title())  # 每个单词的首字母大写

# 内同居中，总长度，空白处填充
ret2 = a1.center(20, "*")
print(ret2)  # ****ahjdsabdsaa*****

# 2.4.1 列表的创建
print()
title = ' 2.4.1 列表的创建 '
print(title.center(25, '='))

# 方法一 （常用）
list1 = [1, 2, '刘飞']

# 方法二（不常用）
list1 = list()  # 空列表
list1 = list('123')
print(list1)  # ['1', '2', '3']

# 方式三：列表推导式（后面的课程会讲到）
list1 = [i for i in range(1, 5)]
print(list1)  # [1, 2, 3, 4]

# 2.4.2 列表的索引切片
l1 = ['a', 'b', '刘飞', 3, 666]
print(l1[0])  # 'a'
print(l1[-1])  # 666
print(l1[1:3])  # ['b', '太白']
print(l1[:-1])  # ['a', 'b', '太白', 3]
print(l1[::2])  # ['a', '太白', 666]
print(l1[::-1])  # [666, 3, '太白', 'b', 'a']
print(l1[:])

# 2.4.3 增加
# append 追加，给列表的最后面追加一个元素
print()
print(' list 增加'.center(20, '#'))
l = [1, 2, 'a']
l.append(666)
print(l)  # [1, 2, 'a', 666]

# insert  插入在列表的任意位置插入元素
l = [1, 2, 'a']
l.insert(1, '刘飞')
print(l)  # [1, '刘飞', 2, 'a']

# extend 迭代着追加，在列表的最后面迭代着追加一组数据
l = [1, 2, 'a']
l.extend('刘飞a')
print(l)  # [1, 2, 'a', '刘', '飞', 'a']

# 2.4.4 删
print()
print(' list 删除 '.center(20, '#'))
# pop  通过索引删除列表中对应的元素，该方法有返回值，返回值为删除的元素
l = ['刘飞', 'a', 1, 3, 'b']
ret = l.pop(1)  # 超出索引，会报错
print(ret, l)  # a ['刘飞', 1, 3, 'b']

# remove  通过元素删除列表中该元素
l = ['刘飞', 'a', 1, 3, 'b']
l.remove('刘飞')
print(l)  # ['a', 1, 3, 'b']

# clear 清空列表
l = ['刘飞', 'a', 1, 3, 'b']
l.clear()
print(l)  # []

# del
# 按照索引删除该元素
l = ['刘飞', 'a', 1, 3, 'b']
del l[2]
print(l)  # ['刘飞', 'a', 3, 'b']

# 切片删除该元素
l = ['刘飞', 'a', 1, 3, 'b']
del l[::2]
print(l)  # ['a', 3]

# 2.4.5. 改
print()
print(' list 修改 '.center(20, '#'))
l = ['刘飞', 'a', 1, 3, 'b']
l[0] = '男神'
print(l)  # ['男神', 'a', 1, 3, 'b']

# 按照切片改值(迭代着增加)
l = ['刘飞', 'a', 1, 3, 'b']
l[1:3] = 'abcdefg'
print(l)  # ['刘飞', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 3, 'b']

# 按照切片(步长)改值(必须一一对应)
l = ['刘飞', 'a', 1, 3, 'b']
l[::2] = '对应1'
print(l)  # ['对', 'a', '应', 3, '1']

# 2.4.6. 查
# 切片去查，或者循环去查。

# 其他操作
print()
print(' list 其他操作 '.center(20, '#'))
# count(数) （方法统计某个元素在列表中出现的次数）。
a = ["q", "w", "q", "r", "t", "y"]
print(a.count('q'))  # 2

# index（方法用于从列表中找出某个值第一个匹配项的索引位置）
a = ["q", "w", "q", "r", "t", "y"]
print(a.index('q'))  # o

# sort （方法用于在原位置对列表进行排序）
a = ["q", "w", "q", "r", "t", "y"]
a.sort()  # 没有返回值 None
print(a)  # ['q', 'q', 'r', 't', 'w', 'y']

# reverse （方法将列表中的元素反向存放）。
a = ["q", "w", "q", "r", "t", "y"]
a.reverse()  # 没有返回值 None
print(a)  # ['y', 't', 'r', 'q', 'w', 'q']

# 列表也可以相加与整数相乘
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)  # [1, 2, 3, 4, 5, 6]
print(l1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 2.4.6 列表的嵌套
print()
print(' list 列表的嵌套 '.center(20, '#'))
l1 = [1, 2, 'liufei', [1, 'WuSir', 3]]
'''
1, 将l1中的'taibai'变成大写并放回原处。
2，给小列表[1,'alex',3,]追加一个元素,'刘飞'。
3，将列表中的'liufei'通过字符串拼接的方式在列表中变成'liufeisb'
'''
l1[2] = l1[2].swapcase()
print(l1)  # [1, 2, 'LIUFEI', [1, 'WuSir', 3]]
l1[3].append('刘飞')
print(l1)  # [1, 2, 'LIUFEI', [1, 'WuSir', 3, '刘飞']]
l1[2] = l1[2] + 'sb'
print(l1)  # [1, 2, 'LIUFEIsb', [1, 'WuSir', 3, '刘飞']]

'''
　你需要存储大量的数据，且需要这些数据有序的时候。
　制定一些特殊的数据群体：按顺序，按规则，自定制设计数据。
'''

print()
print(' 2.5 元组 tuple '.center(26, '#'))
# 2.5 元组
'''
Why:对于容器型数据类型list，无论谁都可以对其增删改查，那么有一些重要的数据放在list中是不安全的，所以需要一种容器类的数据类型存放重要的数据，创建之初只能查看而不能增删改，这种数据类型就是元组。
what:这个容器型数据类型就是元组。
元组:俗称不可变的列表,又被成为只读列表,元祖也是python的基本数据类型之一,用小括号括起来,里面可以放任何数据类型的数据,查询可以,循环也可以,切片也可以.但就是不能改.
'''

# 2.5.1 元组的索引切片
tu1 = ('a', 'b', '刘飞', 3, 666)
print(tu1[0])  # a
print(tu1[-1])  # 666
print(tu1[1:3])  # ('b', '刘飞')
print(tu1[:-1])  # ('a', 'b', '刘飞', 3)
print(tu1[::2])  # ('a', '刘飞', 666)
print(tu1[::-1])  # (666, 3, '刘飞', 'b', 'a')

# 2.5.2 元组其他操作方法
print(' 2.5.2 元组其他操作方法 '.center(26, '#'))
# 因为元组的特性，直接从属于元组的元素不能更改，所以元组只能查看。
tu1 = ('a', 'b', '刘飞', 3, 666)
for i in tu1:
    print(i)

# index：通过元素找索引（可切片），找到第一个元素就返回，找不到该元素即报错。
tu1 = ('a', 'b', '刘飞', 3, 666)
print(tu1.index('a'))  # 0

# count: 获取某元素在列表中出现的次数
tu1 = ('a', 'b', '刘飞', 3, 666)
print(tu1.count('a'))  # 1

# 2.5.3 len
tu1 = ('a', 'b', '刘飞', 3, 666)
print(len(tu1))  # 5

print()
print(' 2.6 dict 字典的使用 '.center(30, '#'))
# 2.6.2 创建字典的几种方式：
# 方式1:
dict1 = dict((('one', 1), ('tow', 2), ('three', 3)))
print(dict1)  # {'one': 1, 'tow': 2, 'three': 3}

# 方式2:
dict2 = dict(one=1, two=2, three=3)
print(dict2)  # {'one': 1, 'two': 2, 'three': 3}

# 方式3:
dict3 = dict({'one': 1, 'two': 2, 'three': 3})
print(dict3)  # {'one': 1, 'two': 2, 'three': 3}

# 方式4: 后面会讲到先了解
dict4 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(dict4)  # {'one': 1, 'two': 2, 'three': 3}

# 方式6: 字典推导式 后面会讲到
dic = {k: v for k, v in [('one', 1), ('two', 2), ('three', 3)]}
print(dic)  # {'one': 1, 'two': 2, 'three': 3}

# 方式7:利用fromkeys后面会讲到。
dic = dict.fromkeys('abc', '刘飞')
print(dic)  # {'a': '刘飞', 'b': '刘飞', 'c': '刘飞'}

# 2.6.3 验证字典的合法性
print(' 2.6 dict 字典的使用 '.center(30, '#'))
# 合法
dic = {123: 456, True: 999, "id": 1, "name": 'sylar', "age": 18, "stu": ['帅哥', '美⼥'], (1, 2, 3): '麻花藤'}
print(dic[123])
print(dic[True])
print(dic['id'])
print(dic['stu'])
print(dic[1, 2, 3])

# 不合法
# dic = {[1, 2, 3]: '周杰伦'}  # list是可变的. 不能作为key
# dic = {{1: 2}: "哈哈哈"}  # dict是可变的. 不能作为key
# dic = {{1, 2, 3}: '呵呵呵'}  # set是可变的, 不能作为key

# 2.6.4 字典的常规操作
# 通过键值对直接增加
print(' dict 字典的增加 '.center(30, '#'))
dic = {'name': 'liufei', 'age': 18}
dic['weight'] = 120  # 没有weight这个键，就增加键值对
print(dic)  # {'name': 'liufei', 'age': 18, 'weight': 120}
dic['name'] = '刘飞'
print(dic)  # 有name这个键，就成了字典的改值

# setdefault
dic = {'name': 'liufei', 'age': 18}
dic.setdefault('height', 181)  # 没有height此键，则添加
print(dic)  # {'name': 'liufei', 'age': 18, 'height': 181}
dic.setdefault('name', '刘飞')  # 有此键则不变
print(dic)  # {'name': 'liufei', 'age': 18, 'height': 181}

# 它有返回值
dic = {'name': 'liufei', 'age': 18}
ret = dic.setdefault('name')
print(ret)  # liufei

print(' 字典的删除 '.center(30, '#'))
# pop 通过key删除字典的键值对，有返回值，可设置返回值。
dic = {'name': 'liufei', 'age': 18}
# ret = dic.pop('name')
# print(ret) # liufei
# print(dic) # {'age': 18}
ret1 = dic.pop('n', None)
print(ret1, dic)  # None {'name': 'liufei', 'age': 18}

# popitem 3.5版本之前，popitem为随机删除，3.6之后为删除最后一个，有返回值
dic = {'name': 'liufei', 'age': 18}
ret = dic.popitem()
print(ret, dic)  # ('age', 18) {'name': 'liufei'}

# clear 清空字典
dic = {'name': 'liufei', 'age': 18}
dic.clear()
print(dic)  # {}

# del
# 通过键删除键值对
dic = {'name': 'liufei', 'age': 18}
del dic['name']
print(dic)  # {'age': 18}

# 删除整个字典
del dic
# print(dic) # 定义的dic也会被删除，此时打印，会报错：NameError: name 'dic' is not defined

print(' 字典的修改 '.center(30, '#'))
dic = {'name': 'liufei', 'age': 18}
dic['name'] = '刘飞'
print(dic)  # {'name': '刘飞', 'age': 18}

# update
dic = {'name': 'liufei', 'age': 18}
dic.update(sex='男', height=181)
print(dic)  # {'name': 'liufei', 'age': 18, 'sex': '男', 'height': 181}

dic = {'name': 'liufei', 'age': 18}
dic.update([(1, 'a')])
print(dic)  # {'name': 'liufei', 'age': 18, 1: 'a'}

dic1 = {"name": "jin", "age": 18, "sex": "male"}
dic2 = {"name": "alex", "weight": 75}
dic1.update(dic2)
print(dic1)  # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
print(dic2)  # {'name': 'alex', 'weight': 75}

print(' 字典的查询 '.center(30, '#'))
# 直接dic[key](没有此键会报错)
dic = {'name': 'liufei', 'age': 18}
print(dic['name'])  # liufei

# get
dic = {'name': 'liufei', 'age': 18}
print(dic.get('name'))  # liufei
print(dic.get('name1'))  # None。没有，输出：None
v = dic.get('name2', '没有此键')
print(v)  # 没有此键

# fromkeys  数据类型的补充时会给大家讲到~
print()
print(' fromkeys '.center(30, '#'))
dic = dict.fromkeys('abcd', '刘飞')
print(dic)  # {'a': '刘飞', 'b': '刘飞', 'c': '刘飞', 'd': '刘飞'}

# dic = dict.fromkeys((1, 2, 3),'刘飞')  这里用tuple 或 list 都可以
dic = dict.fromkeys([1, 2, 3], '刘飞')
print(dic)  # {1: '刘飞', 2: '刘飞', 3: '刘飞'}

# 其他操作
print(' 其他操作 '.center(30, '#'))
dic = {'name': 'liufei', 'age': 18}
key_list = dic.keys()
print(key_list)  # dict_keys(['name', 'age'])  一个高仿列表,存放的都是字典中的key

# 这个高仿列表，可以转换成list
print(list(key_list))  # ['name', 'age']

# 它还可以循环打印
dic = {'name': 'liufei', 'age': 18}

for k in dic:
    print(k)

# name
# age

value_list = dic.values()
print(value_list)  # dict_values(['liufei', 18]) 一个高仿列表,存放都是字典中的value
print(list(value_list))  # ['liufei', 18]

# 它还可以循环打印
for v in dic.values():
    print(v)

# liufei
# 18

key_value_list = dic.items()
print(key_value_list)  # dict_items([('name', 'liufei'), ('age', 18)]) 一个高仿列表,存放是多个元祖,元祖中第一个是字典中的键,第二个是字典中的值

# 并且这个高仿的列表可以转化成列表
print(list(key_value_list))  # [('name', 'liufei'), ('age', 18)]

# 它还可以循环打印
for i in dic.items():
    print(i)
# ('name', 'liufei')
# ('age', 18)

# 这里补充一个知识点：分别赋值，也叫拆包。
print(' 赋值、拆包 '.center(30, '#'))
a, b = 1, 2
print(a, b)  # 1 2

a, b = ('你好', '世界')  # 这个用专业名词就叫做元组的拆包
print(a, b)  # 你好 世界

a, b = ['你好', '大飞哥']
print(a, b)  # 你好 大飞哥

a, b = {'汪峰': '北京北京', '王菲': '天后'}
print(a, b)  # 汪峰 王菲  这里输出的是key

# 所以利用上面刚学的拆包的概念，我们循环字典时还可以这样获取字典的键，以及值：
for k, v in dic.items():
    print('这是键', k)
    print('这是值', v)
# 这是键 name
# 这是值 liufei
# 这是键 age
# 这是值

# 4.1.5字典的嵌套
print(' 4.1.5字典的嵌套 '.center(30, '#'))

# 字典的嵌套是非常重要的知识点，这个必须要建立在熟练使用字典的增删改查的基础上，而且字典的嵌套才是咱们在工作中经常会遇到的字典，
# 工作中遇到的字典不是简简单单一层，而就像是葱头一样，一层接一层，但一般都是很有规律的嵌套，那么接下来我们就学习一下字典的嵌套：

dic = {
    'name': '汪峰',
    'age': 48,
    'wife': [{'name': '国际章', 'age': 38}],
    'children': {'girl_first': '小苹果', 'girl_second': '小怡', 'girl_three': '顶顶'}
}

# 1. 获取汪峰的名字。
print(dic['name'])

# 2.获取这个字典：{'name':'国际章','age':38}。
print(dic['wife'])

# 3. 获取汪峰妻子的名字。
# print(dic['wife'][0].get('name')) # 国际章
print(dic['wife'][0]['name'])

# 4. 获取汪峰的第三个孩子名字。
print(dic['children']['girl_three'])  # 顶顶

print()
print(' 2.7 集合set(了解) '.center(30, '#'))
'''
集合是无序的，不重复的数据集合，它里面的元素是可哈希的(不可变类型)，但是集合本身是不可哈希（所以集合做不了字典的键）的。以下是集合最重要的两点：
    去重，把一个列表变成集合，就自动去重了。
    关系测试，测试两组数据之前的交集、差集、并集等关系。
'''

# 1，集合的创建。
set1 = set({1, 2, 'key'})
set2 = {1, 2, 'barry1'}
print(set1, set2)  # {1, 2, 'key'} {1, 2, 'barry1'}

# 2，集合的增。
print(' 集合的增 '.center(30, '#'))
set1 = {'alex', 'wusir', 'ritian', 'egon', 'barry'}
set1.add('刘飞')
print(set1)  # 每次输出顺序都不同

# update：迭代着增加
set1.update('A')
print(set1)
set1.update('老师')
print(set1)  # {'ritian', 'alex', '刘飞', 'A', 'wusir', '老', 'egon', '师', 'barry'}
set1.update([1, 2, 3])
print(set1)  # {1, 'ritian', 'egon', 'A', '老', 2, 3, 'alex', '刘飞', 'barry', '师', 'wusir'}

# 3，集合的删。
print(' 集合的删 '.center(30, '#'))
set1 = {'alex', 'wusir', 'ritian', 'egon', 'barry'}
set1.remove('alex')  # 删除一个元素
print(set1)  # {'ritian', 'wusir', 'egon', 'barry'}

set1.pop()  # 随机删除一个元素
print(set1)

set1.clear()  # 清空集合
print(set1)  # set()

del set1  # 删除集合
# print(set1) # 删除时候，就不能使用set1了，否则会报错：NameError: name 'set1' is not defined

# 4，集合的其他操作：
print(' 集合的其他操作 '.center(30, '#'))
## 4.1 交集。（&  或者 intersection）
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
print(set1 & set2)  # {4}
print(set1.intersection(set2))  # {4}

# 4.2 并集。（| 或者 union）
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6}

# 4.3 差集。（- 或者 difference）
print(set1 - set2)  # {1, 2, 3}
print(set2.difference(set1))  # {5, 6}

# 4.4反交集。 （^ 或者 symmetric_difference）
print(set1 ^ set2)  # {1, 2, 3, 5, 6}
print(set2.symmetric_difference(set1))  # {1, 2, 3, 5, 6}

# 4.5子集与超集
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1 < set2)  # True 这两个相同，都是说明set1是set2子集。
print(set1.issubset(set2))  # True

print(set2 > set1)  # True
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。

# 5, frozenset不可变集合，让集合变成不可变类型。
s = frozenset('barry')  # frozenset({'y', 'r', 'b', 'a'}) <class 'frozenset'>
print(s, type(s))

print()
print('  for循环 '.center(30, '#'))

# for循环：用户按照顺序循环可迭代对象的内容。
msg = '你好，python！'
for item in msg:
    print(item)
# 你
# 好
# ，
# p
# y
# t
# h
# o
# n
# ！

li = ['alex', '银角', '女神', 'egon', '刘飞']
for i in li:
    print(i)

dic = {'name': '刘飞', 'age': 18, 'sex': 'man'}
for k, v in dic.items():
    print(k, v)

# enumerate：枚举，对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值。
li = ['alex', '银角', '女神', 'egon', '刘飞']
for i in enumerate(li):
    print(i)
# (0, 'alex')
# (1, '银角')
# (2, '女神')
# (3, 'egon')
# (4, '刘飞')

for index, name in enumerate(li, 1):  # 起始位置默认是0，可更改，这里index从1开始
    print(index, name)
# 1 alex
# 2 银角
# 3 女神
# 4 egon
# 5 刘飞

# range：指定范围，生成指定数字。
for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):  # 步长
    print(i)
# 1
# 3
# 5
# 7
# 9

for i in range(10, 1, -2):  # 反向步长
    print(i)
# 10
# 8
# 6
# 4
# 2
