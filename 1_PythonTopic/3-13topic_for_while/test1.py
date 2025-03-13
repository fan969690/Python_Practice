# @Version  :1.0
# @Author   :李祎凡
# @File     :test1
# @Time     :2025/3/13 下午3:29
# 打印1-100之间能被3整除的数


# for循环实现
for i in range(1,101):
    if i%3==0:
        print(i)


#while循环实现
i=1
while i<=100:
    if i % 3 == 0:
        print(i)
    i=i+1
