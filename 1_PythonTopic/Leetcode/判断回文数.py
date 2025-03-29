# @Version  :1.0
# @Author   :李祎凡
# @File     :判断回文数
# @Time     :2025/3/23 下午10:34
# @Other    :文件说明
class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1 = []
        if x < 0:
            return False
        if x == 0:
            return True
        i = 1
        while 1:
            if x / i >= 1:
                list1.append(int(x%(i*10)/i))
                i = i*10
                print(list1)
            else:
                break
        len_num = len(list1)
        for i in range(0,len_num):
            if list1[i] != list1[len_num-i-1]:
                return False
            elif i == len_num-i:
                return True
            elif i+1 == len_num-i:
                return True

print(Solution().isPalindrome(12321))
# print(int(16361%100000/10000))