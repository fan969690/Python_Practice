# @Version  :1.0
# @Author   :李祎凡
# @File     :question6
# @Time     :2025/3/18 下午6:27
# @Other    :文件说明
# Question: Write a program that calculates and prints the value according to the given
# formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C
# is 50. H is 30. D is the variable whose values should be input to your program in a
# comma-separated sequence. Example Let us assume the following comma separated input
# sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24
# Hints: If the output received is in decimal form, it should be rounded off to its
# nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console
# input.
# 写一个程序，根据给定的公式计算并输出值：Q =根号[(2 * C * D)/H]以下是C和H的固定值：C为50。H是30。D是一个变量，
# 它的值应该以逗号分隔的顺序输入到程序中。假设给程序以逗号分隔的输入序列：100,150,180，
# 程序的输出应该是：18,22,24

import math

c = 50
h = 30
value = []
item = [n for n in input("输入以逗号分隔的值").split(",")]
for d in item:
    value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
print(','.join(value))