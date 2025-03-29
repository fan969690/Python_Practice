# @Version  :1.0
# @Author   :李祎凡
# @File     :移除元素
# @Time     :2025/3/28 下午9:45
# @Other    :文件说明

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        n = len(nums)-1
        while i <= n:
            if nums[i] == val:
                nums[i],nums[n] = nums[n],nums[i]
                nums[n] = -1
                n = n-1
            else:
                i += 1
        return n+1