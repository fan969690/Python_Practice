# @Version  :1.0
# @Author   :李祎凡
# @File     :test1
# @Time     :2025/3/19 上午11:54
# @Other    :爬取搜狗页面/判断回文数
# import requests
#
# url = "https://www.sogou.com/web?query=%E6%9E%97%E4%BF%8A%E6%9D%B0&_ast=1742357427&_asf=www.sogou.com&w=01029901&cid=&s_from=result_up&sourceid=5_01_03&sessiontime=1742357469801"
#
# herders = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
# }
#
# resp = requests.get(url,headers=herders)
#
#
# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(resp.text)

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