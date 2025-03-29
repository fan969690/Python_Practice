# @Version  :1.0
# @Author   :李祎凡
# @File     :罗马数字转整数
# @Time     :2025/3/23 下午10:30
# @Other    :文件说明


class Solution:
    ROM = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # enumerate(iterable, start=0)
    # 返回一个枚举对象。iterable
    # 必须是一个序列，或
    # iterator，或其他支持迭代的对象。 enumerate()
    # 返回的迭代器的
    # __next__()
    # 方法返回一个元组，里面包含一个计数值（从
    # start
    # 开始，默认为
    # 0）和通过迭代
    # iterable
    # 获得的值。
    # seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    # list(enumerate(seasons))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    # list(enumerate(seasons, start=1))
    # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    def romanToInt(self, s: str) -> int:
        # print(s[1])
        Sum_total = 0
        n = len(s)
        for i,ch in enumerate(s):
            # [(0,'M'),(1,'I'),(2,'V')]
            value = Solution.ROM[ch]
            if i < n - 1 and value < Solution.ROM[s[i + 1]]:
                Sum_total -= value
            else:
                Sum_total += value
        return Sum_total

s = Solution()
print(s.romanToInt("MIV"))