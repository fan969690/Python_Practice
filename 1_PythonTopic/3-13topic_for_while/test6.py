# @Version  :1.0
# @Author   :李祎凡
# @File     :test6
# @Time     :2025/3/13 下午4:56
# 打印空心金字塔

total = int(input("请输入层数"))


for i in range(1,total + 1):
    for j in range(total - i):
        print(" ",end='')
    for k in range(2*i-1):
        if k == 0 or k == 2*(i-1) or i == total:
            print("*",end='')
        else:
            print(" ",end="")
    print("")