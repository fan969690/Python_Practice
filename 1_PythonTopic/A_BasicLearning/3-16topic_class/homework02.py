# @Version  :1.0
# @Author   :李祎凡
# @File     :homework02
# @Time     :2025/3/16 下午5:24

class Book:
    price = None

    def update_price(self):
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100

book1 = Book()
book1.price = 50
print(book1.price)
book1.update_price()
print(book1.price)