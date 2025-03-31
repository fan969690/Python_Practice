# @Version  :1.0
# @Author   :李祎凡
# @File     :搜索插入位置
# @Time     :2025/3/29 下午10:26
# @Other    :文件说明


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 1 and (nums[0] == target or target < nums[0]):
            return 0
        elif len(nums) == 1 and nums[0] > target:
            return 1
        for i in range(len(nums)-1):
            if nums[i] > target:
                return i
            if target == nums[i]:
                return i
            elif target > nums[i] and (target < nums[i+1] or target == nums[i+1]):
                return i+1
        return len(nums)