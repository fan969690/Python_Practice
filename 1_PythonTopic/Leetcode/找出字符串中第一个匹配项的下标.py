# @Version  :1.0
# @Author   :李祎凡
# @File     :找出字符串中第一个匹配项的下标
# @Time     :2025/3/29 下午10:03
# @Other    :文件说明

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

s = Solution()
print(s.strStr('hello', 'll'))