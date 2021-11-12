#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义一个类
class ClassName:
    # 类中默认函数
    def __init__(self):
        # 忽略这个类
        pass

    # 定义函数
    def update(name):
        list = ['金克丝', '拉克丝', ['贾克斯', '亚托克斯']]
        # print(list)
        list[2][0] = name
        print(list)
        return list


# 实例化对象，将类赋予给jinx
jinx = ClassName
# 调用类中的方法
jinx.update("傻呗")
