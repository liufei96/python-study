#!/usr/bin/env python

print("hello,world")

# name = input("What is your name?")
# age = input("How old are you?")
# hometown = input("Where is your hometown?")
#
# print("Hello ", name, "your are ", age, "years old, you came from", hometown)

# 2. 格式化输出

# '''
# ------------ info of 太白金星  -----------
# Name  : 太白金星
# Age   : 22
# job   : Teacher
# Hobbie: girl
# ------------- end -----------------
# '''

# name = input("Name:")
# age = input("Age:")
# job = input("Job:")
# hobbie = input("Hobbie:")
#
# info = '''
# ------------ info of %s -----------
# Name  : %s  #代表 name
# Age   : %d  #代表 age
# job   : %s  #代表 job
# Hobbie: %s  #代表 hobbie
# ------------- end -----------------
# ''' % (name, name, int(age), job, hobbie)  # 这行的 % 号就是 把前面的字符串 与拓号 后面的 变量 关联起来
#
# print(info)

# %s就是代表字符串占位符，除此之外，还有%d,是数字占位符， 如果把上面的age后面的换成%d，就代表你必须只能输入数字啦
# %d 代表的是数字，但是input 语句接收的数据默认是string类型的

msg = "我是%s,年龄%d,目前学习进度为80%%" % ('刘飞', 26)
print(msg)


print('喜欢' in 'dkfljadklf喜欢hfjdkas')
print('a' in 'bcvd')
print('y' not in 'ofkjdslaf')
