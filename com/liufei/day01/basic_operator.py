# python的基本运算符
"""
运算符
计算机可以进行的运算有很多种，可不只加减乘除这么简单，运算按种类可分为算数运算、比较运算、逻辑运算、赋值运算、成员运算、身份运算、位运算，
今天我们暂只学习算数运算、比较运算、逻辑运算、赋值运算、成员运算

算数运算
a=10,b=20
a + b = 20
a - b = -10
a * b = 200
b / a = 2
b % a = 0
a ** b = 100000000000000000000(10的20此房)
9 // 2 = 4 (除法取整)

# 1. 算数运算
"""
a = 10
b = 20
print(a + b)
print(a - b)
print(b * a)
print(b / a)
print(a ** b)
print(9 // 2)  # 得到的是商

# 2.比较运算符
"""
==   等于，比较对象是否相等  (a==b) 返回False
!=   不等于，比较两个对象是否不相等（a!=b）True
<>   不等于，比较两个对象是否不相等（a<>b）True
>
<
>=
<=
"""

# 3. 赋值运算法
"""
=   简单的赋值
+=  加法赋值运算符
-=  减法赋值运算符    c  -= a  =>  c = c - a
*=  惩罚赋值运算符    c *= a  => c = c * a
/=  除法赋值运算符    c /= a  => c = c / a
%=  取模赋值运算符    c %= a  => c = c % a
**= 幂赋值运算符      c **= a => c = c ** a
//= 取整数赋值运算符   c//=a  =>  c = c // a
"""
print("赋值运算法：")
c = a + b
print(c)
c += a  # 相等于 c = c + a
print(c)


# 4. 逻辑运算符
"""
and   都为True才为True
or    都为False，才为False
not   非，取反

1,在没有()的情况下not 优先级高于 and，and优先级高于or，即优先级关系为( )>not>and>or，同一优先级从左往右计算。
"""

print("逻辑运算符")
print(8 or 3)        # or中， 至少有一个非0时，返回第一个非0
print(0 and 3)       # and中含0，返回0； 均为非0时，返回后一个值
print(0 or 4 and 3 or 7 or 9 and 6)


# 5.成员运算
"""
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
in 如果指定的序列中找到值返回True，否则返回False
not in 如果在指定的序列中没有找到值返回True，否则返回False
"""
print()
print("成员运算:")
print('喜欢' in 'dkfljadklf喜欢hfjdkas')
print('a' in 'bcvd')
print('y' not in 'ofkjdslaf')

# 5. python运算符的优先级
"""
 ** 	    指数 (最高优先级)
 ~ + - 	    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
 * / % // 	乘，除，取模和取整除
 + - 	    加法减法
 >> << 	    右移，左移运算符
 & 	        位 'AND'
 ^ | 	    位运算符
 <= < > >= 	比较运算符
 <> == != 	等于运算符
 = %= /= //= -= += *= **= 	赋值运算符
 s is not 	身份运算符
 in not in 	成员运算符
 not and or 	逻辑运算符
"""