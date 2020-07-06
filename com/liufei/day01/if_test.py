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