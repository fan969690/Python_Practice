# @Version  :1.0
# @Author   :李祎凡
# @File     :test1
# @Time     :2025/3/14 上午10:46

# 求n的斐波那契数列 使用递归

def fb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return  fb(n-1) + fb(n-2)

print(fb(int(input("输入一个数字："))))