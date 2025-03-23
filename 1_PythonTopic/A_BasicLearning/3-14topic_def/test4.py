# @Version  :1.0
# @Author   :李祎凡
# @File     :test4
# @Time     :2025/3/14 下午12:02

def hanoi_tower( num , a , b , c ):
    if num == 1:
        print("第一个盘从：",a,"->",c)
    else:
        hanoi_tower(num-1 , a, c , b )
        print(f"第{num}个盘从：{a} -> {c}")
        hanoi_tower(num-1,b,a,c)


hanoi_tower(2,"A","B","C")