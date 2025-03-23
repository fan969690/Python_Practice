# @Version  :1.0
# @Author   :李祎凡
# @File     :House
# @Time     :2025/3/18 上午10:46
# @Other    :房屋类

import sys
from pathlib import Path

class House:
    id : int
    name : str
    phone : int
    address : str
    rent : int
    state : bool

    def __init__(self, id:int, name:str, phone:int , address:str, rent:int, state:bool):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state

    def show(self):
        state_str = "已出租" if self.state else "未出租"
        print(f"房屋编号：{self.id},房主姓名：{self.name},联系方式：{self.phone},房屋地址：{self.address},租金：{self.rent},出租状态：{state_str}")

