# 一. 基础数据类型补充内容
## 1.1 字符串

'''
字符串咱们之前已经讲了一些非常重要的方法，剩下还有一些方法虽然不是那么重要，但是也算是比较常用，
在此给大家在补充一些，需要大家尽量记住。
'''

# captalize,swapcase,title
msg = 'Liufei 刘飞 hello 123'
print(msg.capitalize())  # 首字母大写
print(msg.swapcase())  # 大小写翻转
print(msg.title())  # 每个单词的首字母大写

# 内同居中，总长度，空白处填充
a1 = '标题'
ret2 = a1.center(20, "*")
print(ret2)

# 寻找字符串中的元素是否存在
msg = 'abcABDkdlsa'
ret = msg.find('abc', 0, 4)
print(ret)  # 0 返回的找到的元素的索引，如果找不到返回-1

ret = msg.index('abc', 0, 4)
print(ret)  # 0 返回的找到的元素的索引，找不到报错。

# 1.2 元组
'''
python中元组有一个特性，元组中如果只含有一个元素且没有逗号，则该元组不是元组，与改元素数据类型一致，如果有逗号，那么它是元组。
'''
tu = (1)
print(tu, type(tu))  # 1 <class 'int'>
tu = ('alex')
print(tu, type(tu))  # alex <class 'str'>
tu = ([1, 2, 3])
print(tu, type(tu))  # {1, 2, 3} <class 'list'>
tu = ({1, 2, 3})
print(tu, type(tu))  # {1, 2, 3} <class 'set'>

print()
# 元组也有一些其他的方法：
# index：通过元素找索引（可切片），找到第一个元素就返回，找不到该元素即报错
tu = ('刘飞', [1, 2, 3], 'WuSir', '女神')
print(tu.index('刘飞'))  # 0

print()
# count: 获取某元素在列表中出现的次数
tu = ('刘飞', [1, 2, 3], 'WuSir', '女神')
print(tu.count('刘飞'))  # 0

# 1.3 列表
# 列表的其他操作方法
# count（数）（方法统计某个元素在列表中出现的次数）。
a = ["q", "w", "q", "r", "t", "y"]
print(a.count('q'))  # 2

# index（方法用于从列表中找出某个值第一个匹配项的索引位置）
a = ["q", "w", "r", "t", "y"]
print(a.index('r'))  # 2

# sort （方法用于在原位置对列表进行排序）。
# reverse （方法将列表中的元素反向存放）。
a = [2, 1, 3, 4, 5]
a.sort()  # a = [2,1,3,4,5]
print(a)  # [1, 2, 3, 4, 5]
a.reverse()  # a = [2,1,3,4,5]
print(a)  # [5, 4, 3, 2, 1]

