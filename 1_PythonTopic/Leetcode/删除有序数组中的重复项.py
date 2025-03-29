# @Version  :1.0
# @Author   :李祎凡
# @File     :删除有序数组中的重复项
# @Time     :2025/3/28 下午9:07
# @Other    :文件说明


# 慢
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n1 = 0
        n2 = 1
        while n2 < len(nums):
            while 1 :
                if nums[n1] == nums[n2]:
                    del nums[n2]
                    break
                else:
                    n1+=1
                    n2+=1
                    break
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums = list(set(nums))
        print(nums)
        return len(nums)

num = [1,1,3,3,3,5,5,7,7]
s = Solution()
print(s.removeDuplicates(num))