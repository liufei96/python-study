
# 常用模块

# 一，什么是模块
print('一，什么是模块'.center(30, '*'))

'''
常见的场景：一个模块就是一个包含了python定义和声明的文件，文件名就是模块名字加上.py的后缀。

   但其实import加载的模块分为四个通用类别：　

　　1 使用python编写的代码（.py文件）

　　2 已被编译为共享库或DLL的C或C++扩展

　　3 包好一组模块的包

　　4 使用C编写并链接到python解释器的内置模块

为何要使用模块？

   如果你退出python解释器然后重新进入，那么你之前定义的函数或者变量都将丢失，因此我们通常将程序写到文件中以便永久保存下来，需要时就通过python test.py方式去执行，此时test.py被称为脚本script。

    随着程序的发展，功能越来越多，为了方便管理，我们通常将程序分成一个个的文件，这样做程序的结构更清晰，方便管理。这时我们不仅仅可以把这些文件当做脚本去执行，还可以把他们当做模块来导入到其他的模块中，实现了功能的重复利用，

'''

# 二，序列化模块。
print('二，序列化模块。'.center(30, '*'))
# 什么叫序列化——将原本的字典、列表等内容转换成一个字符串的过程就叫做序列化。

'''
比如，我们在python代码中计算的一个数据需要给另外一段程序使用，那我们怎么给？
现在我们能想到的方法就是存在文件里，然后另一个python程序再从文件里读出来。
但是我们都知道，对于文件来说是没有字典这个概念的，所以我们只能将数据转换成字典放到文件中。
你一定会问，将字典转换成一个字符串很简单，就是str(dic)就可以办到了，为什么我们还要学习序列化模块呢？
没错序列化的过程就是从dic 变成str(dic)的过程。现在你可以通过str(dic)，将一个名为dic的字典转换成一个字符串，
但是你要怎么把一个字符串转换成字典呢？
聪明的你肯定想到了eval()，如果我们将一个字符串类型的字典str_dic传给eval，就会得到一个返回的字典类型了。
eval()函数十分强大，但是eval是做什么的？e官方demo解释为：将字符串str当成有效的表达式来求值并返回计算结果。
ＢＵＴ！强大的函数有代价。安全性是其最大的缺点。
想象一下，如果我们从文件中读出的不是一个数据结构，而是一句"删除文件"类似的破坏性语句，那么后果实在不堪设设想。
而使用eval就要担这个风险。
所以，我们并不推荐用eval方法来进行反序列化操作(将str转换成python中的数据结构)
'''

# 序列化的目的
#
# 1、以某种存储形式使自定义对象持久化；
# 2、将对象从一个地方传递到另一个地方。
# 3、使程序更具维护性。

'''
| Python      |     JSON      |

| dict           |     object    |

| list, tuple   |     array     |

| str             |     string    |

| int, float     |    number  |

| True           |      true     |

| False          |      false     |
 
| None          |       null     |

Python可序列化的数据类型
'''