# 列表也可以相加与整数相乘
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)  # [1, 2, 3, 4, 5, 6]
print(l1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 循环列表，改变列表大小的问题
'''
先不着急，说这个问题，先做一道小题：
有列表l1, l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）。
有人说这个还不简单么？我循环列表，然后进行判断，只要他的索引为奇数，我就删除。OK，你可以照着这个思路去做。
那么根据题意，这个题最终的结果应该是：l1 = [11, 33, 55],但是你得到的结果却是： l1 = [11, 33, 44] 为什么不对呢？？？
用这个进行举例：当你循环到22时，你将列表中的22删除了，但是你带来的影响是：33,44,55都会往前进一位，他们的索引由原来的2,3,4变成了1,2,3 所以你在往下进行循环时，就会发现，额........完全不对了。
那这个怎么解决呢？有三种解决方式：
'''

## 直接删除
# num_list = [1, 2, 3, 4, 5]
# for i in range(len(num_list)):
#     if num_list[i] == 2:
#         num_list.pop(i)
#     else:
#         print(num_list[i])
# print(num_list)

'''
这样直接删除会报错
TypeError: remove() takes exactly one argument (0 given)
原因是在删除list中的元素后，list的实际长度变小了，但是循环次数没有减少，依然按照原来list的长度进行遍历，所以会造成索引溢出。
'''

# 于是修改了下面代码
num_list = [1, 2, 3, 4, 5]
for i in range(len(num_list)):
    if i >= len(num_list):
        break
    if num_list[i] == 2:
        num_list.pop(i)
    else:
        print(num_list[i])
print(num_list)

# 这回不会报异常了，但是打印结果如下：
# 1
# 4
# 5
# [1, 3, 4, 5]

'''
虽然最后，list中的元素[2]确实被删除掉了，但是，在循环中的打印结果不对，少打印了[3]。
思考了下，知道了原因，当符合条件，删除元素[2]之后，后面的元素全部往前移，于是[3, 4, 5]向前移动，那么元素[3]的索引，就变成了之前[2]的索引（现在[3]的下标索引变为1了），后面的元素以此类推。
可是，下一次for循环的时候，是从下标索引2开始的，于是，取出了元素[4]，就把[3]漏掉了。
'''

# 既然知道了问题的根本原因所在，想要找到正确的方法，也并不难，于是我写了如下的代码：
num_list = [1, 2, 3, 4, 5]
i = 0
while i < len(num_list):
    if num_list[i] == 2:
        num_list.pop(i)
        i -= 1
    else:
        print(num_list[i])
    i += 1
print(num_list)
# 执行结果，完全正确：
# 1
# 3
# 4
# 5
# [1, 3, 4, 5]

# 当然，这还不是最优解，所以，我搜索到了通用的解决方案：1、倒序循环遍历；2、遍历拷贝的list，操作原始的list。

# 1. 倒叙循环
print('倒叙循环'.center(30, '='))
num_list = [1, 2, 3, 4, 5]
for i in range(len(num_list) - 1, -1, -1):
    if num_list[i] == 2:
        num_list.pop(i)
    else:
        print(num_list[i])

print(num_list)

# 执行结果完全正确。那么，为何正序循环时删除就有问题，而倒序循环时删除就ok？额。。。。。。言语难表，还是画个丑图出来吧。
# 删除元素[2]后，[3, 4, 5]往前挤，但是没关系，因为下一次循环的下标索引为0，里面存放的是[1]，所以正是我们所期望的正确的元素值。

# 2. 遍历拷贝的list，操作原始的list
print('遍历拷贝的list，操作原始的list'.center(30, '='))
num_list = [1, 2, 3, 4, 5]
print(num_list)

for item in num_list[:]:
    if item == 2:
        num_list.remove(item)
    else:
        print(item)

print(num_list)

# 在循环一个列表时的过程中，如果你要改变列表的大小（增加值，或者删除值），那么结果很可能会出错或者报错。

'''
原始的list是num_list，那么其实，num_list[:]是对原始的num_list的一个拷贝，是一个新的list，所以，我们遍历新的list，而删除原始的list中的元素，则既不会引起索引溢出，最后又能够得到想要的最终结果。
此方法的缺点可能是，对于过大的list，拷贝后可能很占内存。那么对于这种情况，可以用倒序遍历的方法来实现。
'''

print()
#  1.4 dict
# 首先是字典的增删改查有几个方法需要给大家讲解一下：
# popitem 3.5版本之前，popitem为随机删除，3.6之后为删除最后一个，有返回值
dic = {'name': '刘飞', 'age': 18}
ret = dic.popitem()
print(ret, dic)  # ('age', 18) {'name': '刘飞'}

# update
dic = {'name': '刘飞', 'age': 18}
dic.update(sex='男', height=175)
print(dic)  # {'name': '刘飞', 'age': 18, 'sex': '男', 'height': 175}

dic = {'name': 'liufei', 'age': 18}
dic.update([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
print(dic)  # {'name': 'liufei', 'age': 18, 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dic1 = {"name": "jin", "age": 18, "sex": "male"}
dic2 = {"name": "alex", "weight": 75}
dic1.update(dic2)
print(dic1)  # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
print(dic2)  # {'name': 'alex', 'weight': 75}

# fromkeys：创建一个字典：字典的所有键来自一个可迭代对象，字典的值使用同一个值。
dic = dict.fromkeys('abcd', '刘飞')
print(dic)  # {'a': '刘飞', 'b': '刘飞', 'c': '刘飞', 'd': '刘飞'}

dic = dict.fromkeys([1, 2, 3], '刘飞')
print(dic)  # {1: '刘飞', 2: '刘飞', 3: '刘飞'}

# 这里有一个坑，就是如果通过fromkeys得到的字典的值为可变的数据类型，那么你的小心了。
dic = dict.fromkeys([1, 2, 3], [])
print(dic)  # {1: [], 2: [], 3: []}
dic[1].append(666)
print(dic)  # {1: [666], 2: [666], 3: [666]}
print(id(dic[1]), id(dic[2]), id(dic[3]))  # 2207100941056 2207100941056 2207100941056

'''
循环字典，改变字典大小的问题
来，先来研究一个小题，有如下字典：
dic = {'k1':'刘飞','k2':'barry','k3': '刘飞', 'age': 18} 请将字典中所有键带k元素的键值对删除。那么拿到这个题，有人说我一个一个删除，这是不行的，因为这个字典只是举个例子，里面的元素不确定，
所以你要怎么样？你要遍历所有的键，符合的删除，对吧？ 嗯，终于上套了，哦不，上道了，请开始你的表演。
'''
dic = {'k1': '刘飞', 'k2': 'barry', 'k3': '刘飞', 'age': 18}
# for i in dic:
#     if 'k' in i:
#         del dic[i]
# print(dic)

'''
报错
RuntimeError: dictionary changed size during iteration
翻译过来是：字典在循环迭代时，改变了大小。
'''

# 这是什么意思？ 他的意思很简单，你的字典在循环时，不要改变字典的大小，只要改变大小，就会报错！那么怎么解决？？?
# 正确的做法
for i in list(dic.keys()):
    if 'k' in i:
        del dic[i]

print(dic)  # {'age': 18}

# 二. 数据类型间的转换问题
print('二、数据类型间的转换问题'.center(30, '='))
'''
咱们现在学过的数据类型有：int bool str list tuple dict set ，这些数据类型之间都存在着相互转换的问题，有些转换是非常重要的，那么有些转换则基本不用，
那么接下来我们学习一下比较重要的数据的转换问题。
'''
# int bool  str 三者转换
# int ---> bool
i = 100
print(bool(i))  # True  # 非零即True
i1 = 0
print(bool(i1))  # False 零即False

# bool ---> int
t = True
print(int(t))  # 1  True --> 1
t = False
print(int(t))  # 0  False --> 0

# int ---> str
i1 = 100
print(str(i1))  # '100'

# str ---> int  # 全部由数字组成的字符串才可以转化成数字
s1 = '90'
print(int(s1))  # 90

# str ---> bool
s1 = '太白'
s2 = ''
print(bool(s1))  # True 非空即True
print(bool(s2))  # False
# bool ---> str
t1 = True
print(str(True))  # 'True'

# str list 两者转换
# str ---> list
s1 = 'alex 刘飞 武大'
print(s1.split())  # ['alex', '太白', '武大']

# list ---> str  # 前提 list 里面所有的元素必须是字符串类型才可以
l1 = ['alex', '太白', '武大']
print(' '.join(l1))  # 'alex 太白 武大'

# list set 两者转换
# list ---> set
s1 = [1, 2, 3]
print(set(s1)) # {1, 2, 3}

# set ---> list
set1 = {1, 2, 3, 3,}
print(list(set1))  # [1, 2, 3]

print('str bytes 两者转换'.center(30, '='))
# str ---> bytes
s1 = '刘飞'
print(s1.encode('utf-8'))  # b'\xe5\xa4\xaa\xe7\x99\xbd'

# bytes ---> str
b = b'\xe5\x88\x98\xe9\xa3\x9e'
print(b.decode('utf-8'))  # '刘飞'

## 所有数据都可以转化成bool值
# 转化成bool值为False的数据类型有：
# '', 0, (), {}, [], set(), None

print()
# 三.基础数据类型的总结
print('按存储空间的占用分（从低到高）'.center(30, '='))

'''
数字
字符串
集合：无序，即无序存索引相关信息
元组：有序，需要存索引相关信息，不可变
列表：有序，需要存索引相关信息，可变，需要处理数据的增删改
字典：有序，需要存key与value映射的相关信息，可变，需要处理数据的增删改（3.6之后有序）
'''

# 按存值个数区分

'''
标量／原子类型	   数字，字符串
容器类型	       列表，元组，字典
'''

# 按可变不可变区分
'''
可变	    列表，字典
不可变	数字，字符串，元组，布尔值
'''

# 按访问顺序区分
'''
直接访问	            数字
顺序访问（序列类型）	字符串，列表，元组
key值访问（映射类型）	字典
'''