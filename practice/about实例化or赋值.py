class MyClass(object):
    i = 123456

    def __init__(self):
        self.i = 345


a = MyClass()
b = MyClass
print(a.i)
print(f"a.i的内存地址--{id(a.i)}")
print(f"a的内存地址--{id(a)}")
print('-'*30)
print(MyClass.i)
print(f"MyClass.i的内存地址--{id(MyClass.i)}")
print(f"MyClass的内存地址--{id(MyClass)}")
print('-'*30)
print(b.i)
print(f"b.i的内存地址--{id(b.i)}")
print(f"b的内存地址--{id(b)}")




# https://blog.csdn.net/s1156605343/article/details/104275730
#
# 类不带括号叫赋值，带括号叫实例化。
# 什么是实例化？
# “类提供默认行为，是实例的工厂”
# 怎么理解这句话呢？所谓工厂，就是可以用同一个模子做出很多具体的产品。类就是那个模子，实例就是具体的产品。所以，实例是程序处理的实际对象。
# 类是由一些语句组成，但是实例，是通过调用类生成，每次调用一个类，就得到这个类的新的实例。
