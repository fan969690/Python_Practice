# @Version  :1.0
# @Author   :李祎凡
# @File     :test2
# @Time     :2025/3/14 上午11:15

def peach(day):
    if day == 10:
        return 1
    else:
        return (peach(day + 1) + 1)*2

print(peach(int(input("请输入天数"))))