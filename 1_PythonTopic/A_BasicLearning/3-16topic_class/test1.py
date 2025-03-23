# @Version  :1.0
# @Author   :李祎凡
# @File     :test1
# @Time     :2025/3/16 下午4:13


class Person:
    name: None
    age: None
    def hi(self):
        print('Hello World')

    def cal01(self):
        num = 0
        for i in range(1,1001):
            num+=i
        return num

    def cal02(self,num):
        sum=0
        for i in range(1,num+1):
             sum+=i
        return sum

    def get_sum(self,a,b):
        return a+b

person01 = Person()
person01.hi()
print(person01.cal01())
print(person01.cal02(3))
print(person01.get_sum(1,2))