# @Version  :1.0
# @Author   :李祎凡
# @File     :最长公共前缀
# @Time     :2025/3/24 下午9:42
# @Other    :思路 两两比较，求相同的其实串  再递归


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        tem = strs[0]
        for i in range(1,len(strs)):
            tem = self.alike(tem, strs[i])
            if tem == "":
                return ""
        return tem

    def alike(self ,str1: str, str2: str) -> str:
        tem = ""
        minlen = len(str1) if len(str1) < len(str2) else len(str2)
        for i in  range(0,minlen):
            if str1[i] == str2[i]:
                tem += str1[i]
            else:
                break
        return tem


s = Solution()
print(s.longestCommonPrefix(["ab","a"]))
