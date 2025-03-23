# @Version  :1.0
# @Author   :李祎凡
# @File     :test8
# @Time     :2025/3/13 下午7:24
# 某人有10万块钱，每经过一次路口需要缴费，缴费的规则是这个样子的，
# 当他的现金大于5万的时候，每次交5%就够了，
# 当现金小于等于5万的时候，每次交1000块钱编程计算该人可以经过多少次路口
money = 100000
cishu = 0

while 1:
    if money > 50000:
        money -= money*0.05
        cishu += 1
    elif money >= 1000:
        money -= 1000
        cishu += 1
    else:
        break
print(f"总共经过路口{cishu}次")