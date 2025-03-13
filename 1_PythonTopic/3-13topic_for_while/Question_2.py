# @Version  :1.0
# @Author   :李祎凡
# @File     :Question_2
# @Time     :2025/3/13 下午9:11

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a
# single line. Suppose the following input is supplied to the program: 8
# Then, the output should be: 40320

# 编写一个程序，计算给定数字的阶乘。结果应该以逗号分隔的顺序打印在单行上。
# 假设向程序提供以下输入：8那么，输出应该是：40320

def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)



num = int(input("请输入你想求的阶乘："))


print(num)
