# @Version  :1.0
# @Author   :李祎凡
# @File     :加一
# @Time     :2025/3/30 下午10:46
# @Other    :文件说明
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + 1 != 10:
                digits[i] = digits[i] + 1
                return digits
            elif i == 0 and (digits[i] + 1 == 10) :
                digits[i] = 0
                digits.insert(0, 1)
                return digits
            elif digits[i] + 1 == 10:
                digits[i] = 0


# AI
class Solution:
    def plusOne2(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # 当前位是9时置0
        # 循环结束说明所有位都是9，补1并返回
        return [1] + digits

s = Solution()
print(s.plusOne([9]))