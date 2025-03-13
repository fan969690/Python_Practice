# @Version  :1.0
# @Author   :李祎凡
# @File     :test4
# @Time     :2025/3/13 下午4:20
# 打印1-100之间所有是9的倍数的整数,统计个数及总和

i = 1
num = 0
sum = 0
while i <= 100:
    if i % 9 == 0:
        print(i)
        num+=1
        sum+=i
    i+=1
print(f"总数有：{num},总和为：{sum}")