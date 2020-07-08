# 介绍str的方法
# 2.3 字符串
print("========= 字符串内容 =======")
## Python中凡是用引号引起来的数据可以称为字符串类型，组成字符串的每个元素称之为字符，将这些字符一个一个连接起来，然后在用引号起来就是字符串。

s1 = "翊扬NB"   # 对于s1这个字符串来说，他是由四个字符组成：翊，扬，N，B

## 2.3.1 字符串的索引和切片

a = 'ABCDEFGHIJK'
print(a[0])
print(a[10])
#print(a[11])  超过下标，会报错

## 切片。顾头不顾尾
print(a[0:3])
print(a[:])     # 默认到最后
print(a[:-1])   # -1 是列表中最后一个元素的索引，但是要满足顾头不顾腚的原则，所以取不到K元素
print(a[:5:2])  # 加步长

# 2.3.2 字符串常用的方法

print("====== 字符串常用的方法 =====")
# 数 字符串中元素出现的个数
# ret3 = a1.count("a",0,4) # 可切片
# print(ret3)

a4 = "dkfjdkfasf54"
# startswith 判断是否以。。。开头
# endswith  判断是否以。。。结尾
ret4 = a4.endswith('jdk', 3, 6)   # 顾头不顾ding
print(ret4)   # True

ret5 = a4.startswith("kfj", 1, 4)
print(ret5)  # True

#split 以什么分割，最终形成一个列表此列表不含有这个分割的元素。
ret9 = 'title,Tilte,atre,'.split('t')
print(ret9)
ret91 = 'title,Tilte,atre,'.rsplit('t', 1) # 数字1 表示最终的结果是2列
print(ret91)

# format的三种玩法 格式化输出
res = "{} {} {}".format("egon", 18, "yiyang")
print(res)
res = "{1} {0} {1}".format("egon", 18, "yiyang")
print(res)
res = "{name} {age} {sex}".format(sex='male', age=18, name="yiyang")
print(res)

#strip
name = "*barry**"
print(name.strip("*"))  # 去掉两边的*，中间的去不掉
print(name.lstrip("*"))  # 去掉左边的*
print(name.rstrip("*"))  # 去掉右边的*

#replace替换
name='alex say :i have one tesla,my name is alex'
print(name.replace("alex", "SB"))
print(name.replace("alex", "SB", 1))  # 1 表示只替换1个

# is系列
name = "yiyang123"
print(name.isalnum()) # 字符串由字母或数组组成
print(name.isalpha()) # 字符串是由字母组成
print(name.isdecimal()) #字符串是由十进制组成

#############下面这些方法在数据类型补充时会讲到，现在不讲####################
#寻找字符串中的元素是否存在
a4 = "dkfjdkfasf54"
ret6 = a4.find("fjdk", 1 , 6)
print(ret6)  # 返回的找到的元素的索引，如果找不到返回-1

# ret61 = a4.index("fjdk", 4, 6)
# print(ret61) # 返回的找到的元素的索引，找不到报错。

# captalize,swapcase,title
print(name.capitalize())  # 首字母大写
print(name.swapcase())  # 大小写翻转
msg = "yiyang say hello"
print(msg.title()) # 每个单词首字母大写

# 内容居中,总长度，空白处填充
ret2 = msg.center(21, "*")
print(ret2)