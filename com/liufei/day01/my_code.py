
# python小数据池，代码块的最详细、深入剖析

# 一，id，is，==

'''
在Python中，id是什么？id是内存地址，那就有人问了，什么是内存地址呢？
你只要创建一个数据（对象）那么都会在内存中开辟一个空间，将这个数据临时加在到内存中，
那么这个空间是有一个唯一标识的，就好比是身份证号，标识这个空间的叫做内存地址，也就是这个数据（对象）的id，
那么你可以利用id（）去获取这个数据的内存地址：
'''

name = '刘飞'
print(id(name)) # 2064147392240  每次都不一样

'''
那么 is 是什么？ == 又是什么？

== 是比较的两边的数值是否相等，而 is 是比较的两边的内存地址是否相等。 如果内存地址相等，那么这两边其实是指向同一个内存地址。
'''

l1 = 1000
l2 = 1000
print(l1 is l2) # True
print(l1 == l2) # True

## 可以说如果内存地址相同，那么值肯定相同，但是如果值相同，内存地址不一定相同。

# 2. 代码块
'''
根据官网提示我们可以获知：
根据提示我们从官方文档找到了这样的说法：
A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a unit. The following are blocks: a module, a function body, and a class definition. Each command typed interactively is a block. A script file (a file given as standard input to the interpreter or specified as a command line argument to the interpreter) is a code block. A script command (a command specified on the interpreter command line with the ‘-c‘ option) is a code block. The string argument passed to the built-in functions eval() and exec() is a code block.
A code block is executed in an execution frame. A frame contains some administrative information (used for debugging) and determines where and how execution continues after the code block’s execution has completed.
'''

'''
上面的主要意思是：
Python程序是由代码块构造的。块是一个python程序的文本，他是作为一个单元执行的。
代码块：一个模块，一个函数，一个类，一个文件等都是一个代码块。
而作为交互方式输入的每个命令都是一个代码块。
什么叫交互方式？就是咱们在cmd中进入Python解释器里面，每一行代码都是一个代码块，例如：
'''

'''
那么，可能有的同学还有一些不理解代码块，可以这样解释：我们都上过学对吧，你们在初中的时候，有没有过值周？就以一个班的学生用一星期的时间打扫整个学校，
再比如有没有运动会，无论是值周，还是运动会，还是组织什么活动，都是以什么为单位呢？对，都是以班级为单位，那么咱们学生就好比是代码，
班级就好比是代码块，我们想让代码运行起来，必须依靠班级去执行，也就是代码块。
OK，那么现在我们了解了代码块，这和小数据池有什么关系呢？且听下面分析。
'''

# 3. 代码块的缓存机制
'''
前提条件：在同一个代码块内。
机制内容：Python在执行同一个代码块的初始化对象的命令时，会检查是否其值是否已经存在，如果存在，会将其重用。换句话说：执行同一个代码块时，遇到初始化对象的命令时，他会将初始化的这个变量与值存储在一个字典中，
    在遇到新的变量时，会先在字典中查询记录，如果有同样的记录那么它会重复使用这个字典中的之前的这个值。所以在你给出的例子中，文件执行时（同一个代码块）会把i1、i2两个变量指向同一个对象，
    满足缓存机制则他们在内存中只存在一个，即：id相同。
适用对象： int（float），str，bool。
对象的具体细则：（了解）
　　int(float):任何数字在同一代码块下都会复用。
　　bool:True和False在字典中会以1，0方式存在，并且复用。
　　str：几乎所有的字符串都会符合缓存机制，具体规定如下（了解即可！）：
'''

# 3.1 非乘法得到的字符串都满足代码块的缓存机制：
s1 = "liufei@huawei.com"
s2 = "liufei@huawei.com"
print(s1 is s2) # True

# 3.2 乘法得到的字符串分两种情况：
## 乘数为1时，任何字符串满足代码块的缓存机制：
s1 = "liufei@huawei.comaaaaaaaaaaaaaaaaaaaaa" * 1
s2 = "liufei@huawei.comaaaaaaaaaaaaaaaaaaaaa" * 1
print(s1 is s2) # True

