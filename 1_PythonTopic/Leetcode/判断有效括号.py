# @Version  :1.0
# @Author   :李祎凡
# @File     :判断有效括号
# @Time     :2025/3/25 下午10:26
# @Other    :遇到正括号就通过，直到遇到反括号

class Solution:

    def isValid(self, s: str) -> bool:
        dict_1 = {')': '(', ']': '[', '}': '{'}

        while s != '':
            if len(s) <= 1:
                return False
            elif s[0] == "]" or s[0] == "}" or s[0] == ")":
                return False
            elif s == '':
                return True
            elif len(s) == 2 and s[1] in "({[":
                return False
            elif len(s) == 2 and s[0] == s[1]:
                return False
            elif len(s) == 2 and s[0] == dict_1[s[1]]:
                return True

            for i in range(1,len(s)):
                if s[i] == "(" or s[i] == "[" or s[i] == "{":
                    pass
                elif dict_1[s[i]] == s[i-1]:
                    s = s[:i-1]+s[i+1:]
                    print(s)
                    break
                else:
                    return False
                if i == len(s)-1:
                    return False

    def isValid2(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # 遇到右括号，检查栈顶元素
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # 左括号压入栈
                stack.append(char)

        # 栈为空则所有括号正确闭合
        return not stack

s = Solution()
print(s.isValid("([]){"))