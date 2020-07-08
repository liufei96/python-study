# 什么是数据类型？
"""
整数(int) ,字符串(str),布尔值(bool),列表(list),元组(tuple),字典(dict),集合(set).
 int。数字：主要用于运算。1 ，2,3...
 bool。判断真假：True, False.
 str。简单少量的储存数据，并进行相应的操作。name = 'alex',
 tuple。只读，不能更改。(1,'alex')
 list：大量有序数据，[1,'ses',True,[1,2,3],{'name':'jinxin'}]
 dict：大量数据，且是关联性比较强的数据  {'name':'jinxin','age':18,'name_list':['张三'，'李四']}

"""

# 1.数字int类型
"""
十进制转换成二进制
  方式：除2取余，逆序排列
二进制转换成十进制
 例如：二进制数1101.01转化成十进制

    1101.01（2）=1*20+0*21+1*22+1*23 +0*2-1+1*2-2=1+0+4+8+0+0.25=13.25（10）

    所以总结起来通用公式为：

    abcd.efg(2)=d*20+c*21+b*22+a*23+e*2-1+f*2-2+g*2-3（10）

2.2.2 int操作方法

    因为数字主要是用于计算，所以针对于数字可以使用的方法除了那些运算之外，没有什么经常会用的方法，
    python给咱们提供了一种方法：bit_length()就是帮助你快速的计算整数在内存中占用的二进制码的长度.
    
"""

num = 100    # 转换成二进制是 110 0100
print(num.bit_length())

# 2.布尔值bool
"""
布尔值就两种：True，False。就是反应条件的正确与否。

真   1   True。

假   0   False。  

这里补充一下int str bool 三者数据类型之间的转换。
"""

# int ---> bool
i = 100
print(bool(i))  # True，非零即True

i1= 0
print(bool(i1))

# bool --> int
t = True
print(int(t))   # True为1
t = False
print(int(t))  # False 0

# int  ---> str
i1 = 100
print(str(i1))

# str --> int
s1 = '90'
print(int(s1))

# str --> bool
s1 = '翊扬'
s2 = ''
print(bool(s1))  # 非空即为True
print(bool(s2))  # False

# bool --> str
t1 = True
print(str(t1))




