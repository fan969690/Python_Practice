# @Version  :1.0
# @Author   :李祎凡
# @File     :二进制求和
# @Time     :2025/3/30 下午11:32
# @Other    :文件说明

def add(a: str, b: str , bool:bool) -> int:
    if bool == True:
        return int(a) + int(b) + 1
    else:
        return int(a) + int(b)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        min = len(a) if len(a) < len(b) else len(b)
        max = list(a) if len(a) > len(b) else list(b)
        print("max类型：",type(max))
        print("max:",max)
        bool = False
        for i in range(-1, -min-1, -1):
            if add(a[i],b[i],bool) == 0:
                max[i] = '0'
                bool = False
            elif add(a[i],b[i],bool) == 1:
                max[i] = '1'
                bool = False
            elif add(a[i],b[i],bool) == 2:
                max[i] = '0'
                bool = True
            elif add(a[i],b[i],bool) == 3:
                max[i] = '1'
                bool = True
        if bool == True:
            for i in range((-min-1),-len(max)-1,-1):
                if add(max[i],0,bool) == 1:
                    max[i] = '1'
                    bool = False
                    break
                elif add(max[i],0,bool) == 2:
                    max[i] = '0'
                    bool = True
        if bool == True:
            max.insert(0,'1')
        print(max)
        return ''.join(max)


s = Solution()
print(s.addBinary('1011','1111'))

# AI优化代码
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         max_list = list(a) if len(a) > len(b) else list(b)
#         min_len = min(len(a), len(b))
#         carry = False
#
#         # 处理公共长度部分
#         for i in range(-1, -min_len - 1, -1):
#             sum_bit = int(a[i]) + int(b[i]) + carry
#             if sum_bit >= 2:
#                 max_list[i] = str(sum_bit - 2)
#                 carry = True
#             else:
#                 max_list[i] = str(sum_bit)
#                 carry = False
#
#         # 处理较长字符串剩余高位
#         idx = -min_len - 1
#         while carry and idx >= -len(max_list):
#             current_val = int(max_list[idx]) + carry
#             if current_val >= 2:
#                 max_list[idx] = '0'
#                 carry = True
#             else:
#                 max_list[idx] = str(current_val)
#                 carry = False
#             idx -= 1
#
#         # 处理最高位进位
#         if carry:
#             return '1' + ''.join(max_list)
#         return ''.join(max_list)


# 标准答案
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         x=str(int(a)+int(b))
#         y=list(map(int,x))
#         for i in range(len(y)-1,0,-1):
#             if y[i]>=2:
#                 y[i]=y[i]-2
#                 y[i-1]=y[i-1]+1
#         if y[0]>=2:
#             y[0]=y[0]-2
#             return '1'+''.join(map(str,y))
#         else:
#             return ''.join(map(str,y))