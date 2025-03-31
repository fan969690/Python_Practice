# @Version  :1.0
# @Author   :李祎凡
# @File     :最后一个单词的长度
# @Time     :2025/3/29 下午10:44
# @Other    :文件说明


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        print(s)
        for i in s[::-1]:
            print(i)
            if i != '':
                return len(i)


s = Solution()
print(s.lengthOfLastWord('   fly me   to   the moon  '))