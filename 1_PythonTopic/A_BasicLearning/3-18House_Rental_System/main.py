# @Version  :1.0
# @Author   :李祎凡
# @File     :main
# @Time     :2025/3/18 上午10:51
# @Other    :系统主界面
from House import House
from add import add

house1 = House(1,"李一凡",18739178900,"武陟县",800,False)
house2 = House(2,"柯舒舒",18185891016,"焦作市",1000,False)
house3 = House(3,"王王王",19522460489,"武陟县",800,True)
house4 = House(4,"芳芳芳",12312312312,"东京",1200,False)
house5 = House(5,"白白白",67867867878,"北京",800,False)
Houselist = {1:house1,2:house2,3:house3,4:house4,5:house5}

while 1 :
    print("===========房屋出租系统===========")
    print("1----------查看所有房屋----------")
    print("2----------编号查找房屋----------")
    print("3------------增加房屋-----------")
    print("4----------编号修改房屋----------")
    print("5----------编号删除房屋----------")
    print("0------------退出系统-----------")
    print("===========房屋出租系统===========")
    num = int(input("请输入要使用的功能编号:"))
    if num == 1:
        for key in Houselist:
            Houselist[key].show()
    elif num == 2:
        id = int(input("请输入要查找的房屋编号:"))
        Houselist[id].show()
    elif num == 3:
        id = 0
        name = input("请输入房主姓名：")
        phone = int(input("请输入房主电话："))
        address = input("请输入房屋地址：")
        rent = int(input("请输入房屋租金："))
        state = input("请输入房屋是否出租：Y/N")
        if state == "Y":
            state = True
        elif state == "N":
            state = False
        new_house = House(id,name,phone,address,rent,state)
        add(Houselist,new_house)
    elif num == 4:
        print("编号修改房屋")
    elif num == 5:
        print("编号删除房屋")
    elif num == 0 :
        print("退出")
        break