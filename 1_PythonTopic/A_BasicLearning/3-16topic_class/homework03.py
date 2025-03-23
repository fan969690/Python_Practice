# @Version  :1.0
# @Author   :李祎凡
# @File     :homework03
# @Time     :2025/3/16 下午5:27
import math


class Circle:
    r = None
    def perimeter(self):
        return self.r * 2 * math.pi

    def area(self):
        return self.r * math.pi **2


circle = Circle()
circle.r = 2
print(circle.perimeter())
print(circle.area())