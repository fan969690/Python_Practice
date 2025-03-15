# @Version  :1.0
# @Author   :李祎凡
# @File     :test3
# @Time     :2025/3/14 上午11:31

def f(n):
        if n == 1:
            return 3
        else:
            return 2*f(n-1)+1


print(f(int(input("请输入一个n："))))