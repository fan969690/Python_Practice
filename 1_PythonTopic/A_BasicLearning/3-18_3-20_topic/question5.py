# @Version  :1.0
# @Author   :李祎凡
# @File     :question
# @Time     :2025/3/18 下午6:16
# @Other    :文件说明
# Define a class which has at least two methods: getString: to get a string from
# console input printString: to print the string in upper case. Also please
# include simple test function to test the class methods.
# 定义一个类，它至少有两个方法：getString：从控制台输入获取字符串；
# printString：以大写打印字符串。也请包括简单的测试功能来测试类的方法。

class tools(object):
    def getString(self):
        return input("Enter a string: ")
    def printString(self,STR:str):
        return print(STR.upper())


tools = tools()
str1 = tools.getString()
tools.printString(str1)