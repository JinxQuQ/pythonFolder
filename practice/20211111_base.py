#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义数字
num = 12
# 定义字符串
name = "李雷"
# 定义数组
list1 = [1, 2, 3, ['a', 4], 'b', 5]
list2 = ['金克丝', '拉克丝', ['贾克斯', '亚托克斯']]
# 定义元祖
yuanzu = ("jinx", 2, 3)

print(num)
print(name)
# 输出元祖
print(yuanzu[0])
# list的角标是从0开始的
print(list1[2] + list1[3][1])
print("type-{0[1]}{0[3][1]}-{1[2][1]}".format(list1, list2))

#  "{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序
# 'hello world'
#  "{0} {1}".format("hello", "world")  # 设置指定位置
# 'hello world'
#  "{1} {0} {1}".format("hello", "world")  # 设置指定位置
# 'world hello world'
print('我要输出{0}+{1}'.format(list1[2] + list1[3][1], num))
# 也可以自定义
print('type {a}&{b}'.format(a='love', b='U'))

# format的一种变形写法
print(f"{list1[3][1]}={list2[2][1]}={yuanzu[0]}")

# 占位符：%s,%d,%f
# 1) %s表示将参数格式化为字符串
# 2) %d表示将参数格式化为整数
# 3) %.1f表示将参数格式化为带有1位小数点的浮点数
print('type+%s' % num)
