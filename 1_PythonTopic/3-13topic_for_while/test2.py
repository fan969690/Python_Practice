# @Version  :1.0
# @Author   :李祎凡
# @File     :test2
# @Time     :2025/3/13 下午4:08
# 打印40-200之间所有偶数

# for循环取余实现
for i in range(20,201):
    if(i%2==0):
        print(i)

# while循环加2实现
i=40
while i<=200:
    print(i)
    i+=2

# while循环取余实现
while i<=200:
    if i%2==0:
        print(i)
    i+=1