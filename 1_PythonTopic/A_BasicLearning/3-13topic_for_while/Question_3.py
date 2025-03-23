# @Version  :1.0
# @Author   :李祎凡
# @File     :Question_3
# @Time     :2025/3/13 下午9:21

# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary. Suppose the following input is
# supplied to the program: 8 Then, the output should
# be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# 给定一个整数n，编写一个程序生成一个包含（i, i*i）的字典，该字典是1到n之间的整数（包括两者）。
# 然后程序应该输出字典。那么，输出应该是：{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}

n = int(input('输入一个数: '))
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print(d)