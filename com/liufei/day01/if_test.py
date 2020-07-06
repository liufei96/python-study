'''
if 条件
    满足条件执行
else
    if条件不满足就走这段
'''

# 1. 简单的流程控制语句
AgeOfOldBody = 48

if AgeOfOldBody > 52:
    print("Too old, time to retire..")
else:
    print("还能折腾几年!")

'''
缩进
  这里必须要插入这个缩进的知识点
  
在有{}来区分代码块的情况下，缩进的作用就只剩下让代码变的整洁了。
Python是门超级简洁的语言，发明者定是觉得用{}太丑了，所以索性直接不用它，那怎么能区分代码块呢？答案就是强制缩进。

Python的缩进有以下几个原则:

    顶级代码必须顶行写，即如果一行代码本身不依赖于任何条件，那它必须不能进行任何缩进
    同一级别的代码，缩进必须一致
    官方建议缩进用4个空格，当然你也可以用2个，如果你想被人笑话的话。

多分支
'''

# if...else ...可以有多个分支条件
'''
if 条件:
    满足条件执行代码
elif 条件:
    上面的条件不满足就走这个
elif 条件:
    上面的条件不满足就走这个
elif 条件:
    上面的条件不满足就走这个    
else:
    上面所有的条件不满足就走这段
'''

age_of_oldboy = 48

guess = int(input('>>:'))

if guess > age_of_oldboy:
    print("猜的大了，往小的试试..")
elif guess < age_of_oldboy:
    print("猜的太小了，往大里试试...")
else:
    print("恭喜你，猜对了...")


# example
'''
再来个匹配成绩的小程序吧，成绩有ABCDE5个等级，与分数的对应关系如下

A    90-100
B    80-89
C    60-79
D    40-59
E    0-39

要求用户输入0-100的数字后，你能正确打印他的对应成绩
'''

score = int(input("请输入分数："))

if score > 100:
    print("我擦，最高分才100分，你要逆天吗？")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
elif score >= 0:
    print("E")
else:
    print("分数不能少于0")








