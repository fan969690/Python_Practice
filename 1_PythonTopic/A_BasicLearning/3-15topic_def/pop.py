# @Version  :1.0
# @Author   :李祎凡
# @File     :pop
# @Time     :2025/3/15 下午8:13
from random import randrange


# 随机生成n个1-100之间的数字，存放在数列中
def list(num):
    list = []
    for i in range(num):
        list.append(randrange(1,100))
    return list

# 冒泡排序
def pop(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                num = list[j]
                list[j] = list[j+1]
                list[j+1] = num


list = list(10)
print(list,type(list),type(list[0]))
pop(list)
print(list)