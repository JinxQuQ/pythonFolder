#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def update():
    list = ['金克丝', '拉克丝', ['贾克斯', '亚托克斯']]
    print(list)
    list[2][0] = 9
    print(list)


# 调用函数
update()


# 定义函数
def update(name):
    list = ['金克丝', '拉克丝', ['贾克斯', '亚托克斯']]
    print(list)
    list[2][0] = name
    print(list)


# 调用函数
update("皮克斯")


# 定义函数
def change(num):
    sum = num + 3
    print(sum)


change(8)
