# 格式化输出
"""
现有一练习需求，问用户的姓名、年龄、工作、爱好 ，然后打印成以下格式
------------ info of 刘翊扬  -----------
Name  : 刘翊扬
Age   : 25
job   : 程序员
Hobbies: girl
------------- end -----------------
"""
name = input("Name:")
age = input("Age:")
job = input("Job:")
hobbies = input("Hobbies:")

# 注意：下面的多行注解下，不能再放单行注解
# %s就是代表字符串占位符，除此之外，还有%d,是数字占位符， 如果把上面的age后面的换成%d，就代表你必须只能输入数字啦
info = '''
--------- info of %s -------------  
Name    : %s
Age    : %s
Job    : %s
Hobbies    : %s
---------- end -------
''' % (name, name, age, job, hobbies)
print(info)

"""
while 条件:
    # 循环体
    # 如果条件为真，那么循环体则执行
    # 如果条件为假，那么循环体不执行
"""
# while True:
#     print('痒')
#     print('社会摇')
#     print('喜洋洋')
#     print('我要这铁棒有何用')

# 那么如何终止循环
"""
1. 改变条件(根据上面的流程，只要改变条件，就会终止循环)。
2. 关键字：break。
3. 调用系统命令：quit(),exit() 后面会讲到，不建议大家使用。
4. 关键字：continue（终止本次循环）
"""

flag = True
while flag:
    print('痒')
    print('社会摇')
    print('喜洋洋')
    flag = False
    print('我要这铁棒有何用')

# practice 1: 输出 1~100 之间的数

count = 1
# while count <= 100:
#     print(count)
#     count = count + 1


# practice2 :求1~100的和
sum = 0
while count <= 100:
    sum = count + sum
    count = count + 1
print(sum)

# 终止循环的第二方法：break
"""
break：很简单，就是Python给大家提供的关键字，什么是关键字？就是python中具有一定特殊意义的单词，
比如if，str，int等，这些不能用作变量对吧？ 

那么break的用法是什么？ 即：循环中，只要遇到break马上退出循环
"""
flag = True
print(111)
while flag:
    print('痒')
    print('社会摇')
    print('喜洋洋')
    break
    print('我要这铁棒有何用')
print(222)

# practice3 :求1~100所有的偶数
s = 2
while s <= 100:
    if s % 2 == 0:
        print(s)
    s = s + 1

# continue终止本次循环，继续下一次循环
flag = True
print(111)
# while flag:
#     print('痒')
#     print('社会摇')
#     print('喜洋洋')
#     continue
#     print('我要这铁棒有何用')
# print(222)


# while ... else ...
# while 后面的else 作用是指，当while 循环正常执行完，中间没有被break 中止的话，就会执行else后面的语句

count = 0
while count <= 5:
    count += 1
    if count == 3:break
    print("Loop", count)

else:
    print("循环正常执行完啦")
print("-----out of while loop ------")





