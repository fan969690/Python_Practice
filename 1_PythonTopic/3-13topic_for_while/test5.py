# @Version  :1.0
# @Author   :李祎凡
# @File     :test5
# @Time     :2025/3/13 下午4:26
# 完成表达式输出 如输入6输出0+6，1+5，2+4，---6+0

num=0
start = 0
num = int(input("请输入一个数:"))
# stop = num
# while start != stop:
#     print(start," + ",num," = ",start+num)
#     start += 1
#     num -= 1

while start <= num:
    print(f"{start} + {num-start} = {num}")
    start+=1