## 乘数>=2时：仅含大小写字母，数字，下划线，总长度<=20，满足代码块的缓存机制：
s1 = 'liufei_' * 5
s2 = 'liufei_' * 5
print(s1 is s2) # True
print(len(s1)) # 现在 <= 20这个条件没有了。python 3.8

'''
 优点：能够提高一些字符串，整数处理人物在时间和空间上的性能；需要值相同的字符串，整数的时候，直接从‘字典’中取出复用，
 避免频繁的创建和销毁，提升效率，节约内存。
'''

# 3. 小数据池
'''
小数据池，不同代码块的缓存机制，也称为小整数缓存机制，或者称为驻留机制等等，博主认为，只要你在网上查到的这些名字其实说的都是一个意思，
叫什么因人而异。
那么到底什么是小数据池？他有什么作用呢？
前提条件：在不同一个代码块内。
机制内容：官方对于整数，字符串的小数据池是这么说的:
'''

'''
来，我给你们翻译并汇总一下，这个表达的意思就是：
Python自动将-5~256的整数进行了缓存，当你将这些整数赋值给变量时，并不会重新创建对象，而是使用已经创建好的缓存对象。
python会将一定规则的字符串在字符串驻留池中，创建一份，当你将这些字符串赋值给变量时，并不会重新创建对象， 而是使用在字符串驻留池中创建好的对象。
　　其实，无论是缓存还是字符串驻留池，都是python做的一个优化，就是将~5-256的整数，和一定规则的字符串，放在一个‘池’（容器，或者字典）中，无论程序中那些变量指向这些范围内的整数或者字符串，那么他直接在这个‘池’中引用，言外之意，就是内存中之创建一个。
适用对象： int（float），str，bool 
对象的具体细则：（了解即可）
int：那么大家都知道对于整数来说，小数据池的范围是-5~256 ，如果多个变量都是指向同一个（在这个范围内的）数字，他们在内存中指向的都是一个内存地址。
'''

n1 = 100
n2 = 100
n3 = 100
print(id(n1), id(n2), id(n3))

## 那么对于字符串的规定呢？
## str:字符串要从下面这几个大方向讨论（了解即可！）：
## 1,字符串的长度为0或者1，默认都采用了驻留机制（小数据池）。
### 3.1 乘数为1时：
## 仅含大小写字母，数字，下划线，默认驻留。
s1 = 'djsakdsaDSAKDLASkldsa_dkaldasldklas'
s2 = s1 * 1
print(s1 is s2) # True

### 含其他字符，长度<=1,默认驻留。
s1 = '@#'
s2 = '@#'
print(s1 is s2) # True

# 指定驻留
s1 = '@#' * 20
s2 = '@#' * 20
print(s1 is s2) # True

print()
from sys import intern
a = intern('hello!@'*20)
b = intern('hello!@'*20)
print(a is b) # True

'''
bool值就是True，False，无论你创建多少个变量指向True，False，那么他在内存中只存在一个。
看一下用了小数据池（驻留机制）的效率有多高：
显而易见，节省大量内存在字符串比较时，非驻留比较效率o(n)，驻留时比较效率o(1)。
'''

'''
优点：能够提高一些字符串，整数处理人物在时间和空间上的性能；需要值相同的字符串，整数的时候，
直接从‘池’里拿来用，避免频繁的创建和销毁，提升效率，节约内存s
'''

# 四、小结
'''
如果在同一代码块下，则采用同一代码块下的换缓存机制。
如果是不同代码块，则采用小数据池的驻留机制。
'''

'''
通过交互方式中执行下面代码：   # 这是不同代码块下，则采用小数据池的驻留机制。
>>> i1 = 1000
>>> i2 = 1000
>>> print(i1 is i2)
False  # 不同代码块下的小数据池驻留机制 数字的范围只是-5~256.
'''


def func():
    i1 = 1000
    print(id(i1))


def func2():
    i1 = 1000
    print(id(i1))


func()
func2()
