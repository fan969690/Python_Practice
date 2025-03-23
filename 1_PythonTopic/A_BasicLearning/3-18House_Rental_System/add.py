# @Version  :1.0
# @Author   :李祎凡
# @File     :add
# @Time     :2025/3/18 上午11:38
# @Other    :增加房屋功能模块
import House

def add(house_dict:dict, house: House):
    house.id = len(house_dict)+1
    house_dict[len(house_dict)+1] = house