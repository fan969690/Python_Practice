# @Version  :1.0
# @Author   :李祎凡
# @File     :Question_1
# @Time     :2025/3/13 下午9:04

# Write a program which will find all such numbers which are
# divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in
# a comma-separated sequence on a single line.
#
# 编写一个程序，找出2000到3200之间所有能被7整除但不是5的倍数的数字
# （两者都包括在内）。获得的数字应以逗号分隔的顺序打印在一行上。
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(f"{i},",end='')

# 标准答案
l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

print(','.join(l))