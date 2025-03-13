# @Version  :1.0
# @Author   :李祎凡
# @File     :Question_4
# @Time     :2025/3/13 下午9:37

# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number. Suppose the following
# input is supplied to the program: 34,67,55,33,12,98 Then, the output should
# be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
#
# 编写一个程序，从console接收一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组。
# 假设向程序提供以下输入：34,67,55,33,12,98，
# 那么输出应该是：['34','67','55','33','12','98']（'34','67','55','33','12','98'）

values = input("输入逗号分割的序列")
l = values.split(",")
t = tuple(l)
print(type(l),l)
print(type(t),t)

# 输入逗号分割的序列1,2,34,5,6,7,
# <class 'list'> ['1', '2', '34', '5', '6', '7', '']
# <class 'tuple'> ('1', '2', '34', '5', '6', '7', '')