"""
列表相比于字符串，不仅可以储存不同的数据类型，而且可以储存大量数据，
32位python的限制是 536870912 个元素,
64位python的限制是 1152921504606846975 个元素。
而且列表是有序的，有索引值，可切片，方便取值。
"""

# 1. 创建列表的三种方式
print("======= 创建列表的三种方式 =======")
## 方式1：（常用）
list1 = [1, 2, 'list']
print(list1)

## 方式二：不常用
list2 = list()  # 空列表
# list3 = list(iterable) # 可迭代对象
list1 = list("123")
print(list1) # ['1', '2', '3']

## 方式三：列表推导式
list3 = [i for i in range(1, 5)]
print(list3) # [1, 2, 3, 4]


# 2. 列表索引的切片
print()
print("======= 列表索引的切片 =======")

list4 = ["a", "b", "翊扬", 3, 666]
print(list4[0])   # a['a', '翊扬', 666]
print(list4[-1])  # 666
print(list4[1:3]) # ['b', '翊扬']
print(list4[:-1]) # ['a', 'b', '翊扬', 3]
print(list4[::2]) # 步长是2。['a', '翊扬', 666]
print(list4[::-1])  # [666, 3, '翊扬', 'b', 'a']   倒叙排序

# 3. 增加
# append追加，给列表的最后面追加一个元素
print("========= 增加元素 ==========")
l = [1, 2, "a"]
print(l)
l.append("aa")
print(l)

# insert 插入在列表的任意位置
l.insert(0, 11)
print(l)

# extend 迭代着追加，在列表的最后面迭代着追加一组数据
l = [1, 2, "a"]
l.extend("翊扬aa")
print(l)  # [1, 2, 'a', '翊', '扬', 'a', 'a']

# 删除
print()
print("====== 删除 ======")
# pop 通过索引删除列表中对应的元素，该方法有返回值，返回值为删除的元素
l = ["太白", "alex", "Wusir", "女神", 34]
ret = l.pop(1)
print(ret)
print(l)

# remove 通过元素删除列表中的元素
l = ["太白", "alex", "Wusir", "女神", 34]
l.remove("alex")
print(l)

# clear清空列表
l = ["太白", "alex", "Wusir", "女神", 34]
l.clear()
print(l)

# del
# 按照索引进行删除
l = ["太白", "alex", "Wusir", "女神", 34]
del l[2]
print(l)

# 切片删除该元素
l = ["太白", "alex", "Wusir", "女神", 34]
del l[1:]
print(l)

# 切片（步长删除）
l = ["太白", "alex", "Wusir", "女神", 34]
del l[1::2]
print(l)

# 该。
print()
print("====== 修改 ======")

# 按照索引修改
l = ["太白", "alex", "Wusir", "女神", 34]
l[0] = "翊扬"
print(l)

# 按照切片改值（迭代着添加）
l = ["太白", "alex", "Wusir", "女神", 34]
l[1:3] = "abcdefg"
print(l)

# 按照切片，步长改值（必须一一对应）
l = ["太白", "alex", "女神", 34, "wosj"]
print(l[::2])
l[::2] = "对应1"
print(l)   # ['对', 'alex', '应', 34]